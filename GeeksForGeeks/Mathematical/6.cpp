using namespace std;
#include<iostream>
#include<vector>
#include<string>
#include<math.h>
//

class Solution{
	public:
    string armstrongNumber(int n){
        //lets take 153 here
        int temp=n;
        int sum=0;
        while(temp>0){
            /*  here temp%10 will result in us fetching the last value and then 
            it will be raised to 3 using pow() function as in value^3, then using
            '+=' operator(one of various kinds of assignment opereator)
            sum will be added to the result and also assigned/overwritten on it
            eg of sum+=pow(temp%10,3) considering sum is initially 0 will be 27
            next iteration it will be sum+=125 => sum=152 next iteration it will 
            be 153(1+152)*/
            sum+=pow(temp%10,3);
            //cout<<sum<<"    "<<pow(temp%10,3)<<",";
            /*  here temp will be divided with 10 and also assigned to temp,
            eg temp/=153 will reult in 15 which will also be stored in temp */
            temp/=10;
            //temp<<",";
        }
        if(sum==n)
            return "Yes";
        cout<<"\n"<<sum;
        return "No";
    }//hope this helps
	
};

int main(){
    Solution s;
    std::cout<<s.armstrongNumber(153);
}

