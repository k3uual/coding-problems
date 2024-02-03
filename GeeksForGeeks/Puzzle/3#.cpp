using namespace std;
#include<iostream>
#include<string>

class Solution {
  public:
    string isSquare(int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4) {
        // code here
        int arr[4][2]={{x1,y1},{x2,y2},{x3,y3},{x4,y4}};
        int flag=0, pair=0,first=-99999,sec=-99999;
        for(int i=0;i<4;i++){
            if(arr[i][0]==arr[i][1])
                pair++;
            else{
                if(first!=-99999){
                    if(first==arr[i][1]&&sec==arr[i][0])
                        flag++;
                }
                first=arr[i][0];
                sec=arr[i][1];
            }
        }
        if(flag==1 && pair==2)
            return "Yes";
        return "No";
    }
};

int main(){
    Solution s;
    cout<<s.isSquare(20,10,10,20,20,20,10,10);
}