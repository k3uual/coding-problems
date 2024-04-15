#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int minimumSubarrayLength(vector<int>& nums, int k) {
        int value;
        int sol = -1;
        int orResult = 0;
        for(int size = 0; size < nums.size(); size++) {

            for(int j = 0, k = size; k < nums.size(); j++, k++) {
                int tempSize = size;
                while(tempSize < 0) {
                    orResult += nums[j];
                    tempSize--;
                }
                cout << orResult << endl;
            }
            cout << "---";
        }
        
        
        if(value >= k){
            return sol;
        }
    }
};

int main() {
    vector<int> get = {1,2,3};

    Solution s;
    s.minimumSubarrayLength(get, 2);
}