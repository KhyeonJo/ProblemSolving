import sys

T = int(sys.stdin.readline())
L = []
for i in range(T):
    L.append(int(sys.stdin.readline()))

max_num = max(L)

nums = [True] * (max_num+1)
nums[0], nums[1] = False, False


for i in range(2, int(max_num**0.5)+1):
    if nums[i]:
        for j in range(i*i, max_num+1, i):
            nums[j] = False

primes = [x for x in range(2, max_num+1) if nums[x]]

for i in range(T): #숫자 N개 중 1개에 대해
    num = 0
    j=0
    dict={}
    target = L[i]
    
    while j < len(primes) and primes[j]<L[i]:
        p = primes[j]
        q = target - p
        
        if q in dict or p==q:
            num +=1
        else:
            dict[p] = q
        j+=1
      
    print(num)