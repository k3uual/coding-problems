using namespace std;
#include<iostream>
#include<vector>
#include<math.h>

class Solution {
  public:
    vector<int> threeDivisors(vector<long long> query, int q)
    {
        int flag=0,counter=0;
        vector<int> ans;
        for(int n:query){
            for(int i=4;i<n;i++){
                for(int j=2;j<n;j++){
                    if(i%j==0){
                        flag++;
                        if(flag>2)
                            break;
                    }
                }
                if(flag==2)
                    counter++;
                flag=0;
            }
            ans.push_back(counter);
            counter=0;
        }
        return(ans);
    }
    vector<int> threeDivisors_2(vector<long long> query, int q){
        int counter=0;
        vector<int> ans;
        for(int n:query){
            for(int i=2;i<n;i++){
                
                if(i*i>n)
                    break;
                else
                    if(isprime(i)){
                        cout<<"'"<<i*i<<"'";
                        counter++;
                    }
            }
            ans.push_back(counter);
            counter=0;
        }
        return(ans);
    }
    bool isprime(int n){
        for(int i=2;i<=sqrt(n);i++)
            if(n%i==0)
                return false;
        return true;
    }
    
    vector<int> threeDivisors_3(vector<long long> query, int q){
        int counter=0;
        vector<int> ans;
        for(int n:query){
            for(int i=2;i*i<=n;i++){
                if(isprime(i)){
                    cout<<"'"<<i<<"'";
                    counter++;
                }
            }
            ans.push_back(counter);
            counter=0;
        }
        return(ans);
    }
    
};

int main(){
    Solution s;
    vector<long long> v={289};
    vector<int> sol=s.threeDivisors_2(v,2);
    for(int i:sol)
        cout<<i<<" ";
}