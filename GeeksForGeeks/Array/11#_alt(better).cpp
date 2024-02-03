#include <bits/stdc++.h>
using namespace std;

class Solution{
    public:
    int remove_duplicate(int a[],int n){
        // code here
        if (n == 0)
            return 0;
        int j = 0;
        for (int i = 1; i < n; i++) {
            if (a[j] != a[i]) {
                a[j + 1] = a[i];
                j++;
            }
        }
        return j + 1;
    }
};
int main(){
    Solution s;
    int a[]={1,1,1,2,2,2,2,3,3,4,5,5,5};
    int n=s.remove_duplicate(a,13);
    for(int i=0;i<n;i++)
        cout<<a[i]<<",";
}