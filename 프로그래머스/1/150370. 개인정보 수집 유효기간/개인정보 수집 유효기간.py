def calculateDifference(today, createdDate):
    todayYear, todayMonth, todayDate = map(int, today.split("."))
    createYear, createMonth, createDate = map(int, createdDate.split("."))
    
    ## 먼저 Date를 비교한다
    if todayDate < createDate:
        todayMonth -= 1
        todayDate = todayDate+28-createDate
    else:
        todayDate -= createDate
    
    ## Month를 비교한다
    if todayMonth < createMonth:
        todayYear -= 1
        todayMonth = todayMonth+12-createMonth
    else:
        todayMonth -= createMonth
    
    todayYear -= createYear
    
    return todayYear*12*28 + todayMonth*28 + todayDate
    

def solution(today, terms, privacies):
    answer = []
    ## 약관을 dictionary로 만들자
    termsDict = {}
    for val in terms:
        key, value = val.split(" ")
        termsDict[key] = int(value)

    ## 한달은 28일이라는 것을 기반으로 계산을 해야한다
    for index, privacy in enumerate(privacies):
        date, types = privacy.split()
        if calculateDifference(today, date) >= termsDict[types]*28:
            answer.append(index+1)
    
    return answer