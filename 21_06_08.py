# 백준 15829번

import sys
input = sys.stdin.readline
n = input()
s = list(map(str,input().rstrip()))
alphabet = 'abcdefghijklmnopqrstuvwxyz'
cnt = 0
for i in range(len(s)):
    num = alphabet.index(s[i])
    cnt+=(num+1)*(31**i)
print(cnt)


#프로그래머스 > 해시 > 전화번호 목록

def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        head_len = len(phone_book[i])
        for j in range(i+1,len(phone_book)):
            if phone_book[i]==phone_book[j][:head_len]:
                answer=False
                break
    return answer


#best code
def solution(phone_book):
    answer = True

    # phone_book.sort(key=lambda x: len(x))

    num_hash = {}
    for num in phone_book:
        num_hash[num] = 1

    for num in phone_book:
        tmp = ''
        for i in num:
            tmp += i
            if tmp in num_hash and tmp != num:
                answer = False
                break

    return answer