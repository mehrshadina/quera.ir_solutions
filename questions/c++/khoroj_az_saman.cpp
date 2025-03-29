#include <iostream>
#include <vector>
#include <algorithm>

const int MOD = 1000000007;

// Function to perform DFS and compute the size of the subtree for each node
void dfs(int node, const std::vector<std::vector<int>>& tree, std::vector<int>& subtree_size) {
    subtree_size[node] = 1;
    for (int child : tree[node]) {
        dfs(child, tree, subtree_size);
        subtree_size[node] += subtree_size[child];
    }
}

// Function to compute factorial modulo MOD
void compute_factorials(int n, std::vector<long long>& fact) {
    fact[0] = 1;
    for (int i = 1; i <= n; ++i) {
        fact[i] = fact[i - 1] * i % MOD;
    }
}

// Function to compute modular multiplicative inverse using Fermat's Little Theorem
long long mod_inv(long long a, long long m) {
    long long res = 1;
    long long k = m - 2;
    while (k) {
        if (k % 2) res = res * a % m;
        a = a * a % m;
        k /= 2;
    }
    return res;
}

// Function to compute binomial coefficient C(n, k) % MOD
long long binomial_coeff(int n, int k, const std::vector<long long>& fact) {
    if (k > n) return 0;
    return fact[n] * mod_inv(fact[k], MOD) % MOD * mod_inv(fact[n - k], MOD) % MOD;
}

// Function to print the tree structure
void print_tree(const std::vector<std::vector<int>>& tree) {
    std::cout << "Tree structure:" << std::endl;
    for (size_t i = 1; i < tree.size(); ++i) {
        std::cout << "Node " << i << ": ";
        for (int child : tree[i]) {
            std::cout << child << " ";
        }
        std::cout << std::endl;
    }
}

// Function to print the subtree sizes
void print_subtree_sizes(const std::vector<int>& subtree_size) {
    std::cout << "Subtree sizes:" << std::endl;
    for (size_t i = 1; i < subtree_size.size(); ++i) {
        std::cout << "Node " << i << ": " << subtree_size[i] << std::endl;
    }
}

int main() {
    int n;
    std::cin >> n;

    std::vector<int> parent(n + 1);
    std::vector<std::vector<int>> tree(n + 1);
    for (int i = 2; i <= n; ++i) {
        std::cin >> parent[i];
        tree[parent[i]].push_back(i);
    }

    std::vector<int> subtree_size(n + 1);
    dfs(1, tree, subtree_size);

    // Print the tree structure
    print_tree(tree);

    // Print the subtree sizes
    print_subtree_sizes(subtree_size);

    std::vector<long long> fact(n + 1);
    compute_factorials(n, fact);

    std::vector<long long> result(n + 1);
    for (int k = 1; k <= n; ++k) {
        long long total_ways = 0;
        for (int i = 1; i <= n; ++i) {
            if (subtree_size[i] >= k) {
                total_ways = (total_ways + binomial_coeff(subtree_size[i] - 1, k - 1, fact)) % MOD;
            }
        }
        result[k] = total_ways;
    }

    for (int k = 1; k <= n; ++k) {
        std::cout << result[k] << " ";
    }
    std::cout << std::endl;

    return 0;
}
