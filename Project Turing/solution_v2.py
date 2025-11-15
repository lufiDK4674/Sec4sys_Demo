def solve():
    n, T, K = map(int, input().split())
    w = [0] + list(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # For each node, compute minimum cuts needed for its subtree
    min_cuts = [float('inf')] * (n + 1)
    subtree_sum = [0] * (n + 1)
    
    def dfs(u, parent):
        subtree_sum[u] = w[u]
        children = []
        
        # Process children first
        for v in adj[u]:
            if v != parent:
                children.append(v)
                dfs(v, u)
                subtree_sum[u] += subtree_sum[v]
        
        # Try to keep the entire subtree as one component
        if T - K <= subtree_sum[u] <= T + K:
            min_cuts[u] = 0
        
        # Try different partitioning strategies
        # Strategy 1: Cut some/all children
        if children:
            # Try cutting all children
            total_cuts = 0
            all_valid = True
            
            for v in children:
                if min_cuts[v] == float('inf'):
                    all_valid = False
                    break
                total_cuts += min_cuts[v]
            
            if all_valid:
                # Check if the remaining node alone is valid
                if T - K <= w[u] <= T + K:
                    total_cuts += len(children)  # Add cuts for all child edges
                    min_cuts[u] = min(min_cuts[u], total_cuts)
        
        # For leaves that can't be balanced alone
        if not children and min_cuts[u] == float('inf'):
            min_cuts[u] = float('inf')  # Cannot balance single invalid node
    
    dfs(1, -1)
    
    if min_cuts[1] == float('inf'):
        print(-1)
    else:
        print(min_cuts[1])

solve()
