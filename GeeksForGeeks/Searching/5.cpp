#include <bits/stdc++.h>
using namespace std;

class Solution{
    public:
    // Function to find floor of x
    // n: size of vector
    // x: element whose floor is to find
    int findFloor(vector<long long> v, long long n, long long x){
        // Your code here
        long long large=-1;
        for(int i=0;i<n && v[i]<=x;i++)
            large=i;
        
        return large;
    }
};
int main(){
    Solution s;
    vector<long long> a={10,20,30,40,50,60};
    cout<<s.findFloor(a,6,55);
}