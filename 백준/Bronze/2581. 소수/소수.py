M = int(input())
N = int(input())

L = list(range(M, N+1))
res = []
for num in L:
    if num < 2:
        continue
    is_prime = True
    for check in range(2, int(num**(0.5))+1):
        if num%check == 0:
            is_prime = False
            break
    if is_prime:
        res.append(num)
        

if res == []:
    print(-1)
else:
    print(sum(res))
    print(res[0])