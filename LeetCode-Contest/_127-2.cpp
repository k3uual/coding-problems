#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

class Solution {
public:
    int minimumLevels(vector<int>& possible) {
        int dPlay = 1;
        
        int d, b;
        if(possible.size() == 2) {
            cout << "here";
            int sum;
            for(int i = 0; i < 2; i++) {
                sum += possible[i];
            }
            if(sum == 0)
                return -1;
        }
        while(dPlay <= possible.size()) {
            int dWin = 0, bWin = 0;

            for(d = 0; d < dPlay; d++) {
                if(possible[d])
                    dWin++;
                else   
                    dWin--;
                cout << "dWin" << dWin << endl;
            }
            
            for(b = d; b < possible.size(); b++) {
                cout << "pos:"<< possible[b];
                if(possible[b])
                    bWin++;
                else
                    bWin--;
                cout << "bWin" << bWin << endl;
            }

            if(dWin > bWin) return d;
            dPlay++;
        }
        return -1;
    }
};

int main() {
    vector<int> map = {0,1,1};

    Solution s;
    cout << s.minimumLevels(map);
}