from collections import defaultdict

def solution(clothes):
    answer = 0
    temp = 1
    # dict 선언, defaultdict를 통해 초기값 0 int형으로 선언
    categories = defaultdict(int)

    # 각 옷의 카테고리별로 경우의 수 추가, 초기값이 다 0으로 되어있기 때문에 바로 증감시키면 된다
    for cloth_info in clothes:
        categories[cloth_info[1]] += 1
  
    # categories의 value값만 활용하여 경우의 수 계산. 해당 카테고리의 옷을 안 입는 경우도 포함해서 계산한다.
    for case_num in categories.values():
        temp *= (case_num + 1)

    # 최소한 한 가지 옷은 입었다는 전제이기에 옷을 전부 입지 않은 경우의 수 1가지를 감산한다
    answer = temp - 1
    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))