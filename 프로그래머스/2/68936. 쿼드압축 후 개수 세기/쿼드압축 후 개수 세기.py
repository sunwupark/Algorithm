def solution(arr):
    answer = {0: 0, 1: 0}
    
    def find(size, x, y):
        if size == 1:
            answer[arr[x][y]]+=1
            return
        
        total = 0
        for nx in range(x, x+size):
            total += sum(arr[nx][y:y+size])
            
        if total == size*size:
            answer[1]+=1
        elif total == 0:
            answer[0]+=1
        else:
            find(size//2, x,y)
            find(size//2, x+size//2, y)
            find(size//2, x,y+size//2) 
            find(size//2, x+size//2, y+size//2)
    
    find(len(arr), 0, 0)
    return [answer[0], answer[1]]