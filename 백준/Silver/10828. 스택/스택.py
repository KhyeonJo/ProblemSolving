import sys

N = int(sys.stdin.readline())
L = []

for i in range(N):
    now = sys.stdin.readline().strip()
    if now.startswith('pu'):
        A, B = now.split()
        L.append(B)
    elif now =='pop':
        if len(L)==0:
            print(-1)
        else:
            print(L.pop())
    elif now =='size':
        print(len(L))
    elif now =='empty':
        print(int(len(L)==0))
    elif now =='top':
        if len(L)==0:
            print(-1)
        else:
            print(L[-1])