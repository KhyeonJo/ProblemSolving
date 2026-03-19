def cut(N, L):
    first = L[0][0]
    global plus, zero, minus
    if first ==-1: #first -1이면 나머지 나왔을 때 재귀
        for i in L:
            if 0 in i or 1 in i:
                top_left = [row[0:N//3] for row in L[0:N//3]]
                top_mid = [row[N//3:N//3*2] for row in L[0:N//3]]
                top_right = [row[N//3*2:N//3*3] for row in L[0:N//3]]
                mid_left = [row[0:N//3] for row in L[N//3:N//3*2]]
                mid_mid = [row[N//3:N//3*2] for row in L[N//3:N//3*2]]
                mid_right = [row[N//3*2:N//3*3] for row in L[N//3:N//3*2]]
                bot_left =  [row[0:N//3] for row in L[N//3*2:N//3*3]]
                bot_mid = [row[N//3:N//3*2] for row in L[N//3*2:N//3*3]]
                bot_right = [row[N//3*2:N//3*3] for row in L[N//3*2:N//3*3]]
                
                cut(N//3, top_left)
                cut(N//3, top_mid)
                cut(N//3, top_right)
                cut(N//3, mid_left)
                cut(N//3, mid_mid)
                cut(N//3, mid_right)
                cut(N//3, bot_left)
                cut(N//3, bot_mid)
                cut(N//3, bot_right)
                return
    elif first ==0: #first 0이면  나머지 나왔을 때 재귀
        for i in L:
            if -1 in i or 1 in i:
                top_left = [row[0:N//3] for row in L[0:N//3]]
                top_mid = [row[N//3:N//3*2] for row in L[0:N//3]]
                top_right = [row[N//3*2:N//3*3] for row in L[0:N//3]]
                mid_left = [row[0:N//3] for row in L[N//3:N//3*2]]
                mid_mid = [row[N//3:N//3*2] for row in L[N//3:N//3*2]]
                mid_right = [row[N//3*2:N//3*3] for row in L[N//3:N//3*2]]
                bot_left =  [row[0:N//3] for row in L[N//3*2:N//3*3]]
                bot_mid = [row[N//3:N//3*2] for row in L[N//3*2:N//3*3]]
                bot_right = [row[N//3*2:N//3*3] for row in L[N//3*2:N//3*3]]
                
                cut(N//3, top_left)
                cut(N//3, top_mid)
                cut(N//3, top_right)
                cut(N//3, mid_left)
                cut(N//3, mid_mid)
                cut(N//3, mid_right)
                cut(N//3, bot_left)
                cut(N//3, bot_mid)
                cut(N//3, bot_right)
                return
                return
    else: #first 1이면  나머지 나왔을 때 재귀
        for i in L:
            if -1 in i or 0 in i:
                top_left = [row[0:N//3] for row in L[0:N//3]]
                top_mid = [row[N//3:N//3*2] for row in L[0:N//3]]
                top_right = [row[N//3*2:N//3*3] for row in L[0:N//3]]
                mid_left = [row[0:N//3] for row in L[N//3:N//3*2]]
                mid_mid = [row[N//3:N//3*2] for row in L[N//3:N//3*2]]
                mid_right = [row[N//3*2:N//3*3] for row in L[N//3:N//3*2]]
                bot_left =  [row[0:N//3] for row in L[N//3*2:N//3*3]]
                bot_mid = [row[N//3:N//3*2] for row in L[N//3*2:N//3*3]]
                bot_right = [row[N//3*2:N//3*3] for row in L[N//3*2:N//3*3]]
                
                cut(N//3, top_left)
                cut(N//3, top_mid)
                cut(N//3, top_right)
                cut(N//3, mid_left)
                cut(N//3, mid_mid)
                cut(N//3, mid_right)
                cut(N//3, bot_left)
                cut(N//3, bot_mid)
                cut(N//3, bot_right)
                return
                return
    

    if first == -1:
        minus +=1
    elif first == 0:
        zero +=1
    else:
        plus +=1
    return

    
import sys

input = sys.stdin.readline
minus = 0
zero = 0
plus = 0

N = int(input())
L = []
for i in range(N):
    l = list(map(int, input().split()))
    L.append(l)

cut(N, L)

print(minus)
print(zero)
print(plus)