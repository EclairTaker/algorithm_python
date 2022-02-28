def solution(priorities, location):
    answer = 0
    # enumerate를 활용, location값을 고유 idx값으로 간직한 priority 정보를 구성
    # 이 녀석이 Queue 역할을 수행
    prio = [(idx, pri) for idx, pri in enumerate(priorities)]
    
    # Queue가 끝나지 않는 이상 반복문 수행
    while (len(prio) != 0):
        cur = prio.pop(0)
        # any()를 활용하여 prio값이 현재 값보다 클 경우 = 값을 미룬다
        if any(cur[1] < max[1] for max in prio):
            prio.append(cur)
        # 출력 수행
        else:
            answer += 1
            # [0]의 고유 idx값을 고유 location 식별값으로 활용 구분한다
            if (cur[0] == location):
                break
    
    return answer

def main()  :
    priorities = [2, 1, 3, 2]
    location = 2

    answer = solution(priorities, location)
    print(answer)

main()