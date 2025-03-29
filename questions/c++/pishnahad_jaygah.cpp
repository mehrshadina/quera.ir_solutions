#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

struct Tag {
    string name;
    int id;
};

struct Advertisement {
    string name;
    int cpc;
    vector<string> tags;
    int id;
};

struct Place {
    string name;
    int cpc;
    vector<string> tags;
    int id;
};

class AdSystem {
    map<string, Tag> tags;
    vector<Advertisement> ads;
    vector<Place> places;
    map<string, int> tagIdMap;
    map<string, int> adIdMap;
    map<string, int> placeIdMap;
    int tagCounter = 1;
    int adCounter = 1;
    int placeCounter = 1;

public:
    void addTag(string name) {
        if (tagIdMap.find(name) != tagIdMap.end()) {
            cout << "Error: Tag already exists" << endl;
        } else {
            Tag tag = { name, tagCounter };
            tags[name] = tag;
            tagIdMap[name] = tagCounter++;
            cout << "Done: Tag id is " << tags[name].id << endl;
        }
    }

    void listTags() {
        cout << "TAGs:";
        for (const auto& tag : tags) {
            cout << " " << tag.second.name;
        }
        cout << endl;
    }

    void addAdvertisement(string name, int cpc, vector<string> tags) {
        if (adIdMap.find(name) != adIdMap.end()) {
            cout << "Error: Ad already exists" << endl;
            return;
        }
        for (const string& tag : tags) {
            if (tagIdMap.find(tag) == tagIdMap.end()) {
                cout << "Error: Tag not found" << endl;
                return;
            }
        }
        Advertisement ad = { name, cpc, tags, adCounter };
        ads.push_back(ad);
        adIdMap[name] = adCounter++;
        cout << "Done: Ads id is " << ad.id << endl;
    }

    void listAds() {
        cout << "ADSs:";
        for (const auto& ad : ads) {
            cout << " " << ad.name;
        }
        cout << endl;
    }

    void addPlace(string name, int cpc, vector<string> tags) {
        if (placeIdMap.find(name) != placeIdMap.end()) {
            cout << "Error: Place already exists" << endl;
            return;
        }
        for (const string& tag : tags) {
            if (tagIdMap.find(tag) == tagIdMap.end()) {
                cout << "Error: Tag not found" << endl;
                return;
            }
        }
        Place place = { name, cpc, tags, placeCounter };
        places.push_back(place);
        placeIdMap[name] = placeCounter++;
        cout << "Done: Place id is " << place.id << endl;
    }

    void listPlaces() {
        cout << "PLACEs:";
        for (const auto& place : places) {
            cout << " " << place.name;
        }
        cout << endl;
    }

    void suggestAds(int placeId) {
        if (placeId <= 0 || placeId > places.size()) {
            cout << "Error: Place not found" << endl;
            return;
        }
        Place& place = places[placeId - 1];
        vector<pair<int, int>> scores;
        for (const auto& ad : ads) {
            int matchedTags = 0;
            int unmatchedTags = 0;
            for (const string& tag : ad.tags) {
                if (find(place.tags.begin(), place.tags.end(), tag) != place.tags.end()) {
                    matchedTags++;
                } else {
                    unmatchedTags++;
                }
            }
            int score = (max(1, ad.cpc - place.cpc)) * (matchedTags - unmatchedTags);
            scores.push_back({ score, ad.id });
        }
        sort(scores.rbegin(), scores.rend(), [](const pair<int, int>& a, const pair<int, int>& b) {
            if (a.first != b.first) return a.first > b.first;
            return a.second < b.second;
        });
        cout << "SUGGEST-ADS:";
        for (const auto& score : scores) {
            cout << " " << score.second;
        }
        cout << endl;
    }

    void suggestPlaces(int adId) {
        if (adId <= 0 || adId > ads.size()) {
            cout << "Error: Ads not found" << endl;
            return;
        }
        Advertisement& ad = ads[adId - 1];
        vector<pair<int, int>> scores;
        for (const auto& place : places) {
            int matchedTags = 0;
            int unmatchedTags = 0;
            for (const string& tag : place.tags) {
                if (find(ad.tags.begin(), ad.tags.end(), tag) != ad.tags.end()) {
                    matchedTags++;
                } else {
                    unmatchedTags++;
                }
            }
            int score = (max(1, place.cpc - ad.cpc)) * (matchedTags - unmatchedTags);
            scores.push_back({ score, place.id });
        }
        sort(scores.rbegin(), scores.rend(), [](const pair<int, int>& a, const pair<int, int>& b) {
            if (a.first != b.first) return a.first > b.first;
            return a.second < b.second;
        });
        cout << "SUGGEST-PLACE:";
        for (const auto& score : scores) {
            cout << " " << score.second;
        }
        cout << endl;
    }

    void matchAdToPlace(int adId, int placeId) {
        if (adId <= 0 || adId > ads.size()) {
            cout << "Error: Ads not found" << endl;
            return;
        }
        if (placeId <= 0 || placeId > places.size()) {
            cout << "Error: Place not found" << endl;
            return;
        }
        cout << "Done: " << adId << " matched to " << placeId << endl;
        ads.erase(remove_if(ads.begin(), ads.end(), [adId](const Advertisement& ad) { return ad.id == adId; }), ads.end());
        places.erase(remove_if(places.begin(), places.end(), [placeId](const Place& place) { return place.id == placeId; }), places.end());
    }
};

int main() {
    int n;
    cin >> n;
    cin.ignore();
    AdSystem adSystem;
    for (int i = 0; i < n; ++i) {
        string input;
        getline(cin, input);
        stringstream ss(input);
        string command;
        ss >> command;
        if (command == "ADD-TAG") {
            string name;
            ss >> name >> name;
            adSystem.addTag(name);
        } else if (command == "TAG-LIST") {
            adSystem.listTags();
        } else if (command == "ADD-ADS") {
            string name, tmp;
            int cpc;
            ss >> name >> name >> tmp >> cpc >> tmp;
            vector<string> tags;
            string tag;
            while (ss >> tag) {
                tags.push_back(tag);
            }
            adSystem.addAdvertisement(name, cpc, tags);
        } else if (command == "ADS-LIST") {
            adSystem.listAds();
        } else if (command == "ADD-PLACE") {
            string name, tmp;
            int cpc;
            ss >> name >> name >> tmp >> cpc >> tmp;
            vector<string> tags;
            string tag;
            while (ss >> tag) {
                tags.push_back(tag);
            }
            adSystem.addPlace(name, cpc, tags);
        } else if (command == "PLACE-LIST") {
            adSystem.listPlaces();
        } else if (command == "SUGGEST-ADS") {
            string tmp;
            int id;
            ss >> tmp >> id;
            adSystem.suggestAds(id);
        } else if (command == "SUGGEST-PLACE") {
            string tmp;
            int id;
            ss >> tmp >> id;
            adSystem.suggestPlaces(id);
        } else if (command == "MATCH") {
            string tmp;
            int adId, placeId;
            ss >> tmp >> tmp >> adId >> tmp >> placeId;
            adSystem.matchAdToPlace(adId, placeId);
        }
    }
    return 0;
}
