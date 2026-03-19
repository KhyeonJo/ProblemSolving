N = int(input())
cnt = 0
now = 1
while N >= now**2:
    if now**2 <= N:
        cnt+=1
    now +=1
print(cnt)