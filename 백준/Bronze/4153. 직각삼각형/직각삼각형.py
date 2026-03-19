while 1:
    L = sorted(list(map(int, input().split())))
    if L[0]==L[1]==L[2]==0:
        break
    elif L[2]*L[2] == L[1]*L[1] + L[0]*L[0]:
        print("right")
    else:
        print("wrong")