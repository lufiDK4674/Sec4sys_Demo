# Qwen Run 2 - Wrong DP State (Failed)

def solve():
    n, T, K = map(int, input().split())
    w = [0] + list(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # DP with wrong state definition
    dp = {}  # dp[(node, included)] = min cuts for subtree
    
    def dfs(u, parent, included):
        if (u, included) in dp:
            return dp[(u, included)]
        
        if included:
            # Include this node in current component
            result = 0
            total_sum = w[u]
            
            for v in adj[u]:
                if v != parent:
                    child_result = dfs(v, u, True)
                    result += child_result
                    # This is wrong - we don't track sums properly
            
            if total_sum > T + K:
                result = float('inf')
        else:
            # Start new component from this node
            result = 1  # Cut edge to parent
            for v in adj[u]:
                if v != parent:
                    result += dfs(v, u, True)
        
        dp[(u, included)] = result
        return result
    
    answer = dfs(1, -1, True)
    print(-1 if answer == float('inf') else answer)

solve()

# This approach fails because:
# 1. DP state doesn't properly track component sums
# 2. The included/excluded binary state is insufficient  
# 3. Doesn't handle the balance constraint correctly
