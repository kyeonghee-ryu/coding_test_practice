# 프로그래머스 > 탐욕법 > 조이스틱

a = 'ABCDEFGHIJKLMN OPQRSTUVWXYZ'
print(len('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
name = "JAZ"
# AJ(9) + 1 + E(4) + 1 + R(9) + 1 + O(12) + 1 + E(4) + 1 + N(13) = 56
# print(9+4+9+12+4+13)
res= 0
temp = 'A'*len(name)
for i in range(len(name)):
    if temp[i]!=name[i]:
        idx= a.find(name[i])
        if idx > 13:
            res+=(len(a)-idx+1)
        else:
            res+=(idx+1)
    else:
        res+=1
        continue
jabaz
print(res-1)


print(res-1)