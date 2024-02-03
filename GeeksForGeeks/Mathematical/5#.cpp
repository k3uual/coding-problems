#include<iostream>
#include<vector>

class Solution{
	public:
	int closestNumber(int N , int M) {
        //here we will take eg(test case) of N=-15 and M=6
        int flag=0;
        if(M<0)     //6 is greater than 0
            M=-M;   //won't execute cause condition false
        if(N<0){    //-15 less than 0
            N=-N;   //will execute and convert N=15
            flag=1; //set flag cause negative no.
        }
        
        int first = N-(N%M);    //15-(15%6)=15-3=12("12" is multiple of 6)
        int sec = first+M;      //M will be next multiple of 6(12+6="18")
        //here sec-N is written to produce positive result, instead of N-sec
        if(N-first < sec-N)     //this won't execute cause both values are equal
        {
            if(flag == 1)
                return -first;  //return negative cause 15 was originally -15
            else
                return first;   //return positive
        }
        //this will execute when second multiple is less than or "equal" to first one
        else{
            if(flag==1)
                return -sec;    //this is the value which will be returned as "-12"
            else    
                return sec;     //flag was set so this won't be executed
        }
    }
};

int main(){
    Solution s;
    std::cout<<s.closestNumber(-15,6); 
}