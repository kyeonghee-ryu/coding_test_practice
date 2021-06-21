answers = [1,3,2,4,2]
s1 = [1,2,3,4,5]
s2 = [2, 1, 2, 3, 2, 4, 2, 5]
s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

s = [s1,s2,s3]
for i in range(len(s)):
    if len(answers)>=len(s[i]):
        q = len(answers)//len(s[i])
        r = len(answers)%len(s[i])
        s[i] = s[i]*q+s[i][:r]
    else:
        s[i] = s[i][:len(answers)]

# for i in range(len(s)):
#     q = len(answers)//len(s[i])
#     r = len(answers)%len(s[i])
#     s[i] = s[i]*q+s[i][:r]
# 왜인지는 모르겠지만 위의 if-else문이 더 빨리 끝남


res = []
for i in range(len(s)):
    cnt = 0
    for j,k in zip(s[i],answers):
        if j==k:
            cnt+=1
    res.append(cnt)

answer = []
for i in range(len(res)):
    if max(res)==res[i]:
        answer.append(i+1)

print(answer)





######################################
#참고하면 좋은 코드
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result