#include <iostream>
#include <string>
using namespace std;

int countBarsa(string number) {
    int count = 0;
    int n = number.length();

    for (int i = 0; i < n; ++i) {
        if ((number[i] - '0') % 8 == 0)
            ++count;
        cout << number[i] - '0' << endl;
        int num = (number[i-1] - '0') * 10 + (number[i] - '0');
        if (num > 0 )
            cout << num << endl;
        if (num >= 0 && num % 8 == 0)
            ++count;
            
    }

    for (int i = 2; i < n; ++i) {
        int num = (number[i-2] - '0') * 100 + (number[i-1] - '0') * 10 + (number[i] - '0');
        if (num > 0)
        cout << num << endl;
        if (num >= 0 && num % 8 == 0) {
            count += (i-1);
        }
    }

    return count;
}

int main() {
    string number;
    cin >> number;

    cout << countBarsa(number) << endl;

    return 0;
}
