#include <iostream>
#include <sstream>
#include <bitset>
#include <vector>
#include <string>

std::string calculateNetMask(int netLength) {
    std::string binary_netMask = "";
    for (int i = 0; i < 32; ++i) {
        if (i < netLength)
            binary_netMask += '1';
        
        else
            binary_netMask += '0';
    }

    std::string netMask = "";
    for (int i = 0; i < 4; ++i) {
        netMask += std::to_string(std::bitset<8>(binary_netMask.substr(i * 8, 8)).to_ulong());
        
        if (i < 3)
            netMask += '.';
    }
    
    std::cout << netMask << std::endl;

    return netMask;
}

std::string ipToBinary(const std::string& ip) {
    std::stringstream ss(ip);
    std::string token;
    std::string binary_ip = "";
    
    while (std::getline(ss, token, '.')) {
        int octet = std::stoi(token);
        binary_ip += std::bitset<8>(octet).to_string();
    }
    
    return binary_ip;
}

std::string calculateNetID(const std::string& ipBinary, int netLength) {
    std::string binary_netID = ipBinary.substr(0, netLength) + std::string(32 - netLength, '0');
    std::string netID = "";
    for (int i = 0; i < 4; ++i) {
        netID += std::to_string(std::bitset<8>(binary_netID.substr(i * 8, 8)).to_ulong());
        
        if (i < 3)
            netID += '.';
    }
    
    std::cout << netID << std::endl;

    return netID;
}

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
    
    std::cout << hostRangeStart + " - " + hostRangeEnd << std::endl;

    return hostRangeStart + " - " + hostRangeEnd;
}

std::string calculateBroadcast(const std::string& ipBinary, int netLength) {
    std::string binary_broadcast = ipBinary.substr(0, netLength) + std::string(32 - netLength, '1');
    std::string broadcast = "";
    for (int i = 0; i < 4; ++i) {
        broadcast += std::to_string(std::bitset<8>(binary_broadcast.substr(i * 8, 8)).to_ulong());
        
        if (i < 3)
            broadcast += '.';
    }
    
    std::cout << broadcast << std::endl;

    return broadcast;
}



int main() {
    std::string input;
    std::cin >> input;

    size_t pos = input.find('/');
    std::string ip = input.substr(0, pos);
    int netLength = std::stoi(input.substr(pos + 1));

    std::string ipBinary = ipToBinary(ip);
    calculateNetMask(netLength);
    std::string netID = calculateNetID(ipBinary, netLength);
    std::string broadcast = calculateBroadcast(ipBinary, netLength);
    calculateHostRange(netID, broadcast);

    return 0;
}
