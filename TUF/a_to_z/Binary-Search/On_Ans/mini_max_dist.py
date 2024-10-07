
def numberOfGasStationsRequired(dist, arr):
    n = len(arr)  # size of the array
    cnt = 0
    print("dist",dist)
    for i in range(1, n):
        numberInBetween = ((arr[i] - arr[i - 1]) / dist)
        print("numbet",numberInBetween)
        if (arr[i] - arr[i - 1]) == (dist * numberInBetween):
            numberInBetween -= 1
        cnt += numberInBetween
    print("cnt:",cnt)
    return cnt


def minimiseMaxDistance(arr, k):
    n = len(arr)  # size of the array
    low = 0
    high = 0

    # Find the maximum distance:
    for i in range(n - 1):
        high = max(high, arr[i + 1] - arr[i])

    # Apply Binary search:
    diff = 1e-6
    while high - low > diff:
        mid = (low + high) / 2.0
        cnt = numberOfGasStationsRequired(mid, arr)
        if cnt > k:
            low = mid
        else:
            high = mid

    return high


arr = [1, 7, 8, 9]
k = 2
ans = minimiseMaxDistance(arr, k)
print("The answer is:", ans)


