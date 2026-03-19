from collections import deque
import sys
while 1:
    N = deque(sys.stdin.readline())
    if N[0] == '.':
        break
    big = 0
    sml = 0
    chL =[]

    while 1:
        now = N.popleft()
        if now =='[':
            chL.append(now)
        elif now =='(':
            chL.append(now)
        elif now ==']':
            if chL == []:
                print('no')
                break
            if chL.pop() !='[':
                print('no')
                break
        elif now ==')':
            if chL == []:
                print('no')
                break
            if chL.pop() !='(':
                print('no')
                break
        elif now =='.':
            if chL == []:
                print('yes')
                break
            else:
                print('no')
                break