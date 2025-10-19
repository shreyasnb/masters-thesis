import heapq

N = int(input().strip())
A = list(map(int, input().split()))
K = int(input().strip())

K = max(0, min(K, N))

if K == 0:
    print(0)
    print(' '.join('0' for _ in range(N)))
else:
    top_indices = set(heapq.nlargest(K, range(N), key=A.__getitem__))
    dist = sum(A[i] for i in top_indices)
    work = ['1' if i in top_indices else '0' for i in range(N)]
    print(dist)
    print(' '.join(work))
