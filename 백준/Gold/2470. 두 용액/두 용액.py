import sys

input = sys.stdin.readline


N = int(input())
L = list(map(int, input().split()))
min = 2000000000
L.sort()

start, end = 0, len(L)-1

while start<end:
    sum = L[start] + L[end]
    if abs(sum) < abs(min):
        min = sum
        A = L[start]
        B = L[end]
        if min<0:
            start +=1
        elif min>0:
            end -=1
        else:
            break
    else:
        if sum<0:
            start +=1
        elif sum>0:
            end -=1
        

print(A, B)