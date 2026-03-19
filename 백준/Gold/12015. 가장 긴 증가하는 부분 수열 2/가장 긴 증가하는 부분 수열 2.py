import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))
arr = [0]

def BS(num):
    start, end = 0, len(arr)
    while start <= end:
        mid = (start + end)//2
        if num > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return start

for i in range(N):
    if arr[-1] < L[i]:
        arr.append(L[i])
    else:
        arr[BS(L[i])] = L[i]

print(len(arr)-1)