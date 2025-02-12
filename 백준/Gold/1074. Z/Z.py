## 분할 후 칸을 채우면 된다
## 4등분으로 나눈다음 왼위, 오위, 왼아, 오아로 접근 하는 방식으로 가면된다
## 만약 한변의 길이가 2일때 하나씩 접근하면 된다

N, r, c = map(int, input().split())
count = 0

def dc(startx, starty, length):
    global count
    # print(startx, starty, length, count)

    if length == 1:
        if startx == r and starty == c:
            print(count)
            return
        else:
            count+=1
    else:
        nextLength = length//2
        if startx <= r < startx+nextLength and starty <= c < starty+nextLength:
            dc(startx, starty, nextLength)
        elif startx <= r < startx+nextLength and starty+nextLength <= c < starty+length:
            count += nextLength*nextLength
            dc(startx, starty+nextLength, nextLength)
        elif startx+nextLength <= r < startx +length and starty <= c< starty+nextLength:
            count += nextLength*nextLength*2
            dc(startx+nextLength, starty, nextLength)
        elif startx+nextLength <= r < startx +length and starty+nextLength <= c < starty+length:
            count += nextLength*nextLength*3
            dc(startx+nextLength, starty+nextLength, nextLength)

dc(0,0,2**N)
