def solve():
    n, T, K = map(int, input().split())
    w = [0] + list(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # dp[u] = minimum cuts needed for subtree rooted at u
    dp = [float('inf')] * (n + 1)
    
    def dfs(u, parent):
        children = []
        child_sums = []
        
        for v in adj[u]:
            if v != parent:
                children.append(v)
                dfs(v, u)
                child_sums.append(dfs_sum(v, u))
        
        # Total sum of this subtree
        total_sum = w[u] + sum(child_sums)
        
        # Option 1: Keep entire subtree together
        if T - K <= total_sum <= T + K:
            dp[u] = 0
        
        # Option 2: Cut some children and form optimal partition
        if children:
            # Try cutting all children
            cuts = 0
            valid = True
            for v in children:
                if dp[v] == float('inf'):
                    valid = False
                    break
                cuts += dp[v] + 1  # +1 for the edge cut
            
            if valid and T - K <= w[u] <= T + K:
                dp[u] = min(dp[u], cuts)
    
    def dfs_sum(u, parent):
        total = w[u]
        for v in adj[u]:
            if v != parent:
                total += dfs_sum(v, u)
        return total
    
    dfs(1, -1)
    
    if dp[1] == float('inf'):
        print(-1)
    else:
        print(dp[1])

solve()
