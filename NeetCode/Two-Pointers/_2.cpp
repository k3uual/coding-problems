#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
        vector<int> ans;
        int temp = target;
        int limit = 0;
        unsigned int i, j;

        if(numbers[0] < 0){
            temp = temp - numbers[0];
        }
        for(i = 0; i < numbers.size(); i++){
            
            if(numbers[i] > temp){
                break;
            }
            limit++;
        }
        limit--;
        if(limit < 2){
            ans.push_back(1);
            ans.push_back(2);
            return(ans);
        }
        
        for(i = 0; i < numbers.size(); i++){
            int find = target - numbers[i];
            for(j = limit; j > i; j--){
                if(numbers[j] < find)
                    break;
                
                if(numbers[j] == find){
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
    vector<int> num = {-10,-8,-2,1,2,5,6};
    //vector<int> num = {3,24,50,79,88,150,345};

    vector<int> ans = s.twoSum(num, 0);
    for(auto x: ans){
	cout<< x << "\n";
    }
    return 0;
}