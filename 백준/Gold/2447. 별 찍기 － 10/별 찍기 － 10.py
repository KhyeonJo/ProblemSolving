def Star(n):
    if n==1:
        return ['*']
    else:
        Stars = Star(n//3)
        now = []
        for i in Stars: 
            now.append(i*3)   #n=9일때 Stars는 ['***', '* *', '***'] 여기서 각 값을 3배로 늘여서 저장. '*********', '* ** ** *', '*********' 이렇게
        for i in Stars:
            now.append(i+' '*(n//3)+i)
        for i in Stars:
            now.append(i*3)
    return now
    

N =int(input())
ls = Star(N)
for i in range(N):
    print(ls[i])