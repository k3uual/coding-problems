#include <iostream>
#include <vector>
using namespace std;

int total(int n, double a, double b)
{
   int total_amt;
   
   if (b / 2 < a) {
      total_amt = b * (n / 2);
      if(n % 2 != 0) {
         total_amt += a;
      }
   }
   else {
      return n * a;
   }
   return total_amt;
}

int main()
{
   int n = 5;
   double a = 5;
   double b = 11;

   cout << total(n, a, b);
}