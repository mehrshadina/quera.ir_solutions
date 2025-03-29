#include <iostream>
#include <string>

using namespace std;

string converttor(int n, const string& path) {
    string commands;
    char last_char = 'R';

    for (int i = 0; i < n; ++i) {
        switch (path[i]) {
            case 'U':
                if (last_char != 'U') {
                    if (last_char == 'D') {
                        commands += "RR";
                    } else if (last_char == 'L') {
                        commands += "RRR";
                    } else if (last_char == 'R') {
                        commands += "R";
                    }
                }
                commands += "F";
                last_char = 'U';
                break;
            case 'D':
                if (last_char != 'D') {
                    if (last_char == 'U') {
                        commands += "RR";
                    } else if (last_char == 'L') {
                        commands += "R";
                    } else if (last_char == 'R') {
                        commands += "RRR";
                    }
                }
                commands += "F";
                last_char = 'D';
                break;
            case 'L':
                if (last_char != 'L') {
                    if (last_char == 'R') {
                        commands += "RR";
                    } else if (last_char == 'D') {
                        commands += "RRR";
                    } else if (last_char == 'U') {
                        commands += "R";
                    }
                }
                commands += "F";
                last_char = 'L';
                break;
            case 'R':
                if (last_char != 'R') {
                    if (last_char == 'L') {
                        commands += "RR";
                    } else if (last_char == 'U') {
                        commands += "RRR";
                    } else if (last_char == 'D') {
                        commands += "R";
                    }
                }
                commands += "F";
                last_char = 'R';
                break;
            default:
                break;
        }
    }

    return commands;
}

int main() {
    int n;
    string path;


    cin >> n >> path;
    string robotCommands = converttor(n, path);
    cout << robotCommands << endl;

    return 0;
}
