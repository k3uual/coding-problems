#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int temp = target;
        int high = 0;
        
        if(numbers[0] < 0){
            temp = temp - numbers[0];
        }
        for(int i = 0; i < numbers.size(); i++){
            
            if(numbers[i] > temp){
                break;
            }
            high++;
        }
        high--;
        if(high < 2){
            ans.push_back(1);
            ans.push_back(2);
            return(ans);
        }

        int low = 0;
        
        while(low <= high) {
            int sum = numbers[low] + numbers[high];
            if(sum == target)
                return {low+1, high+1};
            
            else if(sum > target)
                high--;
            
            else
                low++;
        }
        
        return ans;
    }
};

int main(){
    Solution s;
    vector<int> num = {-10,-8,-2,1,2,5,6};
    //vector<int> num = {3,24,50,79,88,150,345};

    vector<int> ans = s.twoSum(num, 0);
    for(auto x: ans){
	cout<< x << "\n";
    }
    return 0;
}