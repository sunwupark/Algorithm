def solution(dirs):
    answer = 0
    from collections import defaultdict
    visited = defaultdict(bool)
    x = y = 0
    for di in dirs:
        if di == "U" and x + 1 <= 5:
            visited[f"{x}{y}{x+1}{y}"] = True
            x += 1
        elif di == "D" and x - 1 >= -5:
            visited[f"{x-1}{y}{x}{y}"] = True
            x -=1 
        elif di == "L" and y - 1 >= -5:
            visited[f"{x}{y-1}{x}{y}"] = True
            y -=1 
        elif di == "R" and y +1 <= 5:
            visited[f"{x}{y}{x}{y+1}"] = True
            y +=1
        
    return len(visited.items())