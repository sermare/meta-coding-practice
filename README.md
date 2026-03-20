# META Coding Interview Practice

A **LeetCode-style local testing environment** for the **top 50 most common META/Facebook coding interview questions**. No account needed, no internet required — just clone, solve, and test.

## Requirements

- Python 3.6+
- pip

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/meta-coding-practice.git
cd meta-coding-practice

# 2. (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
# venv\Scripts\activate    # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. List all 50 problems
python3 runner.py list

# 5. Pick a problem and start solving!
python3 runner.py describe 1
```

## How It Works

### 1. Browse problems

```bash
python3 runner.py list                        # All 50 problems
python3 runner.py list --difficulty easy       # Filter: easy | medium | hard
python3 runner.py list --category "Trees"     # Filter by category keyword
```

### 2. Read the problem statement

```bash
python3 runner.py describe 8
```

Shows the full description, constraints, examples, difficulty, category, and source link.

### 3. Implement your solution

Open `problems/p008_number_of_islands.py` and replace the stub:

```python
# Before (stub)
def solution(grid):
    return None

# After (your solution)
def solution(grid):
    if not grid:
        return 0
    count = 0
    # ... your code here
    return count
```

### 4. Test it

```bash
python3 runner.py test 8        # Run tests for problem 8
python3 runner.py test 8 -v     # Verbose: see inputs, expected vs actual
python3 runner.py test all      # Run all 50 problems at once
```

### 5. Track your progress

```bash
python3 runner.py progress
```

Shows solved/attempted/remaining counts broken down by difficulty.

## Project Structure

```
meta-coding-practice/
├── runner.py               # Main CLI test runner
├── problem_registry.py     # Problem metadata (title, difficulty, source links)
├── requirements.txt        # Python dependencies (colorama, tabulate)
├── problems/               # 50 problem files — edit these!
│   ├── p001_two_sum.py
│   ├── p002_move_zeroes.py
│   ├── ...
│   └── p050_simplify_path.py
└── tests/                  # Test cases for each problem
    ├── test_p001_two_sum.py
    ├── test_p002_move_zeroes.py
    ├── ...
    └── test_p050_simplify_path.py
```

## All 50 Problems

| # | Problem | Difficulty | Category | LeetCode |
|---|---------|-----------|----------|----------|
| 1 | Two Sum | Easy | Arrays & Hashing | [#1](https://leetcode.com/problems/two-sum/) |
| 2 | Move Zeroes | Easy | Arrays | [#283](https://leetcode.com/problems/move-zeroes/) |
| 3 | Valid Palindrome | Easy | Strings | [#125](https://leetcode.com/problems/valid-palindrome/) |
| 4 | Best Time to Buy and Sell Stock | Easy | Arrays & DP | [#121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) |
| 5 | Valid Parentheses | Easy | Stacks | [#20](https://leetcode.com/problems/valid-parentheses/) |
| 6 | Merge Sorted Array | Easy | Arrays | [#88](https://leetcode.com/problems/merge-sorted-array/) |
| 7 | Reverse Linked List | Easy | Linked Lists | [#206](https://leetcode.com/problems/reverse-linked-list/) |
| 8 | Number of Islands | Medium | Graphs | [#200](https://leetcode.com/problems/number-of-islands/) |
| 9 | Palindrome Linked List | Easy | Linked Lists | [#234](https://leetcode.com/problems/palindrome-linked-list/) |
| 10 | Product of Array Except Self | Medium | Arrays | [#238](https://leetcode.com/problems/product-of-array-except-self/) |
| 11 | 3Sum | Medium | Arrays | [#15](https://leetcode.com/problems/3sum/) |
| 12 | Merge Intervals | Medium | Arrays & Sorting | [#56](https://leetcode.com/problems/merge-intervals/) |
| 13 | Group Anagrams | Medium | Strings & Hashing | [#49](https://leetcode.com/problems/group-anagrams/) |
| 14 | Binary Tree Level Order Traversal | Medium | Trees | [#102](https://leetcode.com/problems/binary-tree-level-order-traversal/) |
| 15 | Clone Graph | Medium | Graphs | [#133](https://leetcode.com/problems/clone-graph/) |
| 16 | Word Break | Medium | Dynamic Programming | [#139](https://leetcode.com/problems/word-break/) |
| 17 | LRU Cache | Medium | Design | [#146](https://leetcode.com/problems/lru-cache/) |
| 18 | Validate Binary Search Tree | Medium | Trees | [#98](https://leetcode.com/problems/validate-binary-search-tree/) |
| 19 | Lowest Common Ancestor of Binary Tree | Medium | Trees | [#236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) |
| 20 | Subsets | Medium | Backtracking | [#78](https://leetcode.com/problems/subsets/) |
| 21 | Search in Rotated Sorted Array | Medium | Binary Search | [#33](https://leetcode.com/problems/search-in-rotated-sorted-array/) |
| 22 | Kth Largest Element in an Array | Medium | Sorting & Heaps | [#215](https://leetcode.com/problems/kth-largest-element-in-an-array/) |
| 23 | Letter Combinations of a Phone Number | Medium | Backtracking | [#17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) |
| 24 | Sort Colors | Medium | Arrays & Sorting | [#75](https://leetcode.com/problems/sort-colors/) |
| 25 | Decode Ways | Medium | Dynamic Programming | [#91](https://leetcode.com/problems/decode-ways/) |
| 26 | Implement Trie (Prefix Tree) | Medium | Trees & Design | [#208](https://leetcode.com/problems/implement-trie-prefix-tree/) |
| 27 | Course Schedule II | Medium | Graphs | [#210](https://leetcode.com/problems/course-schedule-ii/) |
| 28 | Word Search | Medium | Backtracking & Matrix | [#79](https://leetcode.com/problems/word-search/) |
| 29 | Diagonal Traverse | Medium | Matrix | [#498](https://leetcode.com/problems/diagonal-traverse/) |
| 30 | Maximum Swap | Medium | Math & Greedy | [#670](https://leetcode.com/problems/maximum-swap/) |
| 31 | Custom Sort String | Medium | Strings & Sorting | [#791](https://leetcode.com/problems/custom-sort-string/) |
| 32 | Basic Calculator II | Medium | Stacks & Math | [#227](https://leetcode.com/problems/basic-calculator-ii/) |
| 33 | Minimum Window Substring | Hard | Strings & Sliding Window | [#76](https://leetcode.com/problems/minimum-window-substring/) |
| 34 | Merge K Sorted Lists | Hard | Linked Lists & Heaps | [#23](https://leetcode.com/problems/merge-k-sorted-lists/) |
| 35 | Serialize and Deserialize Binary Tree | Hard | Trees & Design | [#297](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) |
| 36 | Trapping Rain Water | Hard | Arrays & Two Pointers | [#42](https://leetcode.com/problems/trapping-rain-water/) |
| 37 | Longest Consecutive Sequence | Medium | Arrays & Hashing | [#128](https://leetcode.com/problems/longest-consecutive-sequence/) |
| 38 | Add Binary | Easy | Strings & Math | [#67](https://leetcode.com/problems/add-binary/) |
| 39 | Pow(x, n) | Medium | Math & Recursion | [#50](https://leetcode.com/problems/powx-n/) |
| 40 | Next Permutation | Medium | Arrays | [#31](https://leetcode.com/problems/next-permutation/) |
| 41 | Maximal Rectangle | Hard | Stacks & DP | [#85](https://leetcode.com/problems/maximal-rectangle/) |
| 42 | Maximal Square | Medium | Dynamic Programming | [#221](https://leetcode.com/problems/maximal-square/) |
| 43 | Remove Invalid Parentheses | Hard | BFS & Backtracking | [#301](https://leetcode.com/problems/remove-invalid-parentheses/) |
| 44 | Expression Add Operators | Hard | Backtracking & Math | [#282](https://leetcode.com/problems/expression-add-operators/) |
| 45 | Integer to English Words | Hard | Strings & Math | [#273](https://leetcode.com/problems/integer-to-english-words/) |
| 46 | Minimum Size Subarray Sum | Medium | Sliding Window | [#209](https://leetcode.com/problems/minimum-size-subarray-sum/) |
| 47 | Diameter of Binary Tree | Easy | Trees | [#543](https://leetcode.com/problems/diameter-of-binary-tree/) |
| 48 | Longest Increasing Subsequence | Medium | Dynamic Programming | [#300](https://leetcode.com/problems/longest-increasing-subsequence/) |
| 49 | Multiply Strings | Medium | Strings & Math | [#43](https://leetcode.com/problems/multiply-strings/) |
| 50 | Simplify Path | Medium | Strings & Stacks | [#71](https://leetcode.com/problems/simplify-path/) |

## Difficulty Breakdown

- **Easy:** 10 problems
- **Medium:** 32 problems
- **Hard:** 8 problems

## Sources

All problems were identified as frequently asked META/Facebook interview questions from:

- [LeetCode - Meta/Facebook Company Tag](https://leetcode.com/company/facebook/)
- [GeeksforGeeks - Meta SDE Sheet](https://www.geeksforgeeks.org/dsa/facebookmeta-sde-sheet-interview-questions-and-answers/)
- [Educative - Cracking Top Facebook Coding Questions](https://www.educative.io/blog/cracking-top-facebook-coding-interview-questions)
- [Design Gurus - Top 20 Meta Interview Questions](https://www.designgurus.io/blog/top-20-coding-questions-to-pass-meta-interview)
- [GitHub Gist - Facebook Interview LeetCode Prep](https://gist.github.com/fielding/8e22a9e8c2eb4c707f10d3a2b5db59c7)

Each problem file includes the specific source URL where it was identified as a META question.

## Tips

- Start with **Easy** problems to warm up
- META interviews favor **Arrays, Strings, and Trees** — prioritize those categories
- Practice writing clean code **without an IDE** — META disables autocomplete in CoderPad
- Aim to solve Medium problems in **15-20 minutes** and Easy in **10 minutes**
- Use `python3 runner.py test <N> -v` to see exactly where your solution fails

## License

MIT
