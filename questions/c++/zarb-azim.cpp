#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

string multiplyStrings(const string& num1, const string& num2) {
    int m = num1.size();
    int n = num2.size();
    vector<int> result(m + n, 0);

    for (int i = m - 1; i >= 0; i--) {
        for (int j = n - 1; j >= 0; j--) {
            int mul = (num1[i] - '0') * (num2[j] - '0');
            int sum = mul + result[i + j + 1];
            result[i + j] += sum / 10;
            result[i + j + 1] = sum % 10;
        }
    }

    string product;
    for (int digit : result) {
        if (!(product.empty() && digit == 0)) {
            product.push_back(digit + '0');
        }
    }

    return product.empty() ? "0" : product;
}

string smallestNumber(const string& num) {
    string sortedNum = num;
    sort(sortedNum.begin(), sortedNum.end());
    return sortedNum;
}

string largestNumber(const string& num) {
    string sortedNum = num;
    sort(sortedNum.begin(), sortedNum.end(), greater<char>());
    return sortedNum;
}

int main() {
    string num;
    cin >> num;

    string smallest = smallestNumber(num);
    string largest = largestNumber(num);

    string product = multiplyStrings(smallest, largest);
    cout << product << endl;

    return 0;
}
