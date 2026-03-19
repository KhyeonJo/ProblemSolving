def div(a, b, c):
    if b==1:
        return a%c

    X = div(a, b//2, c)
    
    if b%2==0:
        return X*X%c
    else:
        return X*X*a%c









import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())

print(div(a, b, c))