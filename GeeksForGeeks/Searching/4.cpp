#include <bits/stdc++.h>
using namespace std;

class Solution{
    public:
    int b_search(int a[],int lower,int upper,int k){
        int mid=(lower+upper)/2;
        
        if(lower>upper)
            return -1;
        if(a[mid]<k)
            return b_search(a,mid+1,upper,k);
        else if(a[mid]>k)
            return b_search(a,lower,mid-1,k);
        else
            return mid;
        
    }
    int binarysearch(int arr[], int n, int k) {
        // code here
        // int lower=0,upper=n-1,mid;
        // while(lower<=upper){
        //     mid=(lower+upper)/2;
        //     if(arr[mid]<k)
        //         lower=mid+1;
        //     else if(arr[mid]>k)
        //         upper=mid-1;
        //     else
        //         return mid;
        // }
        return b_search(arr,0,n-1,k);
    }
};
int main(){
    Solution s;
    int a[]={1,2,3,4,5};
    cout<< s.binarysearch(a,5,4);
}