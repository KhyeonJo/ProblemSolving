num = int(input())
max = -1000000
min = 1000000
L = list(map(int, input().split()))
for i in range(num):
	if L[i] < min:
		min = L[i]
	if L[i] > max:
		max = L[i]
print(min, max)