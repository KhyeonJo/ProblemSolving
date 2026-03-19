N = int(input())

for i in range(1, N+1):
    test_L = list(map(int, str(i)))
    test = i + sum(test_L)
    if test == N:
        print(i)
        break
    if N == i:
        print(0)