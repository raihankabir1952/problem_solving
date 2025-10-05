'''
[1,2,3]
for i in range(3):
when i=0
for j in range(i,3):
for,i=0
j=0
arr[0:1]=1
j=1
arr[0:2]=1,2
j=2
arr[0:3]=1,2,3
for i=1

'''



def generate_subarrays(arr):
    sub=[]
    n=len(arr)
    for i in range(n):
        for j in range(i,n):
            sub.append(arr[i:j+1])
    return sub
print(" ")
if __name__ == "__main__":
    arr = list(map(int, input("Enter elements: ").split()))
    print(generate_subarrays(arr))