def isSorted(arr):
    n = len(arr)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    return True

if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    if isSorted(arr):
        print("Array is Sorted")
    else:
        print("Array is Not Sorted")

