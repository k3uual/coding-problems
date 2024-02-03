using namespace std;
#include<iostream>
#include<math.h>

class Solution {
  public:
    public:
    //Function to rotate an array by d elements in counter-clockwise direction. 
    int getAngle(int H , int M) {
        // code here
        if (H == 12)
            H = 0;
        if (M == 60){
            M = 0;
            H = +1;
        }
        double hour = (H*60+M)*0.5;
        double min = M*6;
        
        double degree = (abs(hour-min));
        if(degree>180)
            degree = 360-degree;
        
        degree = (int)degree;
        return (int)degree;
    }
};

int main(){
    Solution s;
    cout<<s.getAngle(12,45);
    
}