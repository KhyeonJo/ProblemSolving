import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

def Z(N, start, end):
    global r, c
    mid = 2**(N-1)
    if r < mid:
        if c < mid:
            start = start
            end = start + 4**(N-1)-1
        else:
            start = start + 4**(N-1)
            end = start + 4**(N-1)-1
            c -= mid
    else:
        if c < mid:
            start = start + 4**(N-1)*2
            end = start + 4**(N-1)-1
            r -= mid
        else:
            start = start + 4**(N-1)*3
            end = start + 4**(N-1)-1
            c -= mid
            r -= mid
            
    if N == 1:
        return start
        
    else:
        return Z(N-1, start, end)


print(Z(N, 0, 4**(N)-1))