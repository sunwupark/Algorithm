N, M = map(int, input().split())

num_list = set(list(map(int, input().split())))
num_list = sorted(num_list)
from collections import defaultdict
visited = defaultdict(bool)

def dfs(node, depth, value):
    if depth == M:
        if visited[value]==False:
            visited[value]=True
            print(value)
    else:
        for n in num_list:
            if node <= n:
                dfs(n, depth+1, value+" "+str(n))

for l in num_list:
    dfs(l, 1, str(l))

