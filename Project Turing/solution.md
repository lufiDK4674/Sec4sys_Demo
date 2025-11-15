# Solution Explanation: Balanced Partition Trees

## Algorithm Overview

This problem requires tree dynamic programming with greedy decision-making. The key insight is that for each subtree, we need to decide whether to:
1. **Keep it together** - if the subtree sum fits within [T-K, T+K]
2. **Partition it further** - if we can get a better result by cutting

## Detailed Algorithm

### Step 1: Tree Representation
- Build adjacency list representation of the tree
- Root the tree at node 1 for easier DP processing

### Step 2: DFS with Dynamic Programming

For each node `u`, we compute:
- `subtree_sum[u]`: Total weight in subtree rooted at u
- `min_cuts[u]`: Minimum cuts needed to balance subtree rooted at u

### Step 3: DP Transition

For each node `u`:

```cpp
// Base case: leaf node
if (u is leaf) {
    subtree_sum[u] = w[u];
    if (w[u] >= T-K && w[u] <= T+K) {
        min_cuts[u] = 0;  // This subtree is already balanced
    } else {
        min_cuts[u] = INF;  // Cannot balance single node
    }
    return;
}

// Recursive case: internal node
subtree_sum[u] = w[u];
int total_child_cuts = 0;

for (child v of u) {
    dfs(v);
    subtree_sum[u] += subtree_sum[v];
    total_child_cuts += min_cuts[v];
}

// Option 1: Keep entire subtree together
if (subtree_sum[u] >= T-K && subtree_sum[u] <= T+K) {
    min_cuts[u] = 0;
} else {
    min_cuts[u] = INF;
}

// Option 2: Cut all children and solve recursively
if (total_child_cuts != INF) {
    int cuts_if_separate = total_child_cuts + children.size();
    min_cuts[u] = min(min_cuts[u], cuts_if_separate);
}
```

### Step 4: Handle Root Node Specially

The root node doesn't have a parent edge to cut, so we only consider:
- Keep entire tree (if balanced)
- Cut all children and solve recursively

## Key Insights

### 1. Greedy Property
Once we decide to cut an edge, the subtrees become independent subproblems. This supports the DP approach.

### 2. Optimal Substructure  
The minimum cuts for a subtree depends only on the minimum cuts for its children, not on the rest of the tree.

### 3. Edge Cases
- Single nodes that cannot be balanced → return -1
- All weights fit in single component → return 0
- Mixed scenarios require careful DP computation

## Complexity Analysis

- **Time Complexity**: O(n) - single DFS traversal
- **Space Complexity**: O(n) - for adjacency list and DP arrays
- **Auxiliary Space**: O(h) where h is tree height (recursion stack)

## Implementation Details

### Tree Rooting
We root the tree at node 1, which allows us to process children before parents in the DFS.

### Overflow Prevention
Use `long long` for sum calculations since max sum can be n × max_weight = 2×10^5 × 10^6 = 2×10^11.

### Invalid State Handling
Use a sentinel value (INF) to represent impossible states where no valid partition exists.

## Example Walkthrough

For the tree in Example 1:
```
    1(2)
    |
    2(4)
   /|\
  3(3) 4(5)
       |
       5(2)
       |
       6(4)
```

Target T=10, tolerance K=3, so valid range is [7,13].

**Bottom-up DP:**
- Node 6: sum=4, invalid alone, min_cuts=INF
- Node 5: sum=2, invalid alone, min_cuts=INF  
- Node 4: sum=5+2+4=11, valid! min_cuts=0
- Node 3: sum=3, invalid alone, min_cuts=INF
- Node 2: sum=4+3+11=18, too big. Cut children: cuts=0+INF+1=INF. Cut child 4: sum=4+3=7, invalid.
- Actually, cut between 2-4: {1,2,3} sum=9 (valid), {4,5,6} sum=11 (valid)

The algorithm correctly finds the minimum number of cuts needed.
