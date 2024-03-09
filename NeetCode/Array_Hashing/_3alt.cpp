#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            numMap[nums[i]] = i;
        }

        for (int i = 0; i < n; i++) {
            int complement = target - nums[i];

            if (numMap.count(complement) && numMap[complement] != i) {
                return {i, numMap[complement]};
            }
        }

        return {}; // No solution found
    }
};
int main(){
    Solution sol;
    vector<int> arr={3,2,4,6};
    vector<int> s=sol.twoSum(arr,6);
    for(int i=0;i<s.size();i++)
        cout<<s[i]<<", ";
}