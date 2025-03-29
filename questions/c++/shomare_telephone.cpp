#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool splitNumber(const string& number, vector<string>& segments) {
    int n = number.length();
    if (n < 2) return false;
    
    for (int i = 0; i < n; ) {
        if (i + 2 <= n && number[i] != '0') {
            segments.push_back(number.substr(i, 2));
            i += 2;
        } else if (i + 3 <= n && number[i] != '0') {
            segments.push_back(number.substr(i, 3));
            i += 3;
        } else {
            return false;
        }
    }
    return true;
}

int main() {
    int q;
    cin >> q;
    
    while (q--) {
        int y;
        string x;
        cin >> y >> x;
        
        vector<string> segments;
        
        if (splitNumber(x, segments)) {
            cout << "YES" << endl;
            cout << segments.size() << endl;
            for (const string& segment : segments) {
                cout << segment << endl;
            }
        } else {
            cout << "NO" << endl;
        }
    }
    
    return 0;
}
