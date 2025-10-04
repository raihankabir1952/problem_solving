def abc(arr):
    return arr[::2]  # alternate elements

if __name__=="__main__":
    arr = list(map(int, input("Enter array: ").split()))
    print(*abc(arr))
