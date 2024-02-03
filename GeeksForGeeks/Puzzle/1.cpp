using namespace std;
#include<iostream>

class Solution {
  public:
    int countSquares(int N) {
        // code here
        int sqr=0,count=0;
        //increment loop by 2 starting with 1 to get odd numbers
        for(int i=1;i<N;i=i+2){
            sqr+=i;/*adding the incrementing odd numbers with sqr will 
            result in getting next square number,sequence will be:1,4,9,16,25.....*/
            if(sqr>=N)
                break;
            count++;//count comes after checking condition, it is crucial to place it here
        }
        return(count);
    }
};

int main(){
    Solution s;
    cout<<s.countSquares(25);
}