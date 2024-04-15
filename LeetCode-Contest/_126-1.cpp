#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int sumOfEncryptedInt(vector<int>& nums) {
        int sum = 0;
        for(int i = 0; i < nums.size(); i++) {
            int max = nums[i] % 10;
            int temp = nums[i];
            int count = 0;
            while(temp != 0) {
                int digit = temp % 10;
                temp /= 10;
                if(digit > max)
                    max = digit;
                count++;
            }
            nums[i] = max;
            while(count > 1) {
                nums[i] = (nums[i] * 10) + max;
                count--;
            }
        }
        for(int i = 0; i < nums.size(); i++) {
            sum += nums[i];
        }
        return sum;
    }
};

int main() {
    vector<int> num = {10,21,31};
    Solution s;
    cout << s.sumOfEncryptedInt(num);
    
}
