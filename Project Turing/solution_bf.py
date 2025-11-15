def solve_bf():
    """Brute force solution - try all possible edge cuts"""
    n, T, K = map(int, input().split())
    w = [0] + list(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    def get_components(removed_edges):
        """Get connected components after removing edges"""
        temp_adj = [[] for _ in range(n + 1)]
        removed_set = set(removed_edges)
        
        for u, v in edges:
            if (u, v) not in removed_set and (v, u) not in removed_set:
                temp_adj[u].append(v)
                temp_adj[v].append(u)
        
        visited = [False] * (n + 1)
        components = []
        
        for i in range(1, n + 1):
            if not visited[i]:
                component = []
                stack = [i]
                while stack:
                    node = stack.pop()
                    if not visited[node]:
                        visited[node] = True
                        component.append(node)
                        for neighbor in temp_adj[node]:
                            if not visited[neighbor]:
                                stack.append(neighbor)
                components.append(component)
        
        return components
    
    def is_balanced(component):
        """Check if component sum is within [T-K, T+K]"""
        total = sum(w[node] for node in component)
        return T - K <= total <= T + K
    
    # Try all possible combinations of edge removals
    from itertools import combinations
    
    for num_cuts in range(n):  # 0 to n-1 cuts
        for removed_edges in combinations(edges, num_cuts):
            components = get_components(removed_edges)
            if all(is_balanced(comp) for comp in components):
                print(num_cuts)
                return
    
    print(-1)

solve_bf()
