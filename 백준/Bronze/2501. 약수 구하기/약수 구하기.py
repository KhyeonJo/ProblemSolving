N, K = map(int, input().split())
cnt = 0

for i in range(N):
    if (N % (i+1))==0:
        cnt = cnt + 1
        if (cnt==K):
            print(i+1)
            break
if (cnt<K):
    print('0')