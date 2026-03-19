import sys
N = int(sys.stdin.readline().strip())

L = [0]
pt = [0] * (N+1)

for i in range(N):
    L.append(int(sys.stdin.readline().strip()))

if N==1:
    print(L[1])
    sys.exit()

pt[1] = L[1]
pt[2] = L[1] + L[2] #pt[i]는 거기까지 가는 최고점수

for i in range(3, N+1):
    pt[i] = max(pt[i-2] + L[i], pt[i-3]+L[i-1]+L[i])

print(pt[N])
