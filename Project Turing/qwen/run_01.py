# Qwen Run 1 - Greedy Approach (Failed)

def solve():
    n, T, K = map(int, input().split())
    w = [0] + list(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Simple greedy: start from any node and grow component greedily
    visited = [False] * (n + 1)
    cuts = 0
    
    for start in range(1, n + 1):
        if visited[start]:
            continue
            
        # Grow component greedily from start
        current_sum = 0
        component = []
        queue = [start]
        
        while queue:
            u = queue.pop(0)
            if visited[u]:
                continue
                
            # Try adding this node
            if current_sum + w[u] <= T + K:
                visited[u] = True
                current_sum += w[u]
                component.append(u)
                
                for v in adj[u]:
                    if not visited[v]:
                        queue.append(v)
            else:
                # Need to cut edge to u
                cuts += 1
        
        # Check if component is valid
        if current_sum < T - K:
            print(-1)
            return
    
    print(cuts)

solve()

# This approach fails because:
# 1. Greedy doesn't guarantee optimal cuts
# 2. The order of exploration affects the result
# 3. Doesn't consider tree structure properly
