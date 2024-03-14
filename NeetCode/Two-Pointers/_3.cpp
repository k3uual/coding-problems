#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> sol;
        int count = 0;
        int n = nums.size();
        
        // for(int i = 0; i < n; i++) {
        //     //cout << sum << endl;
        //     for(int j = 0; j < n; j++) {
        //         if(i == j)
        //             continue;
        //         int sum = nums[i] + nums[j] + nums[j+1];
        //         if(sum == 0){
        //             sol.push_back(std::vector<int>());
        //             sol[count].push_back(nums[i]);
        //             sol[count].push_back(nums[i + 1]);
        //             sol[count].push_back(nums[j]);
        //             cout << nums[i] << nums[i + 1] << nums[j] << endl;
        //             count++;
        //         }
        //     }
        // }
        unordered_map<int, int> map;
        for(int i = 0; i < nums.size(); i++) {
            map[nums[i]] = i;
        }

        for(int i = 0; i < nums.size() - 1; i=i+2) {
            int target = 0 - (nums[i] + nums[i+1]);
            cout << target << endl;
            if(map.at(target) != i) {
                sol.push_back(std::vector<int>());
                sol[count].push_back(nums[i]);
                sol[count].push_back(nums[i + 1]);
                sol[count].push_back(target);
                cout << nums[i] << nums[i + 1] << target << endl;
                count++;
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
        for(int j = i+1; j < 3; i++) {
            cout << sol[i][j] << "  ";
        }
        cout << "----" << endl;
    }
}