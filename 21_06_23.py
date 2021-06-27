# 프로그래머스 > 탐욕법 > 큰 수 만들기

#시도 1 : 이 방법으로 했을 때, 테스트 9,10 에서 런타임 에러
def solution(number, k):
    l = len(number)-k
    answer = ''
    num_list = list(map(int,list(number)))

    while len(answer)!=l:
        if len(answer)!= l - 1:
            answer+=str(max(num_list[:-(l-len(answer))+1]))
            num_list = num_list[num_list.index(int(answer[-1]))+ 1:]

        else:
            answer+=str(max(num_list))
    return answer
