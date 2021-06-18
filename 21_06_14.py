#프로그래머스 > heap > 더 맵게

scoville=[1, 2, 3, 9, 10, 12]
K=7
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt=0
    while True:
        if len(scoville)<=1 and scoville[0]<K:
            cnt=-1
            break
        if scoville[0]>K:
            break
        new_num = heapq.heappop(scoville)+(heapq.heappop(scoville)*2)
        heapq.heappush(scoville,new_num)
        cnt+=1
    return cnt

print(solution(scoville,K))