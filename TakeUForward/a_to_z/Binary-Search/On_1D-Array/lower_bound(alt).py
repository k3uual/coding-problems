def lowerBound(arr: [int], n: int, x: int) -> int:
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

if __name__ == "__main__":
    arr = [3,5,6,7,8,10,15,19,20]
    n = len(arr)
    x = 9
    ind = lowerBound(arr, n, x)
    print("The lower bound is the index:", ind)

