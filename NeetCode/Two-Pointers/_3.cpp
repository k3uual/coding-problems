#include<iostream>
#include<vector>
#include<unordered_map>
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> sol;
        set<vector<int>> s;
        int count = 0;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        
        for(int i = 0; i < n; i++) {
            int j = i + 1;
            int k = n - 1;

            while(j < k) {
                int sum = nums[i] + nums[k] + nums[j];

                if(sum == 0) {
                    s.insert({nums[i], nums[j], nums[k]});
                    count++;
                    j++;
                    k--;
                }
                else if(sum < 0) {
                    j++;
                }
                else {
                    k--;
                }
            } 
        }
        for(auto triplets : s)
                sol.push_back(triplets);
            return sol;
    }
};

int main() {
    Solution s;
    vector<int> num = {0,1,1};
    vector<vector<int>> sol = s.threeSum(num);
    
    for(int i = 0; i < sol.size(); i++) {
        for(int j = i+1; j < 3; i++) {
            cout << sol[i][j] << "  ";
        }
        cout << "----" << endl;
    }
}