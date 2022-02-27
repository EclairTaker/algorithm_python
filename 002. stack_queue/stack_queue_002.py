def solution(priorities, location):
    answer = 0

    # Queue 내 최고 priority check
    prio_max = max(priorities)
    my_prio = priorities[location]

    while(True):
        temp = priorities.pop()
        if (prio_max > my_prio):
            priorities.add(temp)
            if (location > 0):
                

        # 어차피 prio_max가 아니며 계속 미뤄야 함

            

    return answer

def main()  :
    priorities = [2, 1, 3, 2]
    location = 2

    answer = solution(priorities, location)
    print(answer)

main()