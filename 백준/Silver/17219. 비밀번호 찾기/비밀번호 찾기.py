import sys

N, M = map(int, sys.stdin.readline().split())
urls = {}

for i in range(N):
    url, pw = map(str, sys.stdin.readline().split())
    urls[url] = pw

for i in range(M):
    url = sys.stdin.readline().strip()
    print(urls[url])