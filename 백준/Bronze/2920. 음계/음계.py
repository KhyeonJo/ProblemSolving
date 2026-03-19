L = list(map(int, input().split()))

if L == sorted(L):
    print("ascending")
elif L == sorted(L, reverse=True):
    print("descending")
else :
    print("mixed")