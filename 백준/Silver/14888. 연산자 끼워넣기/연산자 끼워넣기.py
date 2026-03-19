N = int(input())
nums = list(map(int, input().split()))
L_equ = list(map(int, input().split()))

max = -1000000000
min = 1000000000

def dfs(total, num):
    if num==(len(nums)-1): #전부 다 계산했으면 total을 비교하고 넣기
        global max, min
        if total < min:
           min = total
        if total > max:
           max = total
        return

    for i in range(4): # 계산 중이면 계산하기
        if L_equ[i]!=0:
            L_equ[i] -=1
            pst_total = total
            if i == 0:
                total += nums[num+1]
            elif i == 1:
                total -= nums[num+1]
            elif i == 2:
                total *= nums[num+1]
            else:
                if total < 0:
                    total = (-1) * (total * (-1) // nums[num+1])
                else:
                    total = total // nums[num+1]
            dfs(total, num+1)
            L_equ[i] +=1
            total = pst_total

    
dfs(nums[0], 0)
print(max)
print(min)