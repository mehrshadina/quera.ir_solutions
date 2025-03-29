#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> stones(7);
    for(int i = 0; i < 7; ++i) {
        std::cin >> stones[i];
    }
    
    int x;
    std::cin >> x;
    
    int pos = std::find(stones.begin(), stones.end(), x) - stones.begin();
    
    int fallenStones = 7 - pos;
    
    std::cout << fallenStones << std::endl;
    
    return 0;
}
