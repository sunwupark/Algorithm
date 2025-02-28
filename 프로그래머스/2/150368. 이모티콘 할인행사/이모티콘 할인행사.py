def solution(users, emoticons):
    answer = []
    
    ## 할인율을 배분율에 따라서 permutation을 통해서 조합을 만들어보자
    from itertools import product
    ## 할인율이 루프를 돌면서 나온다
    results = []
    for val in product([10,20,30,40], repeat=len(emoticons)):
        totalSignup = 0
        totalPay = 0
        ## 각 사용자에게 
        for userIndex, user in enumerate(users):
            userPay = 0
            ## 각 항목이 사용자를 사게 한다면
            for itemIndex, discount in enumerate(list(val)):
                if discount >= user[0]:
                    userPay += emoticons[itemIndex]*(100-discount)/100
            
            ## 총 지출이 제한을 넘는다면 가입한다
            if userPay >= users[userIndex][1]:
                userPay = 0
                totalSignup+=1
            else:
                totalPay += userPay
        
        # print(list(val), totalSignup, totalPay)
        results.append((totalSignup, totalPay))
    
    results.sort(key=lambda x: (-x[0], -x[1]))

    return [results[0][0], results[0][1]]