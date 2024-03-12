#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> sol;
        int count = 0;
        int n = nums.size();
        
        for(int i = 0; i < n; i++) {
            //cout << sum << endl;
            for(int j = 0; j < n; j++) {
                if(i == j)
                    continue;
                int sum = nums[i] + nums[j] + nums[j+1];
                if(sum == 0){
                    sol.push_back(std::vector<int>());
                    sol[count].push_back(nums[i]);
                    sol[count].push_back(nums[i + 1]);
                    sol[count].push_back(nums[j]);
                    cout << nums[i] << nums[i + 1] << nums[j] << endl;
                    count++;
                }
            }
        }
        return sol;
    }
};

int main() {
    Solution s;
    vector<int> num = {-1,0,1,2,-1,-4};
    vector<vector<int>> sol = s.threeSum(num);
    
    for(int i = 0; i < sol.size(); i++) {
        for(int j = i+1; j < sol[i].size(); i++) {
            cout << sol[i][j] << endl;
        }
        cout << "----" << endl;
    }
}