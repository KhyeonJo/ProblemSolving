def Can(n):
    if n==0:
        print('-', end='')
    else:
        Can(n-1)
        print(' '*3**(n-1), end='')
        Can(n-1)

while 1:
    try:
        Can(int(input()))
        print('')
    except EOFError:
        break