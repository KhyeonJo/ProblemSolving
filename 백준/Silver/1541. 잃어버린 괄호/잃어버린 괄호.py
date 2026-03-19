import sys

input = sys.stdin.readline

string = input().strip()

splt_string = string.split('-')

result = 0
for i in range(len(splt_string)):
    l = list(map(int, splt_string[i].split('+')))
    piece = sum(l)
    if i == 0:
        result += piece
    else:
        result -=piece

print(result)