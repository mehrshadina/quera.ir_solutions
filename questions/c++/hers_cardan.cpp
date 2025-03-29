#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const int MAXN = 500000;
vector<int> tree[MAXN];
int hangingIndex[MAXN];
int subtreeSize[MAXN];

void dfs(int node, int parent) {
    subtreeSize[node] = 1;
    int maxChildHanging = 0;
    for (int neighbor : tree[node]) {
        if (neighbor == parent) continue;
        dfs(neighbor, node);
        subtreeSize[node] += subtreeSize[neighbor];
        maxChildHanging = max(maxChildHanging, hangingIndex[neighbor]);
    }
    if (subtreeSize[node] == 1) {
        hangingIndex[node] = 1;
    } else {
        hangingIndex[node] = maxChildHanging + 1;
    }
}

void solve() {
    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        
        for (int i = 1; i <= n; i++) {
            tree[i].clear();
            hangingIndex[i] = 0;
            subtreeSize[i] = 0;
        }
        
        for (int i = 1; i < n; i++) {
            int u, v;
            cin >> u >> v;
            tree[u].push_back(v);
            tree[v].push_back(u);
        }

        dfs(1, -1);

        priority_queue<pair<int, int>> pq;
        for (int i = 2; i <= n; i++) {
            if (subtreeSize[i] == 1) {
                pq.push({1, i});
            }
        }

        while (k > 0 && !pq.empty()) {
            auto [hang, node] = pq.top();
            pq.pop();
            int parent = -1;
            for (int neighbor : tree[node]) {
                if (hangingIndex[neighbor] == hang - 1) {
                    parent = neighbor;
                    break;
                }
            }
            if (parent != -1) {
                hangingIndex[parent]--;
                if (parent != 1 && subtreeSize[parent] == 2) { // it becomes a new leaf
                    pq.push({hangingIndex[parent], parent});
                }
                subtreeSize[parent]--;
                k--;
            }
        }

        cout << hangingIndex[1] << endl;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    solve();
    return 0;
}
