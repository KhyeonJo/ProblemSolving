import sys

input = sys.stdin.readline


N = int(input())
L = list(map(int, input().split()))
x = int(input())
cnt = 0

L.sort()

start, end = 0, len(L)-1

while start<end:    
    if L[start]+L[end] < x:
        start +=1
    elif L[start]+L[end] > x:
        end -=1
    else:
        cnt +=1
        start +=1
        end -=1

print(cnt)
