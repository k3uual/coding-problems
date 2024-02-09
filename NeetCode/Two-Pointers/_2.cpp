#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int sum;
        vector<int> ans;
        for(int i = 0;i < numbers.size(); i++){
            for(int j = i+1; j < numbers.size(); j++){
                sum = numbers[i] + numbers[j];
                if(sum > target){
                    break;
                if(sum == target){
                    ans.push_back(i+1);
                    ans.push_back(j+1);
                    return(ans);
                }
            }
        }
        return ans;
    }
};

int main(){
    Solution s;
    vector<int> num = {3,24,50,79,88,150,345};
    vector<int> ans = s.twoSum(num, 200);
    for(auto x: ans){
	cout<< x << "\n";
    }
}