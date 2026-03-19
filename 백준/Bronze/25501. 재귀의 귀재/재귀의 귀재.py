def recursion(word, l, r):
    if l>=r:
        return (1, l+1)
    elif word[l]!=word[r]:
        return (0, l+1)
    else :
        return recursion(word, l+1, r-1) 

N = int(input())

for i in range(N):
    now = input()
    print(*recursion(now, 0, len(now)-1))