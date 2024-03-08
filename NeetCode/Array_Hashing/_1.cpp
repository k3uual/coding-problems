#include <iostream>
#include <vector>
#include <algorithm>
#include<unordered_map>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> track;
        for(int num : nums) {
            if(track[num] == 1) {
                return true;
            }
            track[num]++;
        }
        return false;
    }
};

int main(){
    Solution sol;
    vector<int> num={1,2,3,4,6,15,1};
    cout<<sol.containsDuplicate(num);
}