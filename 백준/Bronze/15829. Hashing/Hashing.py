N = int(input())

L = list(map(ord, input()))
L = [x-96 for x in L]

def ar(n, i):
    ans = (n * (31 **i))
    return ans

H = 0

for i in range(len(L)):
    H = H + ar(L[i], i)

print(H % 1234567891)