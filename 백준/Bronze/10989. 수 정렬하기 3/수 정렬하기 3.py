import sys
input = sys.stdin.readline

N = int(input())
L = [0]*10001

for i in range(N):
    now = int(input())
    L[now] += 1
    
for num in range(10001):
    while L[num]!=0:
        print(num)
        L[num] -=1