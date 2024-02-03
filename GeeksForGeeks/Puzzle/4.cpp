using namespace std;
#include<iostream>

class Solution {
  public:
    int isPowerOfAnother(long long X, long long Y){
        // code here 
        if(X==1)
            return 0;
        if(Y==1)
            return 1;
        int i;
        for(i=1;i<Y;i=i*X);
        if(i==Y)
            return 1;
        return 0;
    }
};

int main(){
    Solution s;
    cout<<s.isPowerOfAnother(100,1);
}