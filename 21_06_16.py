# def solution(numbers):
#     answer = ''
#     return answer
#
#
# numbers=[6, 10, 2]
# solution(numbers)
numbers=[3, 30, 34, 5, 9,30]




# print(list(map(lambda x: x.sort(),numbers)))
# print(list(map(str,numbers)))
# temp = sorted(list(map(str,numbers)),reverse=True)
# print(temp)
#
# for i in range(len(temp)-1):
#     if temp[i][-1]=='0' and temp[i+1]==temp[i][:-1]:
#         # print(i)
#         idx = temp.index(temp[i])
#         print(idx,temp[i])
#         temp.insert(idx+1,temp.pop(idx))
#         print(temp)
# print(''.join(temp))