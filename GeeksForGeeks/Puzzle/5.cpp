using namespace std;
#include<iostream>
#include<math.h>

class Solution{   
public:
    int doOverlap(int L1[], int R1[], int L2[], int R2[]) {
        // code here
        // int a1=l1[0];//top left of first
        // int b1=l1[1];
        
        // int c1=r1[0];// bottom right of first
        // int d1=r1[1];
        
        // int a2=l2[0];//top left of second
        // int b2=l2[1];
        
        // int c2=r2[0];//bottom right of second
        // int d2=r2[1];
        
        if(R1[0]<L2[0] || R2[0]<L1[0] || R2[1]>L1[1] || R1[1]>L2[1]) return 0;
        return 1;
    }
};

int main(){
    Solution sol;
    int p[2]={-50,12};
    int q[2]={- 93,-16};
    int r[2]={-100,11};
    int s[2]={-16,-86};
    cout<<sol.doOverlap(p,q,r,s);
}