import sys

M, N = map(int, sys.stdin.readline().split())

def prime_count(x):
    if x == 1:
        return 0
    for i in range(2, round(x ** 0.5) + 1):
        if x%i==0:
            return 0
    print(x)

for i in range(M, N+1):
    prime_count(i)