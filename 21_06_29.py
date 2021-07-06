# 프로그래머스 > DFS/BFS > 단어 변환
def solution(begin, target,words):
    if target not in words:
        return 0
    answer = 0
    visited = [0 for _ in range(len(words))]
    current_list = [begin]
    while current_list:
        # print(current_list,answer)
        current = current_list.pop()
        if current==target:
            return answer

        for i in range(len(words)):
            # print(i, visited, answer)
            if visited[i]==0:
                cnt=0
                for j in range(len(current)):
                    if words[i][j]==current[j]:
                        # print (words[i][j],visited)
                        cnt+=1
                if cnt==len(current)-1:
                    visited[i]=1
                    current_list.append(words[i])
        answer+=1

    return answer

begin='hit'
target='cog'
words = ["hot", "dot", "dog", "lot", "log"]
print(solution(begin,target,words))