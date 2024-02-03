using namespace std;
#include<iostream>
#include<math.h>

class Solution{   
public:
    int isPowerOfAnother(long long X, long long Y){
        for(int i=0;i<=Y;i++)
            if(pow(X,i)==Y)
                return 1;
        return 0;
    }
};

int main(){
    Solution s;
    cout<<s.isPowerOfAnother(100,1);
}