from collections import defaultdict

# python에서 HashMap과 유사한 구조의 자료형은 dictionary 자료형 (dict)
def solution(participant, completion):
    answer = ''
    # dict 자료형 선언, dict()로도 만들 수 있다.
    # defaultdict를 통해 기본 key 값은 0인 int형으로 초기화
    race_list = defaultdict(int)
    
    # 반복분으로 participant를 dict에 추가하면서 그 value값을 증가, 동명이인 확인용
    for racer in participant:
        race_list[racer] += 1
    
    # 반복문으로 completion을 dict에서 검증
    for racer in completion:
        # completion에 있는 이름 = 완주자. 즉, 해당 완주자의 value 값을 1 증가, 동명이인 확인용
        if racer in race_list:
            race_list[racer] -= 1
    
    # dict.items 메소드를 통해 키-값으로 구성된 튜플 반환, 이를 반복문으로 확인
    for key, value in race_list.items():
        # value가 0이 아니라면 완주 실패라는 뜻, 따라서 key인 참가자 이름을 answer
        if value != 0:
            answer = key

    return answer

fin_answer = solution(["leo", "kiki", "eden"], ["eden", "kiki"])
print(fin_answer)