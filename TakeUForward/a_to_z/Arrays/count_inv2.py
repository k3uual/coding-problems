
from typing import List
import math

cnt = 0
def merge(arr : List[int], low : int, mid : int, high : int) -> int:
    temp = []   # temporary array
    left = low  # starting index of left half of arr
    right = mid + 1 # starting index of right half of arr

    global cnt      # Modification 1: cnt variable to count the pairs

    # storing elements in the temporary array in a sorted manner
    while (left <= mid and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            cnt += (mid - left + 1)  # Modification 2
            right += 1

    # if elements on the left half are still left
    while (left <= mid):
        temp.append(arr[left])
        left += 1

    # if elements on the right half are still left
    while (right <= high):
        temp.append(arr[right])
        right += 1

    # transfering all elements from temporary to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]


def mergeSort(arr : List[int], low : int, high : int):
    if low >= high: return
    mid = (low + high) // 2
    mergeSort(arr, low, mid)    # left half
    mergeSort(arr, mid + 1, high)  # right half
    merge(arr, low, mid, high)  # merging sorted halves

def numberOfInversions(a : List[int], n : int) -> int:
    # Count the number of pairs:
    n = len(a)
    # Count the number of pairs:
    return mergeSort(a, 0, n - 1)

if __name__ == "__main__":
    a = [5,2,3,1,4,9]
    n = 5
    numberOfInversions(a, n)
    print("The number of inversions are:", cnt, a)


