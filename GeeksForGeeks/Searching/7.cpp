#include <bits/stdc++.h>
using namespace std;

class Solution{
    public:
    int search(int A[], int l, int h, int key){
        // l: The starting index
        // h: The ending index, you have to search the key in this range
        while(h-l>=0){
            if(A[l]==key)
                return l;
            if(A[h]==key)
                return h;
            l++;
            h--;
        }
        return -1;
        //complete the function here
    }
};
int main(){
    Solution s;
    int a[]={1,2,3,4,5,6,7};
    cout<<s.search(a,0,6,4);
}