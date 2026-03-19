def sdk(ls, r, c, zeros):
    if zeros==0:
        return ls
        
    candi1 = []
    candi2 = []
    candi3 = []
    onetonine = list(range(1, 10))
    for i in range(r, 9):
        for j in range(c, 9):
            if ls[i][j]==0:
                row = ls[i]
                for a in onetonine:  #행에서 검사
                    if a not in row:
                        candi1.append(a)

                column = []
                for k in range(9):  #열 숫자를 모은 list생성
                    column.append(ls[k][j])
                for a in onetonine:  #열에서 검사
                    if a not in column:
                        candi2.append(a)

                nines = []  #9칸영역 모든 list생성
                row = i // 3
                col = j // 3
                for row_add in range(3):
                    for col_add in range(3):
                        nines.append(ls[row*3+row_add][col*3+col_add])
                for a in onetonine:   #9칸영역 검사
                    if a not in nines:
                        candi3.append(a)

                inter =list(set(candi1)&set(candi2)&set(candi3))

                if inter==[]:
                    return 0

                for decision in inter:
                    ls[i][j]=decision
                    if j==8:
                        ans = sdk(ls, i+1, 0, zeros-1)
                    else:
                        ans = sdk(ls, i, j+1, zeros-1)
                    if ans==0:
                        continue
                    return ans
                ls[i][j] = 0 #??
                return 0 #??
        c=0
    return ls #??
    

L = []
for i in range(9):
    L.append(list(map(int, input().split())))

zeros=0
for i in range(9):
    for j in range(9):
        if L[i][j]==0:
            zeros +=1

L = sdk(L, 0, 0, zeros)

for i in range(9):
    print(*L[i])