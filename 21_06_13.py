prices=[1,2,3,2,3]
answer=[]

def solution(prices):
    answer = []
    while prices:
        q = prices.pop(0)
        cnt=0s
        for price in prices:
            cnt+=1
            if q <= price:
                continue
            else:
                break
        answer.append(cnt)
    return answer

print(solution(prices))