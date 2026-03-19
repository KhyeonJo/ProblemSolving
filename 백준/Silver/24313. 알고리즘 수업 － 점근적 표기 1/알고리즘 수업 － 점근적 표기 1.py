import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline().strip())
n0 = int(sys.stdin.readline().strip())

n_chk = a1-c
_chk = -a0


if _chk >= n0*n_chk and c>=a1:
    print(1)
else:
    print(0)