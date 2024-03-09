#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> prefixsum;
        //vector<int> result;
        for (int i = 0; i<nums.size(); i++){
            int X = target - nums[i];
            if(prefixsum.find(X) != prefixsum.end()){
                return{ prefixsum[X], i};
            }
            prefixsum[nums[i]] = i;
        }
        return{};
    }
};

int main(){
    Solution sol;
    vector<int> arr={3,6,2,4};
    vector<int> s=sol.twoSum(arr,6);
    for(int i=0;i<s.size();i++)
        cout<<s[i]<<", ";
}