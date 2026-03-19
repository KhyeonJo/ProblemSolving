MOD = 1000000007
import sys
input = sys.stdin.readline

N = int(input())


def bi_mat(A, n):
    result = ((1,0), (0,1))
    while n > 0:
        if n & 1:
            result = matmul(result, A)
        A = matmul(A, A)
        n >>=1
    return result

def matmul(A, B):
    return [[(A[0][0]*B[0][0]+A[0][1]*B[1][0]) % MOD, (A[0][0]*B[0][1]+A[0][1]*B[1][1]) % MOD], [(A[1][0]*B[0][0]+A[1][1]*B[1][0]) % MOD, (A[1][0]*B[0][1]+A[1][1]*B[1][1]) % MOD]]

A = ((1,1),(1,0))
print(bi_mat(A, N-1)[0][0])