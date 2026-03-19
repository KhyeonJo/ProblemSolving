import sys

M, N = map(int, sys.stdin.readline().split())
answer = M*N
L = []
answers = []

for i in range(M):
    L.append(sys.stdin.readline().strip())

for i in range(M-7):
    for j in range(N-7):
        white_inx = 0
        black_inx = 0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b) % 2 == 0:
                    if L[a][b]=='W':
                        white_inx +=1
                    else:
                        black_inx +=1
                if (a+b) % 2 == 1:
                    if L[a][b]=='B':
                        white_inx +=1
                    else:
                        black_inx +=1
        answers.append(min(white_inx, black_inx))

print(min(answers))