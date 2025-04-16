def solution(board):
    answer = 1
    
    ## 실수를 했을 상황은 O==X인데 O가 빙고인 경우, O>X인데 X가 빙고인 경우, O<X인 경우
    ## 먼저 rowBingo, O,X의 개수를 Count해보자
    n = len(board)
    bingo = {"O": 0, "X": 0, ".":0}
    OC= 0
    XC= 0
    for i in range(n):
        tempOc = board[i].count('O')
        tempXc = board[i].count('X')
        if tempOc == 3:
            bingo["O"]+=1
        elif tempXc == 3:
            bingo["X"]+=1
        OC += tempOc
        XC += tempXc
    
    ## 세로 빙고 확인
    for j in range(n):
        if board[0][j] == board[1][j] == board[2][j]:
            bingo[board[0][j]]+=1
    
    ## 대각선 빙고 확인
    if board[0][0] == board[1][1] == board[2][2]:
        bingo[board[0][0]]+=1
    
    if board[0][2] == board[1][1] == board[2][0]:
        bingo[board[0][2]]+=1
    
    # print(bingo, OC, XC)
    ## 실수를 했을 상황은 O==X인데 O가 빙고인 경우, O>X인데 X가 빙고인 경우, O<X인 경우
    if (OC == XC and bingo["O"] > 0) or (OC > XC and bingo["X"] > 0) or (OC < XC) or (OC - XC > 1):
        return 0
    
    return answer