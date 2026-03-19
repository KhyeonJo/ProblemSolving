import sys

S = sys.stdin.readline().strip()
q = int(sys.stdin.readline().strip())

check = 0
lettersck = [0]*26

letterswtn = []

for i in S:
    lettersck[ord(i)-97] +=1
    A = lettersck[:]
    letterswtn.append(A)


for i in range(q):
    alpha, l, r = sys.stdin.readline().split()
    l = int(l)
    r = int(r)

    alpha = ord(alpha)-97

    end = letterswtn[r][alpha]
    start =letterswtn[l-1][alpha]

    if l==0:
        start = 0
    
    print(end - start)