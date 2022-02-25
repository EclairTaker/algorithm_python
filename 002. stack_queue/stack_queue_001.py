# 기능 개선 문제
# Queue를 사용해서 해결
# python은 queue가 기본 list형에서 사용 가능함
# python에는 deque라고 해서 양 쪽으로 데이터 입출력이 가능한 자료형 존재

def solution(progress, speeds):
    answer = []
    # 배포 프로젝트 갯수
    pj_cnt = 0
    # 작업 반복 횟수
    temp = 1

    # 프로젝트 진행 체크에 활용할 변수 2개
    pj_progress = progress
    pj_speed = speeds

    # queue에서 pop해서 사용할 초기값용 변수들
    a = pj_progress.pop(0)
    b = pj_speed.pop(0)

    while(True):
        # project 진행 완료 및 배포 단계
        if (a + (b * temp) >= 100):
            # 동시에 배포되는 project 수 check용
            pj_cnt += 1
            # 더 이상 check할 project가 남지 않았을 경우
            if (len(progress) == 0):
                # 지금까지 check한 pj_cnt answer에 추가 후 break
                answer.append(pj_cnt)
                break
            # check할 project 수가 남았다면 그대로 해당 project도 배포 가능한지 여부 check
            else:
                a = progress.pop(0)
                b = speeds.pop(0)
        # project가 아직 배포 불가능
        else:
            # pj_cnt !=0 인데 새로 계산 결과 project 배포가 불가능하다.
            # 이는 곧 지금까지 합친 pj_cnt를 append 후 새로 cnt 해야한다는 뜻
            if (pj_cnt != 0):
                answer.append(pj_cnt)
                pj_cnt = 0

            # 위 과정을 지나면 작업을 1번 완료하였다고 판단 가능
            temp += 1
    
    return answer

def main()  :
    progress = [93, 30, 55]
    speeds = [1, 30, 5]
    answer = []

    answer = solution(progress, speeds)

    print(answer)


main()