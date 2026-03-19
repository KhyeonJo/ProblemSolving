N = int(input())

for i in range(N):
    now = input()
    clt = []
    back = ''
    for j in range(len(now)):
        if j == 0:
            back = now[j]
        else:
            if back == now[j]:
                continue
            elif now[j] not in clt:
                clt.append(back)
                back = now[j]
            else:
                N -=1
                break

print(N)