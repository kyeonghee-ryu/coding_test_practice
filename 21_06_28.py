# 프로그래머스 > DFS/BFS > 네트워크
#
# def solution(n, computers):
#     nw = [0 for _ in range(n)]
    # cnt=0
    # for i in range(n):
    #     if nw[i]==0:
    #         cnt+=1
    #         nw[i]=1
    #         for j in range(len(computers[i])):
    #             print(i,j)
    #             if i!=j:
    #                 if computers[i][j]==1 and nw[j]==0:
    #                     nw[j]=1
    #                     print(j,nw)
    #             else:
    #                 continue
    #     else:
    #         continue
    #     print(i,nw)
    #
    # return cnt



def solution(n, computers):
    nw = [0 for _ in range(n)]
    cnt=0
    for i in range(n):
        if nw[i]==0:
            BFS(n, computers, nw,i)
            cnt+=1
    return cnt

def BFS(n, computers, nw,i):
    nw[i]=1
    queue = []
    queue.append(i)
    while len(queue)!=0:
        i = queue.pop(0)
        nw[i]=1
        for j in range(n):
            if i!=j and computers[i][j]==1:
                if nw[j]==0:
                    queue.append(j)



n = 3
computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n,computers))
