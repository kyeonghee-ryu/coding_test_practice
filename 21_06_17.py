citations =  [0, 1, 1]

def solution(citations):
    for i in range(len(citations),-1,-1):
        temp=[j for j in citations if j>=i]
        if len(temp)>=i and len(citations)-len(temp)<=i:
            answer = i
            break
    return answer

print(solution(citations))
# [0, 0, 0] -> 0, [0, 1, 1] -> 1
# 16번 오류
#
# [0, 1, 2] -> 1
# 11번 오류


# def solution(citations):
#     citations = sorted(citations)
#     l = len(citations)
#     for i in range(l):
#         if citations[i] >= l-i:
#             return l-i
#     return 0


# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer