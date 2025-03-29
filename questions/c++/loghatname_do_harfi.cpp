#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void nextString(
    int length, 
    vector<string>& strings
    ) {
    if (length == 0) {
        return;
    }

    if (length == 1) {
        strings.push_back("a");

        strings.push_back("b");

        return;
    }
    vector<string> shorterStrings;

    nextString(
        length - 1, 
        shorterStrings);

    for (string s : shorterStrings) {

        strings.push_back(
            s + "a"
            );

        strings.push_back(
            s + "b"
            );
    }
}

int main() {
    int n;
    cin >> n;

    vector<string> allStrings;
    int length = 1;
    while (allStrings.size() < n) {
        nextString(
            length, allStrings
            );
        length++;
    }
    
    sort(
        allStrings.begin(), 
        allStrings.end(), 
        [](const string &a, 
        const string &b
        ) {

        if (a.size() == b.size()) {
            return a < b;
        }
        return a.size() < b.size();
    });

    cout << allStrings[n - 1].back() << endl;

    return 0;
}
