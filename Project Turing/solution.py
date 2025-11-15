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
        
        # Process all children first
        children = []
        for v in adj[u]:
            if v != parent:
                children.append(v)
                dfs(v, u)
                subtree_sum[u] += subtree_sum[v]
        
        # Option 1: Keep entire subtree together
        if T - K <= subtree_sum[u] <= T + K:
            min_cuts[u] = 0
        
        # Option 2: Cut children and keep only this node
        if T - K <= w[u] <= T + K:
            total_child_cuts = 0
            all_children_solvable = True
            
            for v in children:
                if min_cuts[v] == float('inf'):
                    all_children_solvable = False
                    break
                total_child_cuts += min_cuts[v]
            
            if all_children_solvable:
                cuts_needed = total_child_cuts + len(children)
                min_cuts[u] = min(min_cuts[u], cuts_needed)
    
    dfs(1, -1)
    
    if min_cuts[1] == float('inf'):
        print(-1)
    else:
        print(min_cuts[1])

solve()
