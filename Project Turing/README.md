# Balanced Partition Trees - Competitive Programming Problem

## Overview
This repository contains a complete competitive programming problem suitable for Codeforces Div1/Div2 difficulty.

**Problem**: Given a weighted tree, partition it into balanced components by removing minimum edges, where each component's weight sum must be within a specified tolerance range.

## Problem Highlights
- **Difficulty**: Div1/Div2 level
- **Topics**: Tree DP, Greedy algorithms, Graph theory
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)

## Files Structure
- `problem.md` - Complete problem statement with examples
- `solution.md` - Detailed algorithm explanation  
- `solution.cpp` - Optimal C++ solution
- `solution.py` - Python implementation
- `solution_bf.py` - Brute force solution for testing
- `test_cases/` - Comprehensive test cases
- `qwen/` - Failed attempts by Qwen model
- `generator.py` - Test case generator
- `requirements.json` - Time/memory limits

## Key Features
✅ **Original problem** - Not found in existing contest archives  
✅ **Proven difficulty** - Qwen3-235B-A22B-2507 failed on 3 attempts  
✅ **Rich test cases** - Covers edge cases and various scenarios  
✅ **Complete explanation** - Detailed solution walkthrough  
✅ **Multiple implementations** - C++ and Python versions

## Algorithm Insight
The solution uses tree dynamic programming where for each subtree, we decide whether to keep it as one component (if balanced) or partition it optimally. The key insight is that the problem has optimal substructure - the best way to partition a subtree depends only on the best partitions of its children.

## Testing
Run the solution against test cases:
```bash
python solution.py < test_cases/1.in  # Expected: 1
python solution.py < test_cases/2.in  # Expected: -1
```

The problem has been designed to be challenging but fair, requiring both algorithmic insight and careful implementation.
