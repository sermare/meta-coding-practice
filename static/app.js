// ─── CodeMirror Editor Init ──────────────────────────────────
var editor = null;

document.addEventListener('DOMContentLoaded', function() {
    var textarea = document.getElementById('code-editor');
    if (!textarea) return; // Not on problem page

    editor = CodeMirror.fromTextArea(textarea, {
        mode: 'python',
        theme: 'monokai',
        lineNumbers: true,
        indentUnit: 4,
        tabSize: 4,
        indentWithTabs: false,
        matchBrackets: true,
        autoCloseBrackets: true,
        lineWrapping: false,
        extraKeys: {
            'Tab': function(cm) {
                cm.replaceSelection('    ', 'end');
            },
            'Ctrl-Enter': function() { runTests(); },
            'Cmd-Enter': function() { runTests(); },
            'Ctrl-/': 'toggleComment',
            'Cmd-/': 'toggleComment'
        }
    });

    // Load saved code from localStorage
    var savedCode = localStorage.getItem('code_' + PROBLEM_ID);
    if (savedCode) {
        editor.setValue(savedCode);
    }

    // Auto-save on change
    editor.on('change', function() {
        localStorage.setItem('code_' + PROBLEM_ID, editor.getValue());
    });

    // Button handlers
    document.getElementById('run-btn').addEventListener('click', runTests);
    document.getElementById('reset-btn').addEventListener('click', resetCode);

    // Pane resizer
    initResizer();
});


// ─── Run Tests ───────────────────────────────────────────────
function runTests() {
    var btn = document.getElementById('run-btn');
    var status = document.getElementById('run-status');
    var resultsBody = document.getElementById('results-body');
    var resultsSummary = document.getElementById('results-summary');

    btn.disabled = true;
    btn.innerHTML = '<span class="btn-icon">&#9203;</span> Running...';
    status.textContent = '';
    resultsBody.innerHTML = '<div class="results-placeholder">Running tests...</div>';
    resultsSummary.textContent = '';
    resultsSummary.className = 'results-summary';

    var code = editor.getValue();

    fetch('/api/run/' + PROBLEM_ID, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code: code })
    })
    .then(function(response) { return response.json(); })
    .then(function(data) {
        renderResults(data);
    })
    .catch(function(err) {
        resultsBody.innerHTML = '<div class="error-banner">Network error: ' + err.message + '</div>';
    })
    .finally(function() {
        btn.disabled = false;
        btn.innerHTML = '<span class="btn-icon">&#9654;</span> Run Tests';
    });
}


// ─── Render Results ──────────────────────────────────────────
function renderResults(data) {
    var resultsBody = document.getElementById('results-body');
    var resultsSummary = document.getElementById('results-summary');

    resultsBody.innerHTML = '';
    resultsSummary.textContent = '';
    resultsSummary.className = 'results-summary';

    // Handle errors
    if (data.error) {
        resultsBody.innerHTML = '<div class="error-banner">' + escapeHtml(data.error) + '</div>';
        resultsSummary.textContent = 'Error';
        resultsSummary.className = 'results-summary some-failed';

        // Still render any results we got
        if (!data.results || data.results.length === 0) return;
    }

    var results = data.results || [];
    var summary = data.summary || {};

    // Summary
    if (summary.all_passed) {
        resultsSummary.textContent = summary.passed + '/' + summary.total + ' Passed';
        resultsSummary.className = 'results-summary all-passed';

        var banner = document.createElement('div');
        banner.className = 'all-passed-banner';
        banner.textContent = 'All Tests Passed!';
        resultsBody.appendChild(banner);
    } else if (summary.total) {
        resultsSummary.textContent = summary.passed + '/' + summary.total + ' Passed';
        resultsSummary.className = 'results-summary some-failed';
    }

    // Individual results
    for (var i = 0; i < results.length; i++) {
        var r = results[i];
        var div = document.createElement('div');

        var statusClass = r.error ? 'error' : (r.passed ? 'passed' : 'failed');
        div.className = 'test-result ' + statusClass;

        var icon = r.passed ? '&#10003;' : '&#10007;';
        var iconClass = r.passed ? 'pass' : 'fail';

        var html = '<span class="test-icon ' + iconClass + '">' + icon + '</span>';
        html += '<div class="test-info">';
        html += '<div class="test-desc">Test ' + r.test_num + ': ' + escapeHtml(r.description) + '</div>';

        if (!r.passed) {
            html += '<div class="test-detail">';
            if (r.error) {
                html += '<span style="color: var(--red);">Error: ' + escapeHtml(r.error) + '</span>';
            } else {
                html += '<span>Expected: ' + escapeHtml(r.expected || '') + '</span>';
                html += '<span>Got: ' + escapeHtml(r.got || '') + '</span>';
            }
            html += '</div>';
        }

        html += '</div>';
        html += '<span class="test-time">' + (r.time_ms || 0) + 'ms</span>';

        div.innerHTML = html;
        resultsBody.appendChild(div);
    }
}


// ─── Reset Code ──────────────────────────────────────────────
function resetCode() {
    if (!confirm('Reset code to the original stub? Your changes will be lost.')) return;

    fetch('/api/reset/' + PROBLEM_ID)
    .then(function(response) { return response.json(); })
    .then(function(data) {
        if (data.code) {
            editor.setValue(data.code);
            localStorage.removeItem('code_' + PROBLEM_ID);
            document.getElementById('results-body').innerHTML =
                '<div class="results-placeholder">Code reset. Click "Run Tests" to test your solution.</div>';
            document.getElementById('results-summary').textContent = '';
        }
    });
}


// ─── Pane Resizer ────────────────────────────────────────────
function initResizer() {
    var resizer = document.getElementById('pane-resizer');
    if (!resizer) return;

    var leftPane = resizer.previousElementSibling;
    var container = resizer.parentElement;
    var isResizing = false;

    resizer.addEventListener('mousedown', function(e) {
        isResizing = true;
        resizer.classList.add('active');
        document.body.style.cursor = 'col-resize';
        document.body.style.userSelect = 'none';
        e.preventDefault();
    });

    document.addEventListener('mousemove', function(e) {
        if (!isResizing) return;
        var containerRect = container.getBoundingClientRect();
        var newWidth = e.clientX - containerRect.left;
        var minWidth = 300;
        var maxWidth = containerRect.width - 400;
        newWidth = Math.max(minWidth, Math.min(maxWidth, newWidth));
        leftPane.style.width = newWidth + 'px';
        leftPane.style.flex = 'none';
        // Force CodeMirror to refresh
        if (editor) editor.refresh();
    });

    document.addEventListener('mouseup', function() {
        if (isResizing) {
            isResizing = false;
            resizer.classList.remove('active');
            document.body.style.cursor = '';
            document.body.style.userSelect = '';
            if (editor) editor.refresh();
        }
    });
}


// ─── Utility ─────────────────────────────────────────────────
function escapeHtml(str) {
    if (!str) return '';
    var div = document.createElement('div');
    div.appendChild(document.createTextNode(str));
    return div.innerHTML;
}
