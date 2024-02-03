#include <bits/stdc++.h>
using namespace std;

class Solution{
    public:
    int findNumberOfTriangles(int arr[], int n)
    {
        // code here
        sort(arr,arr+n);
        int ans = 0;
        for(int i = n-1; i >= 2; i--){
            int a = 0;
            int b = i - 1;
            while(b > a){
                if(arr[a]+arr[b] > arr[i]){
                    ans += (b-a);
                    b--;
                }
                else{
                    a++;
                }
            }
        }
        return ans;
    }
};
int main(){
    Solution s;
    int a[]={6,4,9,7,8};
    cout<<s.findNumberOfTriangles(a,5);
    
}