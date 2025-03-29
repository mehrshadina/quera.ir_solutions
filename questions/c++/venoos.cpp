#include <iostream>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    int borderCities = 2 * (n + m) - 4;

    if (n == 1) {
        borderCities = m;
    } else if (m == 1) {
        borderCities = n;
    }

    cout << borderCities << endl;

    return 0;
}
