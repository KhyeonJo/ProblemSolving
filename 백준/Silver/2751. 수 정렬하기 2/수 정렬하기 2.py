import sys
input = sys.stdin.readline

N = int(input())
L = [int(input()) for i in range(N)]


#merge_sort는 merge or arr를 리턴함.
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

# 두 개의 정렬된 배열을 합치는 함수
def merge(left, right):
    result = []
    i = j = 0

    # 여기서 두 배열을 비교하면서 result에 작은 값부터 추가
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1

    # 남아있는 값 처리
    while i < len(left):
        result.append(left[i])
        i +=1

    while j < len(right):
        result.append(right[j])
        j +=1

    return result

for i in merge_sort(L):
    print(i)