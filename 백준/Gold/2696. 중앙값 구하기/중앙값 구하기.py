import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    M = int(input())
    L = []
    for j in range(M//10): #10넘으면 10개씩 잇기
        l = list(map(int, input().split()))
        L.extend(l)
    if M%10: #나머지 잇기
        l = list(map(int, input().split()))
        L.extend(l)

    start, end = 0, 0
    now_L = []
    print_L = []
    for j in range(M): #L에서 now_L로 옮기면서 계산
        now_L.append(L[j])
        if j%2==0: #홀수번째이면 (idx는 나머지0인걸로해야함.)
            now_L.sort()
            mid = (start+end)//2
            print_L.append(now_L[mid])
            end +=2
    print((M+1)//2)
    
    for j in range(0, len(print_L), 10): #10넘으면 10개씩 잇기
        print(*print_L[j:j+10])