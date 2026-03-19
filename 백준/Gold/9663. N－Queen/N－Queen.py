import sys

N = int(sys.stdin.readline().strip())


L = [] #체커보드
stack = []
total = 0

for i in range(N+1):
    L.append([0] * (N+1))
    
def dfs(num):
    if num == N+1:
        global total
        total += 1
        return
    for i in range(1, N+1):
        if L[num][i] == 0:
            stack.append((num, i))
            for a in range(1,N+1):
                L[a][i] += 1
            for a in range(1,N+1):
                if (num-a)>0 and (i-a)>0:
                    L[num-a][i-a] +=1
            for a in range(1,N+1):
                if (num+a)<=N and (i+a)<=N:
                    L[num+a][i+a] +=1
            for a in range(1,N+1):
                if (num+a)<=N and (i-a)>0:
                    L[num+a][i-a] +=1
            for a in range(1,N+1):
                if (num-a)>0 and (i+a)<=N:
                    L[num-a][i+a] +=1
            dfs(num+1)
            stack.pop()
            for a in range(1,N+1):
                L[a][i] -= 1
            for a in range(1,N+1):
                if (num-a)>0 and (i-a)>0:
                    L[num-a][i-a] -=1
            for a in range(1,N+1):
                if (num+a)<=N and (i+a)<=N:
                    L[num+a][i+a] -=1
            for a in range(1,N+1):
                if (num+a)<=N and (i-a)>0:
                    L[num+a][i-a] -=1
            for a in range(1,N+1):
                if (num-a)>0 and (i+a)<=N:
                    L[num-a][i+a] -=1    
dfs(1)
print(total)