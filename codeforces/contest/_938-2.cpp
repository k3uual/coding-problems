#include<iostream>
#include<vector>
using namespace std;

int sunk(int a[], int n, int k) {
   int sink = 0;
   int end = n-1;
   int front = 0;
   int hit_end = 0;
   for(int i = 1; i <= k; i++) {
      
      if(hit_end) {
         if(a[end] == 0) {
            end--;
            sink++;
         }
         cout << "hit " <<end;
         a[end]--;
         hit_end = 0;
      }
      else {
         if(a[front] == 0) {
            front++;
            sink++;
         }
         cout << "hit " << front;
         a[0]--;
         hit_end = 1;
      }
   }
   for(int i = 0; i < n; i++) {
      cout << a[i];
   }

   if(a[end] == 0)
      sink++;
   if(a[front] == 0)
      sink++;

   //int i = 0,j = n-1;
   // while(i <= j) {
   //    if(a[i] == 0) {
   //    }
   //    if(a[j] == 0) {
   //    }
   //    i++;
   //    j--;
   //    cout << a[i] << "--" << a[j];
   // }
   return sink;
}

int main() {
   int a[] = {1, 2, 4, 3};
   int k = 5;
   int n = 4;

   cout << sunk(a, n, k);
}