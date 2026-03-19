import sys

N = int(sys.stdin.readline().strip())
dict = {}

for i in range(1,21):
    dict[i] = 0
    
for i in range(N):
    now = sys.stdin.readline().strip()
    if now[1] =='l':
        for j in range(1,21):
            dict[j] = j
    elif now[1] =='m':
        for j in range(1, 21):
            dict[j] = 0
    else:
        a, X = map(str, now.split())
        X = int(X)
        
        if now[1] =='d':
            dict[X] = X
        if now[1] =='e':
            dict[X] = 0
        if now[1] =='h':
            if dict[X]== X:
                print(1)
            else:
                print(0)
        if now[1] =='o':
            if dict[X]== X:
                dict[X] = 0
            else:
                dict[X] = X