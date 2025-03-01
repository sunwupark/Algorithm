def getKjinsu(n, k):
    kJinsu = ""
    while n > 0:
        n, val = n//k, n%k
        kJinsu+=str(val)
    
    return kJinsu[::-1]

import math
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
    
def solution(n, k):
    ## 먼저 k진수로 변경한다
    kJinsuString = getKjinsu(n,k)
    result = kJinsuString.split("0")
    
    count = 0
    for toCount in result:
        if toCount and isPrime(int(toCount)):
            count+=1
    
    return count