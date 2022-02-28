def solution(priorities, location):
    answer = 0
    priority = priorities

    # Queue 내 최고 priority check
    my_prio = priority[location]
    temp = 0

    while(len(priority)!=0):
        max_prio = max(priority)
        cur_prio = priority[0]
        # 어쨌든 상관없이 미뤄야 함
        if (cur_prio < max_prio):
            priority.pop(0)
            priority.append(cur_prio)
            # 목표 문서가 cur_doc이였다면
            if (location == 0):
                location = len(priority) - 1
            # 목표 문서가 current가 아닐 경우, location != 0
            else:
                location -= 1
        # cur_prio >= max_prio, max_prio보다 클 수는 없기에 cur_prio == max_prio일 경우
        else:
            if (cur_prio > my_prio):
                priority.pop(0)
                location -= 1
                # 출력이 수행되었으니까
                temp += 1
            # cur_prio == my_prio == max_prio일 경우
            else:
                priority.pop(0)
                temp += 1
                if (location == 0):
                    answer = temp
                    break
                else:
                    location -= 1
        print(temp)
    return answer

def main()  :
    priorities = [2, 1, 3, 2]
    location = 2

    answer = solution(priorities, location)
    print(answer)

main()