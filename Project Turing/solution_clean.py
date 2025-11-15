def solve():
    n, T, K = map(int, input().split())
    w = [0] + list(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Calculate subtree sums and solve recursively
    subtree_sum = [0] * (n + 1)
    min_cuts = [float('inf')] * (n + 1)
    
    def calculate_subtree_sum(u, parent):
        subtree_sum[u] = w[u]
        for v in adj[u]:
            if v != parent:
                calculate_subtree_sum(v, u)
                subtree_sum[u] += subtree_sum[v]
    
    def solve_dp(u, parent):
        children = []
        for v in adj[u]:
            if v != parent:
                children.append(v)
                solve_dp(v, u)
        
        # Option 1: Keep entire subtree together
        if T - K <= subtree_sum[u] <= T + K:
            min_cuts[u] = 0
        
        # Option 2: Cut edges to children and solve independently
        if children:
            total_child_cuts = 0
            can_cut_all = True
            
            for v in children:
                if min_cuts[v] == float('inf'):
                    can_cut_all = False
                    break
                total_child_cuts += min_cuts[v]
            
            if can_cut_all and T - K <= w[u] <= T + K:
                cuts_with_separation = total_child_cuts + len(children)
                min_cuts[u] = min(min_cuts[u], cuts_with_separation)
    
    calculate_subtree_sum(1, -1)
    solve_dp(1, -1)
    
    print(-1 if min_cuts[1] == float('inf') else min_cuts[1])

solve()
