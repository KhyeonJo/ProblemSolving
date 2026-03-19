N = int(input())
for i in range(N):
    times, word = input().split()
    L = list(map(ord, word))
    for j in range(len(L)):
        for k in range(int(times)):
            print(chr(L[j]), end="")
    print("")