#include<iostream>
#include<vector>

class Solution {
    public:
    int nthTermOfAP(int A1, int A2, int N) {
        int step=A2-A1;
        for(int i=1;i<N;i++){
            A1=A1+step;
        }
        return(A1);
    }
};

int main(){
    Solution num;
    std::cout<<num.nthTermOfAP(2,5,10);
}