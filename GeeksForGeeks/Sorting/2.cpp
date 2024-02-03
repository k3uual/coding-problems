#include <bits/stdc++.h>
using namespace std;

class Solution{
    public:
    void binSort(int A[], int N)
    {
        //lets take eg {1 0 1 1 0}
        int j=0;   
        
        /*this loop will overwrite all the 
        elements with all the 0 we find in arr*/
        for(int i=0;i<N;i++)
            if(A[i]==0)
                A[j++]=0; //{0 0 1 1 0}
                
        //loop to overwrite rest of the elements with 1
        for(int i=j;i<N;i++)
            A[i]=1; //{0 0 1 1 1}
        
        //Hope this helps :)
    }
};
int main(){
    Solution s;
    int a[]={0,1,1,0,1,1,1,0};
    s.binSort(a,8);
    for(int i=0;i<8;i++)
        cout<<a[i]<<",";
}
