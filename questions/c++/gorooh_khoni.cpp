#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

unordered_map<string, int> bloodTypeMap = {
    {"O-", 0}, {"O+", 1}, {"A-", 2}, {"A+", 3},
    {"B-", 4}, {"B+", 5}, {"AB-", 6}, {"AB+", 7}
};

vector<int> parseBloodType(const string &bloodType) {
    vector<int> materials(3, 0);
    
    if (bloodType == "A-" || bloodType == "A+" || bloodType == "AB-" || bloodType == "AB+") {
        materials[0] = 1;
    }
    
    if (bloodType == "B-" || bloodType == "B+" || bloodType == "AB-" || bloodType == "AB+") {
        materials[1] = 1;
    }
    
    if (bloodType == "O+" || bloodType == "A+" || bloodType == "B+" || bloodType == "AB+") {
        materials[2] = 1;
    }
    
    return materials;
}

bool isValidBloodType(const vector<int> &parent1, const vector<int> &parent2, const vector<int> &child) {
    for (int i = 0; i < 3; ++i) {
        if (child[i] && !parent1[i] && !parent2[i]) {
            return false;
        }
    }
    return true;
}

int main() {
    int t;
    cin >> t;
    cin.ignore();
    
    while (t--) {
        string d, m, c;
        cin >> d >> m >> c;
        
        vector<int> dad = parseBloodType(d);
        vector<int> mom = parseBloodType(m);
        vector<int> child = parseBloodType(c);
        
        if (isValidBloodType(dad, mom, child)) {
            cout << "valid" << endl;
        } else {
            cout << "invalid" << endl;
        }
    }
    
    return 0;
}
