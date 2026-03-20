#!/usr/bin/env python3
# Run with: python3 app.py
# Then open http://localhost:5000 in your browser
"""
META Coding Interview Practice - Web IDE
Flask application providing a LeetCode-style web interface.
"""
import json
import os
import re
import subprocess
import sys
import tempfile

from flask import Flask, render_template, request, jsonify, abort

from problem_registry import PROBLEMS, get_problem

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROGRESS_FILE = os.path.join(BASE_DIR, ".progress.json")


def _slug(title):
    return title.lower().replace(" ", "_").replace("(", "").replace(")", "").replace(",", "").replace("'", "")


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_progress(progress):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


def _read_problem_file(pid, p):
    slug = _slug(p["title"])
    filepath = os.path.join(BASE_DIR, "problems", "p{:03d}_{}.py".format(pid, slug))
    if not os.path.exists(filepath):
        return None, None
    with open(filepath, "r") as f:
        source = f.read()
    return source, filepath


def _extract_description(source):
    """Extract the DESCRIPTION string from source."""
    match = re.search(r'DESCRIPTION\s*=\s*"""(.*?)"""', source, re.DOTALL)
    if match:
        return match.group(1).strip()
    match = re.search(r"DESCRIPTION\s*=\s*'''(.*?)'''", source, re.DOTALL)
    if match:
        return match.group(1).strip()
    return "No description available."


def _extract_stub(source):
    """Extract everything after the DESCRIPTION block as editable code."""
    # Find end of DESCRIPTION assignment
    match = re.search(r'DESCRIPTION\s*=\s*""".*?"""\s*\n', source, re.DOTALL)
    if not match:
        match = re.search(r"DESCRIPTION\s*=\s*'''.*?'''\s*\n", source, re.DOTALL)
    if match:
        stub = source[match.end():]
        # Remove leading blank lines
        stub = stub.lstrip("\n")
        return stub
    return source


# ─── Routes ────────────────────────────────────────────────────────

@app.route("/")
def dashboard():
    progress = load_progress()
    problems = []
    for pid, p in sorted(PROBLEMS.items()):
        status = progress.get(str(pid), {}).get("status", "not_started")
        problems.append(dict(p, id=pid, status=status))

    solved = sum(1 for pr in problems if pr["status"] == "passed")
    total = len(problems)
    return render_template("dashboard.html", problems=problems, solved=solved, total=total)


@app.route("/problem/<int:pid>")
def problem_page(pid):
    p = get_problem(pid)
    if not p:
        abort(404)

    source, filepath = _read_problem_file(pid, p)
    if not source:
        abort(404)

    description = _extract_description(source)
    stub_code = _extract_stub(source)

    progress = load_progress()
    status = progress.get(str(pid), {}).get("status", "not_started")

    # Get prev/next problem IDs
    pids = sorted(PROBLEMS.keys())
    idx = pids.index(pid)
    prev_pid = pids[idx - 1] if idx > 0 else None
    next_pid = pids[idx + 1] if idx < len(pids) - 1 else None

    return render_template("problem.html",
                           problem=p, pid=pid,
                           description=description,
                           stub_code=stub_code,
                           status=status,
                           prev_pid=prev_pid,
                           next_pid=next_pid)


@app.route("/api/run/<int:pid>", methods=["POST"])
def run_tests(pid):
    p = get_problem(pid)
    if not p:
        return jsonify({"error": "Problem not found", "results": []}), 404

    data = request.get_json(force=True)
    code = data.get("code", "")

    if not code.strip():
        return jsonify({"error": "No code submitted", "results": []})

    # Write user code to temp file
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False, dir=BASE_DIR)
    try:
        tmp.write(code)
        tmp.close()

        result = subprocess.run(
            [sys.executable, os.path.join(BASE_DIR, "execute_user_code.py"),
             str(pid), tmp.name],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            timeout=15, cwd=BASE_DIR
        )

        stdout = result.stdout.decode("utf-8", errors="replace")
        stderr = result.stderr.decode("utf-8", errors="replace")

        if result.returncode != 0:
            return jsonify({"error": stderr or "Execution error", "results": []})

        try:
            output = json.loads(stdout)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid output from runner:\n" + stdout + "\n" + stderr, "results": []})

        # Update progress
        if output.get("summary", {}).get("all_passed"):
            progress = load_progress()
            progress[str(pid)] = {
                "status": "passed",
                "passed": output["summary"]["passed"],
                "total": output["summary"]["total"],
            }
            save_progress(progress)
        elif output.get("results"):
            progress = load_progress()
            if progress.get(str(pid), {}).get("status") != "passed":
                progress[str(pid)] = {
                    "status": "attempted",
                    "passed": output["summary"]["passed"],
                    "total": output["summary"]["total"],
                }
                save_progress(progress)

        return jsonify(output)

    except subprocess.TimeoutExpired:
        return jsonify({"error": "Time Limit Exceeded (15 seconds)", "results": []})
    except Exception as e:
        return jsonify({"error": str(e), "results": []})
    finally:
        try:
            os.unlink(tmp.name)
        except OSError:
            pass


@app.route("/api/reset/<int:pid>")
def reset_code(pid):
    p = get_problem(pid)
    if not p:
        return jsonify({"error": "Problem not found"}), 404

    source, _ = _read_problem_file(pid, p)
    if not source:
        return jsonify({"error": "Problem file not found"}), 404

    stub = _extract_stub(source)
    return jsonify({"code": stub})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print("Starting META Coding Practice IDE at http://localhost:{}".format(port))
    app.run(host="0.0.0.0", port=port, debug=True)
