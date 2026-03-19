N = int(input())

L = []

for i in range(N):
    L.append(list(map(int, input().split())))

A = []
min = 2000000

def dfs(num):
    if len(A)==N//2:
        global min
        tot_A = 0
        tot_B = 0
        
        for i in A:
            for j in A:
                tot_A += L[i-1][j-1]
        B = []
        for i in range(1, N+1):
            if i not in A:
                B.append(i)
        for i in B:
            for j in B:
                tot_B += L[i-1][j-1]
        diff = abs(tot_A - tot_B)        
        
        if diff<min:
            min = diff
        return
        
    for i in range(num+1, N+1):
        A.append(i)
        dfs(i)
        A.pop()



dfs(1)

print(min)