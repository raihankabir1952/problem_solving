'''def remove_duplicate(arr):
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

'''

def solution(arr):
    res = []
    count_zero = 0
    for num in arr:
        if num != 0:
            res.append(num)
        else:
            count_zero += 1
    # Add zeros at the end
    res.extend([0] * count_zero)
    return res

if __name__ == "__main__":
    arr = list(map(int, input("Enter elements: ").split()))
    print("After moving zeros:", solution(arr))


