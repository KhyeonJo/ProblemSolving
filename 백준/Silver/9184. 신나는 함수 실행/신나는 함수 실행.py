import sys
input = sys.stdin.readline
dp= [[[0]* 21 for _ in range(21)] for _ in range(21)]

def W(a, b, c):
    if a <= 0 or b<= 0 or c<=0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return W(20, 20, 20)
    elif dp[a][b][c]!=0: #이미 저장된 경우
        return dp[a][b][c]
    #저장 안되서 계산해야 하는 경우
    elif a<b and b<c:
        dp[a][b][c] = W(a, b, c-1) + W(a, b-1, c-1) - W(a, b-1, c)
    else:
        dp[a][b][c] = W(a-1, b, c) + W(a-1, b-1, c) + W(a-1, b, c-1) - W(a-1, b-1, c-1)
    return dp[a][b][c]

while 1:
    a, b, c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break

    ans = W(a, b, c)
       
    print('w(%d, %d, %d) = %d' % (a, b, c, ans))