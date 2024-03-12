#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int high = matrix.size() - 1;
        int low = 0;
        int colMid;

        if(high == 0 && matrix[0].size() == 1) {
            if(matrix[0][0] == target)
                return true;
            else
                return false;
        }

        while(high >= low) {
            colMid = (high + low)/2;
            
            if(matrix[colMid][0] == target)
                return true;

            if(matrix[colMid][0] > target) {
                high = colMid - 1;
            }
            else {
                low = colMid + 1;
            }
        }

        colMid = high;
        high = matrix[colMid].size() - 1;
        low = 0;

        while(high >= low) {
            int rowMid = (high + low)/2;
            
            if(matrix[colMid][rowMid] == target)
                return true;

            if(matrix[colMid][rowMid] > target) {
                high = rowMid - 1;
            }
            else {
                low = rowMid + 1;
            }
        }

        return false;
    }
};
int main() {
    //vector<vector<int>> nums = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
    vector<vector<int>> nums = {{1},{1}};
    Solution s;

    cout << s.searchMatrix(nums, 0);
}