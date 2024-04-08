#include <iostream>
#include <vector>
#include <string>
#include <bits/stdc++.h>
#define MAX 5
using namespace std;

int front = -1, rear = -1;

void enqueue(bool end, int val, int queue[])
{
   if (front == -1)
   {
      front = rear = 0;
   }
   if (end)
   {
      if (rear == MAX - 1)
      {
         cout << "rear is full" << endl;
         return;
      }
      rear++;
      queue[rear] = val;
   }
   else
   {
      if (front == 0)
      {
         cout << "front is full" << endl;
         return;
      }
      front--;
      queue[front];
   }
}

int dequeue(bool end, int queue[])
{
   if (front == -1)
   {
      cout << "underflow";
      return -1;
   }
   int x;
   if (end)
   {
      x = queue[rear];
      rear--;
   }
   else
   {
      x = queue[front];
      front++;
   }
   if (front > rear)
      front = rear = -1;
   return x;
}

void print(int queue[])
{
   for (int i = front; i <= rear; i++)
   {
      cout << queue[i] << "\t";
      cout << i;
   }
   cout << endl;
}

int main()
{
   int queue[MAX];
   int choice = 0;
   bool end;
   while (choice <= 3)
   {
      cout << "1.insert\n2.delete\n3.print\nenter choice: ";
      cin >> choice;

      if (choice <= 2)
      {
         cout << "0:front\n1:back\nenter end: ";
         cin >> end;
      }
      switch (choice)
      {

      case 1:
         int value;
         cout << "enter value: ";
         cin >> value;
         enqueue(end, value, queue);
         break;

      case 2:
         cout << dequeue(end, queue);
         break;

      case 3:
         print(queue);
         break;

      default:
         cout << "invalid choice";
         break;
      }
   }
   // dequeue(s);
}
