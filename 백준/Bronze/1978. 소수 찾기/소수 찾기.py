N = int(input())
num = list(map(int, input().split()))
cnt = 0

def checker(n):
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count = count + 1
    if count ==2 :
        return 1
    return 0

for i in num:
    cnt = cnt + checker(i)

print(cnt)