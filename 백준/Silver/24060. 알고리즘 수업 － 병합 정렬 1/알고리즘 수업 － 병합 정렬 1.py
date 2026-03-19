def merge_sort(arr, p, r):
    if p<r:
        q = (p+r) //2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)




def merge(arr, p, q, r):
    global cnt, res
    save = []
    i = p
    j = q+1
    while i<=q and j<=r:
        if arr[i]<=arr[j]:
            save.append(arr[i])
            i +=1
        else:
            save.append(arr[j])
            j +=1
    while i<=q:
        save.append(arr[i])
        i +=1
    while j<=r:
        save.append(arr[j])
        j +=1
    for t in range(len(save)):
        arr[p+t] = save[t]
        cnt +=1
        if cnt == K:
            res = save[t]

cnt = 0
res = -1

N, K = map(int, input().split())
A = list(map(int, input().split()))

merge_sort(A, 0, N-1)

print(res)