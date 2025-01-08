from collections import defaultdict

N = int(input())

files = defaultdict(int)
for i in range(N):
    files[input().split(".")[1]] += 1

for j in sorted(files):
    print(j + " " + str(files[j]))