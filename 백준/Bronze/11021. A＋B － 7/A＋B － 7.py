import sys

N = int(sys.stdin.readline())
a = 0
b = 0
for i in range(N):
    a,b = map(int, sys.stdin.readline().split())
    print(f'Case #{i+1}: {a+b}')