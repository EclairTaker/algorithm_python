def solution(money, costs):
    answer = 0
    key = {1, 5, 10, 50, 100, 500}
    money_dict = dict()

    money = 4578
    costs = {1, 4, 99, 35, 50, 1000}

    print(len(money))
    print(len(costs))

    for i in range(len(costs)):
        print(111)
        money_dict[str(key[i])] = str(costs[i])


    return answer