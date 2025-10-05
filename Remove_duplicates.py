def remove_duplicate(arr):      
    arr.sort()
    res=[]
    n=len(arr)
    for i in range(n-1):
        if arr[i]!=arr[i+1]:
            res.append(arr[i])
    res.append(arr[-1])
    return res

if __name__ == "__main__":
    arr = list(map(int, input("Enter elements: ").split()))
    print("After removing duplicates:", remove_duplicate(arr))

