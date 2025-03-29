#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

// Comparator function to sort based on average, count, and j
bool compare(const pair<double, pair<int, int>>& a, const pair<double, pair<int, int>>& b) {
    if (a.first != b.first) // Sort based on average
        return a.first < b.first;
    else if (a.second.first != b.second.first) // If averages are equal, sort based on count
        return a.second.first < b.second.first;
    else // If averages and counts are equal, sort based on j
        return a.second.second < b.second.second;
}

int main() {
    int n;
    cin >> n;

    vector<int> row_lengths(n);
    int max_rows = 0;
    int total_elements = 0;

    for (int i = 0; i < n; ++i) {
        cin >> row_lengths[i];
        max_rows = max(max_rows, row_lengths[i]);
        total_elements += row_lengths[i];
    }

    vector<vector<int>> matrix(n, vector<int>());

    int row_index = 0;
    for (int i = 0; i < total_elements; ++i) {
        int element;
        cin >> element;
        matrix[row_index].push_back(element);
        if (matrix[row_index].size() == row_lengths[row_index]) {
            row_index++;
        }
    }

    // Print the matrix elements
    /*cout << "Matrix Elements:" << endl;
    for (int i = 0; i < n; ++i) {
        cout << "Row " << i+1 << ": ";
        for (int j = 0; j < matrix[i].size(); ++j) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }*/

    // Calculate the average of each column
    vector<pair<double, pair<int, int>>> column_averages;

    for (int j = 0; j < max_rows; ++j) {
        double sum = 0.0;
        int count = 0;
        for (int i = 0; i < n; ++i) {
            if (j < matrix[i].size()) {
                sum += matrix[i][j];
                count++;
            }
        }
        double average = (sum / count);
        column_averages.push_back({average, {count, j}});
    }

    sort(column_averages.begin(), column_averages.end(), compare);

    // Print the column numbers in ascending order of their averages
    //cout << "Column Numbers in Ascending Order of Averages:" << endl;
    for (auto& pair : column_averages) {
        cout << pair.second.second + 1 << " ";
    }
    cout << endl;

    return 0;
}
