#include<iostream>
#include<vector>
using namespace std;
class Solution{
    public:
    int func(int n, vector<int>& dp){
        if(n % 2 != 0)
            return 0;
        
        if(dp[n] != -1) return dp[n];
        if(n == 0) return 1; 
        
        int sum = 0;
        for(int i=2;i<=n;i++){
            cout<<sum<<"\n";
            sum += func(i-2, dp) * func(n-i, dp);
        }
        return dp[n] = sum;
    }
    int count(int N){
        vector<int> dp(N+1, -1);
        return func(N, dp);
    }
    
    int count_2(int N){
        
        vector<int> dp(N+1,0);
        dp[0]=1;
        for(int i=2;i<=N;i+=2)
        {
            int curr=0;
            for(int j=0;j<=N-2;j+=2)
            {
                cout<<curr<<"="<<dp[j]<<"in"<<j<<"\n";
                curr+=(dp[j]*dp[i-j-2]);
            }
            cout<<"ins"<<dp[i]<<"in"<<i<<"="<<curr<<"\n";
            dp[i]=curr;
        }
        return dp[N];
    }
};

int main(){
    Solution s;
    cout<<s.count_2(6);
}