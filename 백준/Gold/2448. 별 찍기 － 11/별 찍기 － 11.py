N = int(input())
stars = [[" " for _ in range(N*2)] for _ in range(N)]

toMove = [(0,0), (1, -1), (1,1), (2, -2), (2, -1), (2,0), (2,1), (2,2)]

def dac(startx, starty, length):
    if length == 3:
        for x,y in toMove:
            stars[x+startx][y+starty] = "*"
    else:
        length = length//2
        dac(startx, starty, length)
        dac(startx+length, starty-length, length)
        dac(startx+length, starty+length, length)

dac(0, N-1, N)
for star in stars:
    print("".join(star))