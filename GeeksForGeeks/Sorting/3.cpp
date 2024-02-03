#include <bits/stdc++.h>
using namespace std;

class Solution{
    public:
    void sort012(int a[], int n)
    {
        // code here 
        int no_0=0,no_1=0;
        //this loop will count the number of 0 and 1 in arr
        for(int i=0;i<n;i++){
            if(a[i]==0)
                no_0++;
            if(a[i]==1)
                no_1++;
        }
        /*this loop will overwrite all the elmeents
        with 1 and 0 and fill up rest with 2*/
        for(int i=0;i<n;i++){
            //here use of if-else if-else is necessary
            if(no_0>0){
                a[i]=0;
                no_0--;
            }
            else if(no_1>0){
                a[i]=1;
                no_1--;
            }
            else
                a[i]=2;
        }
    }
};
int main(){
    Solution s;
    int a[]={0,1,1,2,0,1,2,1,1,0,2,0};
    s.sort012(a,12);
    for(int i=0;i<12;i++)
        cout<<a[i]<<",";
}