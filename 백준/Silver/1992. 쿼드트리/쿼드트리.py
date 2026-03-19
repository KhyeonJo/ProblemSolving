import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
L = []
for i in range(N):
    L.append(list(map(int, input().strip())))

def quad(N, L):
    if L[0][0] == 0:
        for l in L:
            if 1 in l:
                print('(', end='')
                quad(N//2, [row[:N//2] for row in L[:N//2]])
                quad(N//2, [row[N//2:] for row in L[:N//2]])
                quad(N//2, [row[:N//2] for row in L[N//2:]])
                quad(N//2, [row[N//2:] for row in L[N//2:]])
                print(')', end='')
                return
    else:
        for l in L:
            if 0 in l:
                print('(', end='')
                quad(N//2, [row[:N//2] for row in L[:N//2]])
                quad(N//2, [row[N//2:] for row in L[:N//2]])
                quad(N//2, [row[:N//2] for row in L[N//2:]])
                quad(N//2, [row[N//2:] for row in L[N//2:]])
                print(')', end='')
                return
                
    print(L[0][0], end = '')

quad(N, L)