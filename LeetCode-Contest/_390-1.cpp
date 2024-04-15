#include<iostream>
#include<string.h>
#include<unordered_map>
using namespace std;

class Solution {
public:
    int maximumLengthSubstring(string s) {
        unordered_map<char, int> map;
        int occured = 0;
        int max = 0;
        for(int i = 0; i < s.size(); i++) {
            if(i - map[s[i]] > max) {
                max = map[s[i]];
            }
            map[s[i]] = i;
            
        }
        return max;
    }
};

int main() {
    string s = "bcbbbcba";
    Solution sol;
    cout << sol.maximumLengthSubstring(s);
}