
def rotateArray(arr: [], n: int) -> []:
    # Write your code from here.
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1];
    arr[i+1] = temp
    return arr

if __name__ == '__main__':
    print(rotateArray([1,2,3,4,5], 5))