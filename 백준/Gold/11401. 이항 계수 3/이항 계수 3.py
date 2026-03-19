def fact(N, p):
    result = 1
    for i in range(2, N+1):
        result = result * i % p
    return result

def pow(val, times, p):
    if times ==1:
        return val
    elif times ==0:
        return 1
    X = pow(val, times//2, p)
    if times%2 == 0:
        return X * X % p
    else:
        return X * X * val % p

    

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
p = 1000000007

up = fact(N, p)
down = (fact(N-K, p) * fact(K, p)) % p

print(up * pow(down, p-2, p) % p)