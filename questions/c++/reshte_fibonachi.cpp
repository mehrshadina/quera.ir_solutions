#include <iostream>
#include <string>

using namespace std;

bool fib(int n) {
    if (n == 0) return true;
    if (n == 1) return true;

    int a = 1;
    int b = 1;
    int c = 0;

    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
        if (n == c) {
            return true;
        } 
        
    }
    //cout << endl;
    return false;
}

int main() {
    int n;
    cin >> n;

    for (int i = 1; i < n+1; i++) {
        //cout << i << endl;
        if (fib(i)) {
            cout << "+";
        } else {
            cout << "-";
        }
    }

    return 0;
}
