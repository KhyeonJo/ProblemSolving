import queue
import sys
N = int(sys.stdin.readline())

queue = queue.Queue()

for i in range(1, N+1):
    queue.put(i)

for i in range(N-1):
    queue.get()
    queue.put(queue.get())

print(queue.get())