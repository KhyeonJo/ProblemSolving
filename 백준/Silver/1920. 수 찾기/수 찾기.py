import sys


input = sys.stdin.readline

N = int(input())
N_A = list(map(int, input().split()))
N_A.sort()
M = int(input())
M_A = list(map(int, input().split()))

for m in M_A:
    end   = N-1
    start = 0
    is_exist = 0
    chk_list = N_A    #chk_list가 계산하는 list.
    while start <= end:
        mid = (start+end)//2
        mid_val = chk_list[mid]
        if mid_val < m:
            start = mid + 1
        elif mid_val > m:
            end = mid-1
        else:
            is_exist = 1
            break
    print(is_exist)