# Qwen Run 3 - Implementation Bugs (Failed)

def solve():
    n, T, K = map(int, input().split())
    w = [0] + list(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    subtree_sum = [0] * (n + 1)
    min_cuts = [float('inf')] * (n + 1)
    
    def dfs(u, parent):
        subtree_sum[u] = w[u]
        children = []
        
        for v in adj[u]:
            if v != parent:
                children.append(v)
                dfs(v, u)
                subtree_sum[u] += subtree_sum[v]
        
        # Check if entire subtree is balanced
        if T - K <= subtree_sum[u] <= T + K:
            min_cuts[u] = 0
        
        # Try cutting children
        if children:
            total_cuts = 0
            for v in children:
                total_cuts += min_cuts[v]
                total_cuts += 1  # Cut edge to child
            
            # Bug: doesn't check if remaining node is valid
            min_cuts[u] = min(min_cuts[u], total_cuts)
    
    dfs(1, -1)
    
    # Bug: doesn't handle root specially
    if min_cuts[1] == float('inf'):
        print(-1)
    else:
        print(min_cuts[1])

solve()

# This approach fails because:
# 1. Doesn't check if the remaining single node is valid after cuts
# 2. Always adds cut cost even when child can't be balanced
# 3. Incorrect handling of the root node case
# 4. Off-by-one errors in cut counting
