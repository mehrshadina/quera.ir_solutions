#include <iostream>
#include <sstream>
#include <bitset>
#include <vector>
#include <string>

// Function to convert IP address to binary string
std::string ipToBinary(const std::string& ip) {
    std::stringstream ss(ip);
    std::string token;
    std::string binary = "";
    while (std::getline(ss, token, '.')) {
        int octet = std::stoi(token);
        binary += std::bitset<8>(octet).to_string();
    }
    return binary;
}

// Function to calculate net mask
std::string calculateNetMask(int netLength) {
    std::string netMaskBinary = "";
    for (int i = 0; i < 32; ++i) {
        if (i < netLength)
            netMaskBinary += '1';
        else
            netMaskBinary += '0';
    }

    std::string netMask = "";
    for (int i = 0; i < 4; ++i) {
        netMask += std::to_string(std::bitset<8>(netMaskBinary.substr(i * 8, 8)).to_ulong());
        if (i < 3)
            netMask += '.';
    }
    return netMask;
}

// Function to calculate net ID
std::string calculateNetID(const std::string& ipBinary, int netLength) {
    std::string netIDBinary = ipBinary.substr(0, netLength) + std::string(32 - netLength, '0');
    std::string netID = "";
    for (int i = 0; i < 4; ++i) {
        netID += std::to_string(std::bitset<8>(netIDBinary.substr(i * 8, 8)).to_ulong());
        if (i < 3)
            netID += '.';
    }
    return netID;
}

// Function to calculate broadcast address
std::string calculateBroadcast(const std::string& ipBinary, int netLength) {
    std::string broadcastBinary = ipBinary.substr(0, netLength) + std::string(32 - netLength, '1');
    std::string broadcast = "";
    for (int i = 0; i < 4; ++i) {
        broadcast += std::to_string(std::bitset<8>(broadcastBinary.substr(i * 8, 8)).to_ulong());
        if (i < 3)
            broadcast += '.';
    }
    return broadcast;
}

// Function to calculate host range address
std::string calculateHostRange(const std::string& netID, const std::string& broadcast) {
    std::vector<int> netIDParts;
    std::vector<int> broadcastParts;
    std::stringstream ss1(netID);
    std::stringstream ss2(broadcast);
    std::string token;
    while (std::getline(ss1, token, '.')) {
        netIDParts.push_back(std::stoi(token));
    }
    while (std::getline(ss2, token, '.')) {
        broadcastParts.push_back(std::stoi(token));
    }

    netIDParts[3]++;
    broadcastParts[3]--;
    std::string hostRangeStart = "";
    std::string hostRangeEnd = "";
    for (int i = 0; i < 4; ++i) {
        hostRangeStart += std::to_string(netIDParts[i]);
        hostRangeEnd += std::to_string(broadcastParts[i]);
        if (i < 3) {
            hostRangeStart += '.';
            hostRangeEnd += '.';
        }
    }
    return hostRangeStart + " - " + hostRangeEnd;
}

int main() {
    std::string input;
    std::cin >> input;

    // Splitting the input at '/'
    size_t pos = input.find('/');
    std::string ip = input.substr(0, pos);
    int netLength = std::stoi(input.substr(pos + 1));

    // Convert IP address to binary
    std::string ipBinary = ipToBinary(ip);

    // Calculate net mask
    std::string netMask = calculateNetMask(netLength);

    // Calculate net ID
    std::string netID = calculateNetID(ipBinary, netLength);

    // Calculate broadcast address
    std::string broadcast = calculateBroadcast(ipBinary, netLength);

    // Calculate host range address
    std::string hostRange = calculateHostRange(netID, broadcast);

    // Output results
    std::cout << netMask << std::endl;
    std::cout << netID << std::endl;
    std::cout << broadcast << std::endl;
    std::cout << hostRange << std::endl;

    return 0;
}
