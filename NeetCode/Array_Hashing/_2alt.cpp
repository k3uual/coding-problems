#include <iostream>
#include <string>
#include<unordered_map>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        int arr[26] = {0};
        int size = s.size();
        if(size != t.size()) {
            return false;
        }

        int i;
        for(i = 0; i < size; i++) {
            arr[s[i] - 97]++;
        }

        for(i = 0; i < size; i++) {
            arr[t[i] - 97]--;
            if(arr[t[i] - 97] < 0){
                return false;
            }
        }

        return true;
    }
};

int main(){
    Solution sol;
    cout << sol.isAnagram("anagram","gramana");
}