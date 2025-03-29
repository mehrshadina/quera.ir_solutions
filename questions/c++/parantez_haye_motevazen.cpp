#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool isBalanced(string combination) {
    int n = combination.length();
    for (int i = 0; i < n / 2; ++i) {
        if ((combination[i] == '(' && combination[n - 1 - i] != ')') ||
            (combination[i] == ')' && combination[n - 1 - i] != '(')) {
            return false;
        }
    }
    return true;
}

void generateParentheses(int n, string current, int open, int close, vector<string>& result) {
    if (current.length() == 2 * n) {
        if (isBalanced(current)) {
            result.push_back(current);
        }
        return;
    }

    if (open < n) {
        generateParentheses(n, current + '(', open + 1, close, result);
    }

    if (close < open) {
        generateParentheses(n, current + ')', open, close + 1, result);
    }
}

vector<string> generateParentheses(int n) {
    vector<string> result;
    generateParentheses(n, "", 0, 0, result);
    return result;
}

int main() {
    int n;
    cin >> n;

    vector<string> parentheses = generateParentheses(n);

    for (const string& combination : parentheses) {
        cout << combination << endl;
    }

    return 0;
}
