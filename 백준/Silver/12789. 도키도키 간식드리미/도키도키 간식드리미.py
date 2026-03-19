from collections import deque
import sys

N = int(sys.stdin.readline())
start = deque(map(int, sys.stdin.readline().split()))  # start는 큐처럼 사용
side = deque()  # side는 스택처럼 사용

num = 1  # 1부터 N까지 수를 순차적으로 출력해야 함

while start:
    # start에서 숫자를 하나씩 꺼내기
    now = start.popleft()

    # start에서 꺼낸 숫자가 num과 같으면 num을 증가
    if now == num:
        num += 1
    else:
        # side의 top이 num과 일치하지 않으면 side에 넣기
        if not side or side[-1] != num:
            side.append(now)
        else:
            # num과 일치하는 값이 side의 top이면 바로 pop하고 num 증가
            side.pop()
            num += 1
    
    # side에서 num과 일치하는 값이 있으면 바로 pop하고 num 증가
    while side and side[-1] == num:
        side.pop()
        num += 1

# num이 N+1이면 "Nice", 그렇지 않으면 "Sad"
if num == N + 1:
    print("Nice")
else:
    print("Sad")