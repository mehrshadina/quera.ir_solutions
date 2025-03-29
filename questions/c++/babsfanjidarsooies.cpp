#include <iostream>
#include <iomanip>
#include <cmath> // for tgamma

int main() {
    double m, gamma_m, n, gamma_n;

    // Input the values of m, Γ(m), and n
    std::cin >> m >> gamma_m >> n;
    //std::cout << m << '-' << n << std::endl; 
    while (true) {
        //std::cout << m << '-' << n << std::endl; 
        if (m == n){
            gamma_n = gamma_m;
            m ++;
            break;
        } else if (m < n) {
            gamma_m = gamma_m * m;
            m ++;
        } else if (m > n) {
            m --;
            gamma_m = gamma_m / m;
        }
    }
    // Output the result
    std::cout <<  gamma_n << std::endl;

    return 0;
}
