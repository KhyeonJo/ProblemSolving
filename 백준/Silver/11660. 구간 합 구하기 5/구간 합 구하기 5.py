import sys
input = sys.stdin.readline

N, M = map(int, input().split())

mat= []

for i in range(N):
    mat.append(list(map(int, input().split())))

#누적합계산
sum = []
for i in range(len(mat)):
    L = []
    if i > 0:
        prev = mat[i-1][0]
    else:
        prev = 0
    for j in range(len(mat[0])):
        All = mat[i][j]  #전체 중복 계산

        if j == 0:  #A합 계산
            plus1 = 0
        else: 
            plus1 = L[j-1]
            
        if i == 0:  #B합 계산
            plus2 = 0
        else:
             plus2 = sum[i-1][j]

        if i == 0 or j == 0: #intersect계산
            intersec = 0
        else:
            intersec = sum[i-1][j-1] 
        
        L.append(All + plus1 + plus2 - intersec)
        
    sum.append(L)


        

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    x1 -=1
    x2 -=1
    y1 -=1
    y2 -=1
    
    All = sum[x2][y2]
    minus1 = sum[x2][y1-1]
    minus2 = sum[x1-1][y2]
    intersec = sum[x1-1][y1-1]
    
    if y1==0:
        minus1 = 0
        intersec = 0
    if x1==0:
        minus2 = 0
        intersec = 0
    
    print(All - minus1 - minus2 + intersec)