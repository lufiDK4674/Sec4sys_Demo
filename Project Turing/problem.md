# Problem: Balanced Partition Trees

## Problem Statement

You are given a tree with `n` nodes, numbered from 1 to n. Each node `i` has a weight `w[i]`. You want to partition this tree into several **connected components** by removing some edges.

Each connected component in your partition should be **balanced**: the sum of weights in the component should be between `T - K` and `T + K` (inclusive), where `T` is a given target value and `K` is the allowed tolerance.

Your goal is to minimize the number of edges you need to remove to create such a balanced partition.

## Input

The first line contains three integers `n`, `T`, and `K` (1 ≤ n ≤ 2×10^5, 1 ≤ T ≤ 10^9, 0 ≤ K ≤ 10^9).

The second line contains `n` integers `w[1], w[2], ..., w[n]` (1 ≤ w[i] ≤ 10^6).

The next `n-1` lines each contain two integers `u` and `v` (1 ≤ u, v ≤ n, u ≠ v), representing an edge between nodes `u` and `v`.

## Output

Output a single integer: the minimum number of edges that need to be removed to create a balanced partition. If no balanced partition is possible, output -1.

## Constraints

- 1 ≤ n ≤ 2×10^5
- 1 ≤ T ≤ 10^9  
- 0 ≤ K ≤ 10^9
- 1 ≤ w[i] ≤ 10^6
- The given edges form a tree (connected, acyclic)

## Examples

### Example 1
```
Input:
5 10 2
3 7 4 5 1
1 2
2 3  
2 4
4 5

Output:
1
```

**Explanation**: 
Tree structure:
```
    1(3)
    |
    2(7)
   / \
  3(4) 4(5)
       |
       5(1)
```

We can remove edge (2,4) to get components:
- {1,2,3} with sum 3+7+4 = 14 (invalid, > T+K = 12)
- {4,5} with sum 5+1 = 6 (invalid, < T-K = 8)

Better solution: Remove edge (2,3) to get:
- {1,2,4,5} with sum 3+7+5+1 = 16 (invalid)
- {3} with sum 4 (invalid)

Optimal: Remove edge (4,5) to get:
- {1,2,3,4} with sum 3+7+4+5 = 19 (invalid)

Wait, let me recalculate: Remove edge (1,2):
- {1} with sum 3 (invalid, < 8)  
- {2,3,4,5} with sum 7+4+5+1 = 17 (invalid, > 12)

Actually, remove edge (2,4) gives us:
- {1,2,3} with sum 14 (too big)
- {4,5} with sum 6 (too small)

The optimal solution is to remove edge (3,2), giving:
- {1,2,4,5} with sum 16 (too big)
- {3} with sum 4 (too small)

Let me fix this example...

### Example 1 (Corrected)
```
Input:
6 10 3
2 4 3 5 2 4
1 2
2 3
2 4  
4 5
4 6

Output:
1
```

By removing edge (4,5), we get:
- {1,2,3,4,6} with sum 2+4+3+5+4 = 18 (invalid, > 13)
- {5} with sum 2 (invalid, < 7)

By removing edge (2,4), we get:
- {1,2,3} with sum 2+4+3 = 9 (valid, in [7,13])
- {4,5,6} with sum 5+2+4 = 11 (valid, in [7,13])

So the answer is 1.

### Example 2
```
Input:
3 5 1
3 2 7
1 2
2 3

Output:
-1
```

**Explanation**: No matter how we partition, we cannot satisfy the balance constraint. Each single node is outside [4,6], and any pair exceeds the range.
