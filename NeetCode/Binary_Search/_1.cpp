#include<iostream>
#include<vector>
using namespace std;


class Solution {
public:
    int search(vector<int>& nums, int target) {
        int high = nums.size();
        int low = 0;
        
        while(low <= high) {
            int mid = (high + low)/2;
            
            if(nums[mid] == target)
                return mid;

            if(nums[mid] > target) {
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
        }
        return -1;
    }
};

int main() {
    Solution s;
    vector<int> nums = {-1,0,3,5,9,12};
    cout << s.search(nums, 9);
}