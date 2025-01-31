comp_num = int(input())
connect_num = int(input())
connected_list = [[] for i in range(comp_num+1)]
visited_list = [False for i in range(comp_num+1)]
queue = []

for i in range(connect_num):
    a,b = map(int, input().split())
    connected_list[a].append(b)
    connected_list[b].append(a)

#print(connected_list)

def dfs(n):
    visited_list[n] = True
    for j in connected_list[n]:
        if visited_list[j] == False:
            queue.append(j)
    
    if len(queue)>0:
        num = queue.pop(0)
        #print(visited_list, num)
        dfs(num)

dfs(1)
print(visited_list.count(True)-1)