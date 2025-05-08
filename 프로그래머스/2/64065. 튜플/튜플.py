import re
def solution(s):
    answer = []
    total = s.split("}")
    tempList = []
    for val in total:
        if val != "":
            curr = val.replace("{", "").replace("}", "").split(",")
            if '' in curr:
                curr.remove('')
            tempList.append(curr)
    
    tempList.sort(key=lambda x: len(x))
    
    for val in tempList:
        for cur in val:
            if int(cur) not in answer:
                answer.append(int(cur))
            
    return answer