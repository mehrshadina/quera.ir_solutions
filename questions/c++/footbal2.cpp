#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

class Player {
public:
    string name;
    int price;
    int speed;
    int finishing;
    int defense;
    string team;

    Player(string _name, int _price, int _speed, int _finishing, int _defense) {
        name = _name;
        price = _price;
        speed = _speed;
        finishing = _finishing;
        defense = _defense;
        team = "";
    }

    void printDetails() const {
        cout << "Name: " << name << ", Price: " << price << ", Speed: " << speed << ", Finishing: " << finishing << ", Defense: " << defense << ", Team: " << team << endl;
    }
};

class Team {
public:
    string name;
    int money;
    int wins;
    int losses;
    int draws;
    vector<int> playerIDs;

    Team(string _name, int _money) {
        name = _name;
        money = _money;
        wins = 0;
        losses = 0;
    }

    void printDetails() const {
        cout << "Name: " << name << ", Money: " << money << ", Wins: " << wins << ", Losses: " << losses << endl;
    }
};

vector<Player> players;
vector<Team> teams;


void printAllPlayers() {
    cout << "All Players:" << endl;
    for (const auto &player : players) {
        player.printDetails();
    }
}

void printAllTeams() {
    cout << "All Teams:" << endl;
    for (const auto &team : teams) {
        team.printDetails();
    }
}

void newPlayer(string name, int price, int speed, int finishing, int defense) {
    Player player(name, price, speed, finishing, defense);
    players.push_back(player);
}

void newTeam(string name, int money) {
    Team team(name, money);
    teams.push_back(team);
}

void buyPlayer(int playerID, int teamID) {
    playerID = playerID - 1;
    if (playerID >= players.size()) {
        cout << "player with the id #" << playerID << " doesn't exist" << endl;
        return;
    }
    teamID = teamID -1;
    if (teamID >= teams.size()) {
        cout << "team with the id #" << teamID << " doesn't exist" << endl;
        return;
    }

    Player &player = players[playerID];
    Team &team = teams[teamID];

    if (player.team != "") {
        cout << "player already has a team" << endl;
        return;
    }

    if (team.money < player.price) {
        cout << "the team can't afford to buy this player" << endl;
        return;
    }

    team.money -= player.price;
    player.team = team.name;
    team.playerIDs.push_back(playerID);
    cout << "player added to the team successfully" << endl;
}

void match(int teamID1, int teamID2) {
    teamID1 = teamID1 - 1;
    teamID2 = teamID2 - 1;
    if (teamID1 >= teams.size() || teamID2 >= teams.size()) {
        cout << "team doesn't exist" << endl;
        return;
    }

    Team &team1 = teams[teamID1];
    Team &team2 = teams[teamID2];

    //cout << team1.playerIDs.size() << endl;
    //cout << team2.playerIDs.size() << endl;

    if (team1.playerIDs.size() < 11 || team2.playerIDs.size() < 11) {
        cout << "the game can not be held due to an insufficient number of the players" << endl;
        return;
    }

    int powerTeam1 = 0, powerTeam2 = 0;
    for (int playerID : team1.playerIDs) {
        powerTeam1 += players[playerID].speed + players[playerID].finishing;
    }

    for (int playerID : team2.playerIDs) {
        powerTeam2 += players[playerID].speed + players[playerID].defense;
    }

    //cout << powerTeam1 << endl;
    //cout << powerTeam2 << endl;

    if (powerTeam1 > powerTeam2) {
        team1.wins++;
        team2.losses++;
        team1.money += 1000;
        //cout << "match result: " << "1. " <<team1.name << "\n" << "2. " << team2.name << endl;
    } else if (powerTeam2 > powerTeam1) {
        team2.wins++;
        team1.losses++;
        team2.money += 1000;
        //cout << "match result: " << "1. " <<team2.name << "\n" << "2. " << team1.name << endl;
    } else {
        team1.draws++;
        team2.draws++;
    }
}

void rankk() {
    sort(teams.begin(), teams.end(), [](const Team &a, const Team &b) {
        if (a.wins != b.wins)
            return a.wins > b.wins;
        return a.losses < b.losses;
    });

    for (int i = 0; i < teams.size(); ++i) {
        cout << i + 1 << ". " << teams[i].name << endl;
    }
}

int main() {
    string line;
    while (true) {
        getline(cin, line);
        stringstream ss(line);
        string command;
        ss >> command;
        //cout << command << endl;

        if (command == "new") {
            string type, name;
            int money, price, speed, finishing, defense, playerID, teamID;
            ss >> type;
            if (type == "player") {
                ss >> name >> price >> speed >> finishing >> defense;
                newPlayer(name, price, speed, finishing, defense);
            } else if (type == "team") {
                ss >> name >> money;
                newTeam(name, money);
            }
        } else if (command == "buy") {
            int playerID, teamID;
            ss >> playerID >> teamID;
            buyPlayer(playerID, teamID);
        } else if (command == "match") {
            int teamID1, teamID2;
            ss >> teamID1 >> teamID2;
            match(teamID1, teamID2);
        } else if (command == "show_players") {
            printAllPlayers();
        } else if (command == "show_teams") {
            printAllTeams();
        } else if (command == "rank") {
            rankk();
        } else if (command == "end") {
            break;
        }
    }

    return 0;
}
