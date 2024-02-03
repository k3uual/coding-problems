#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> freq;
        int j,flag;
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size();i=j){
            flag=1;
            for(j=i+1;j<nums.size() && nums[i]==nums[j];j++,flag++);
            if(flag>=k)
                freq.push_back(nums[i]);
        }
        return freq;
    }
};

int main(){
    Solution sol;
    vector<int> arr={1,1,1,2,2,3,5,5};
    vector<int> ans=sol.topKFrequent(arr,1);
    for(int i=0;i<ans.size();i++)
        cout<<ans[i]<<", ";
}