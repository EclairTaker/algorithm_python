# programmers 문제풀이 참고
# python에서 HashMap과 유사한 구조의 자료형은 dictionary 자료형 (dict)
def solution(participant, completion):
    answer = ''
    # 후술할 hash() 활용을 위한 int형 초기화
    temp = 0
    # dict 자료형 선언, dict()로도 만들 수 있다.
    race_list = {}

    for racer in participant:
        # racer를 hash한 값을 key로 가지는 dict 선언, value 값으로는 그 참가자 이름을 기록한다.
        race_list[hash(racer)] = racer
        # 해당 해시값들을 temp에 다 저장하게 된다. 동명이인 체크 가능
        temp += int(hash(racer))
    
    for racer in completion:
        # 완주자 이름을 해싱한 값을 temp에서 차례로 제거
        temp -= int(hash(racer))
    
    # 남은 temp의 값을 key로 가지는 value가 바로 낙오자 이름
    answer = race_list[temp]
    return answer

fin_answer = solution(["leo", "kiki", "eden"], ["eden", "kiki"])
print(fin_answer)