#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> sol;
        int temp;
        for(int i=0;i<nums.size();i++){
            temp=target-nums[i];
            for(int j=i+1;j<nums.size();j++){
                if(nums[j]==temp){
                    sol.push_back(i);
                    sol.push_back(j);
                    return sol;
                }
            }
        }
        return sol;
    }
};
int main(){
    Solution sol;
    vector<int> arr={3,2,4};
    vector<int> s=sol.twoSum(arr,6);
    for(int i=0;i<s.size();i++)
        cout<<s[i]<<", ";
}