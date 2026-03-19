import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))

add_L = []
now = 0
for i in range(N):
    if L[i]>=0:
        now +=L[i] 
        add_L.append(now)
    else:
        now +=L[i]
        add_L.append(now)
        if now<0:
            now = 0
print(max(add_L))