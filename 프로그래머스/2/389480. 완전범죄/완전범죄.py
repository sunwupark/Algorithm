def solution(info, n, m):
    answer = 0
    current = set([(0,0)])
    for x,y in info:
        adding = set()
        for tempx, tempy in current:
            if tempx+x < n:
                adding.add((tempx+x, tempy))
            if tempy+y < m:
                adding.add((tempx, tempy+y))
            
        if adding:
            current = adding
        else:
            return -1
    current = list(current)
    current.sort(key=lambda x: x[0])
    return current[0][0]
                