using namespace std;
#include<iostream>
#include<vector>

class Solution {
  public:
        void print(int ar[], int n){
        // code here
        for(int i=0;i<n;i=i+2)
            cout<<ar[i]<<" ";
    }
};

int main(){
    int ar[]={10,20,30,40,50};
    Solution s;
    s.print(ar,5);
}