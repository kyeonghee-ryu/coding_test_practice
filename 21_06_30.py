# 프로그래머스 > DFS/BFS > 여행경로

def solution(tickets):
    visited = [0 for _ in range(len(tickets))]
    queue = []
    tickets.sort(key=lambda x:x[1])
    print(tickets)
    for i in range(len(tickets)):
        if tickets[i][0]=='ICN':
            queue.append(tickets[i])
            visited[i]=1
            break
    answer = [queue[0][0]]

    while queue:
        q = queue.pop(0)
        answer.append(q[1])

        print(q,answer)
        for i in range(len(tickets)):
            if visited[i]==0:
                if tickets[i][0]== q[1]:
                    queue.append(tickets[i])
                    visited[i]=1
                    break


    return answer


tickets =  [["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]
print(solution(tickets))