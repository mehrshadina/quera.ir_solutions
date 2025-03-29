#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

int countBarsa(string number) {
    int count = 0;
    int n = number.length();

    for (int i = 0; i < n; i++) {
        int num = 0;
        for (int j = i; j < n; j++) {
            //cout << (number[j] - '0') << "-" << num * 10 << endl;
            //if ((number[j] - '0') % 2 != 0)
            //    continue;
            num = (num * 10 + (number[j] - '0'));
            cout << number[j] << endl;
            if (number[j] == '0' || number[j] == '2' || number[j] == '6' || number[j] == '8') {
                //cout << number[j] << "#" << j << "#" << (number[j] - '0') << "#" << num * 10 << endl;
                if (num % 8 == 0)
                    ++count;
            }
        }
    }

    return count;
}

int main() {
    string number;
    cin >> number;

    int result = countBarsa(number);
    cout << result << endl;
   
    return 0;
}
