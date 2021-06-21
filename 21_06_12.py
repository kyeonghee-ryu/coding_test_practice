#프로그래머스 >스택/큐 > 다리를 지나는 트럭
bridge_length=2
weight = 10
truck_weights = [7,4,5,6]
truck_num = len(truck_weights)
finish = []
road = []
answer = 0

road = [0 for _ in range(bridge_length)]

while len(road)!=0:
    # print(road)
    answer += 1
    road.pop(0)
    if len(truck_weights)!=0:
        if sum(road) + truck_weights[0] <= weight:
            road.append(truck_weights[0])
            truck_weights.pop(0)
        else:
            road.append(0)
print(answer)
