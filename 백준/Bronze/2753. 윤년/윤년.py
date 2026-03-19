A = int(input())

if A%4==0:
    if (A%100)==0:
        if (A%400)==0:
            print('1')
        if (A%400)!=0:
            print('0')
    if (A%100)!=0:
        print('1')

if A%4!=0:
    print('0')