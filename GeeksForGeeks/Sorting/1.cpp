#include <bits/stdc++.h>
using namespace std;

class Solution{
    public:
    bool arraySortedOrNot(int arr[], int n) {
        // code here
        int i;
        for(i=0;i<n-1;i++)
            if(arr[i]>arr[i+1])
                break;
        if(i==n-1)
            return 1;
        return 0;
    }
};
int main(){
    Solution s;
    int a[]={1,2,2,2,4,5};
    cout<<s.arraySortedOrNot(a,6);
}