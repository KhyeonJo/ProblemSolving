import sys
input = sys.stdin.readline

res = []

def divide_and_conquer(histogram, start, end):
    if end == start:
        return histogram[end]
    elif end - start == 1:
        if histogram[end] < histogram[start]:
            return max(2*histogram[end], histogram[start])
        else:
            return max(2*histogram[start], histogram[end])
    
    mid = (start + end) // 2
    left_area = divide_and_conquer(histogram, start, mid)
    right_area = divide_and_conquer(histogram, mid+1, end)
    left = mid-1
    right = mid+1

    #분할해서 왼쪽area, 오른쪽area, 중간(mid)기준 좌우 확장하며 최대넓이 측정한 값 이렇게 3가지를 비교해야함.
    
    mid_area = histogram[mid]  #왼쪽area 계산
    now_height = histogram[mid] #오른쪽 area 계산
    
    while start <= left and right <= end: #중간(mid)기준 좌우로 더 큰 높이를 가진 쪽부터 확장하며 최대 넓이 계산. (mid area 계산 시작)
        if histogram[left] < histogram[right]:
            if histogram[right] < now_height:
                now_height = histogram[right]
            mid_area = max(mid_area, now_height * (right - left))
            right += 1
        else:
            if histogram[left] < now_height:
                now_height = histogram[left]
            mid_area = max(mid_area, now_height * (right - left))
            left -= 1
            
    while start <= left: #좌우 중 한쪽은 남았을테니 그 중 왼쪽을 계산해주는 while문 (mid area 계산중)
        if histogram[left] < now_height:
            now_height = histogram[left]
        mid_area = max(mid_area, now_height * (right - left))
        left -= 1
    while right <= end: #좌우 중 한쪽은 남았을테니 그 중 오른쪽을 계산해주는 while문 (mid area 계산중)
        if histogram[right] < now_height:
            now_height = histogram[right]
        mid_area = max(mid_area, now_height * (right - left))
        right += 1

    return max(left_area, right_area, mid_area) #비교할 때 재귀함수return값끼리 비교함. (D&C에서 자주 하는 일) 근데 여기선 예외로 mid area를 매번 직접 계산해야함.
        
            
        
res = []
while 1:
    histogram = list(map(int, input().split()))
    n = histogram[0]
    if n == 0:
        break
    
    res.append(divide_and_conquer(histogram, 1, n))

    
for i in res:
    print(i)