import itertools
N, M = map(int, input().split())
for i in list(itertools.combinations(range(1, N+1), M)) : print(*i)
