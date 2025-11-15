#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

int n;
long long T, K;
vector<long long> w;
vector<vector<int>> adj;
vector<long long> subtree_sum;
vector<int> min_cuts;

void dfs(int u, int parent) {
    subtree_sum[u] = w[u];
    
    // Process all children first
    vector<int> children;
    for (int v : adj[u]) {
        if (v != parent) {
            children.push_back(v);
            dfs(v, u);
            subtree_sum[u] += subtree_sum[v];
        }
    }
    
    // Option 1: Keep entire subtree together
    if (subtree_sum[u] >= T - K && subtree_sum[u] <= T + K) {
        min_cuts[u] = 0;
    } else {
        min_cuts[u] = INF;
    }
    
    // Option 2: Cut all children and solve recursively
    if (!children.empty()) {
        int total_child_cuts = 0;
        bool possible = true;
        
        for (int v : children) {
            if (min_cuts[v] == INF) {
                possible = false;
                break;
            }
            total_child_cuts += min_cuts[v];
        }
        
        if (possible) {
            // Check if current node alone is valid
            if (w[u] >= T - K && w[u] <= T + K) {
                int cuts_if_separate = total_child_cuts + children.size();
                min_cuts[u] = min(min_cuts[u], cuts_if_separate);
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> n >> T >> K;
    
    w.resize(n + 1);
    adj.resize(n + 1);
    subtree_sum.resize(n + 1);
    min_cuts.resize(n + 1);
    
    for (int i = 1; i <= n; i++) {
        cin >> w[i];
    }
    
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    
    dfs(1, -1);
    
    if (min_cuts[1] == INF) {
        cout << -1 << endl;
    } else {
        cout << min_cuts[1] << endl;
    }
    
    return 0;
}
