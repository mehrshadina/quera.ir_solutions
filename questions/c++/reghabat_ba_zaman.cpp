#include <iostream>
#include <vector>
using namespace std;

int main() {
    int m, buildings;
    cin >> m >> buildings;
    
    vector<int> heights;
    int height;
    for (int i = 0; i < buildings; ++i) {
        cin >> height;
        heights.push_back(height);
    }
    heights.push_back(0);
    
    int count = 0;
    int prev = 0;
    
    for (int i = 0; i < heights.size(); ++i) {
        int current = heights[i];
        
        if (current > prev) {
            int diff = current - prev;
            
            if (diff % m == 0) {
                count += diff / m;
            } else {
                count += diff / m + 1;
            }
        }
        
        if (current < prev) {
            int diff = prev - current;
            
            if (diff % m == 0) {
                count += diff / m;
            } else {
                count += diff / m + 1;
            }
        }
        
        prev = current;
    }
    
    count += buildings;
    
    cout << count << endl;
    
    return 0;
}
