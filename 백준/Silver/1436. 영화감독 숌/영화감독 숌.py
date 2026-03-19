N =int(input())

num = 666
cnt = 0
while 1:
    num_str = str(num)
    if "666" in num_str:
        cnt +=1
    if cnt == N:
        print(num)
        break
    num +=1
    