import sys
from collections import Counter
import math

input = sys.stdin.readline

N, M = map(int, input().split())


A = list(map(int, input().split()))

sum = []
k = 0

for i in A:
    sum.append(i+k)
    k = i+k

div = []

for i in sum:
    div.append(i%M)

cnt = Counter(div)

result = cnt[0]

a= 0
while a<=M:
    result += math.comb(cnt[a], 2)
    a +=1

print(result)