#include <iostream>
#include<vector>

class Solution{
public:
    std::vector<int> getTable(int N)
    {
        std::vector<int> vec;
        for(int i=1;i<=10;i++){
            vec.push_back(i*N);
        }
        return(vec);
    }
};

int main(){
    Solution multiply;
    std::vector<int> sol;
    sol = multiply.getTable(5);
    for (int i = 0; i < sol.size(); i++) 
        std::cout << sol[i] <<" ";
}