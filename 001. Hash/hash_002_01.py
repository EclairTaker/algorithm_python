# 가장 편한 방법은 startswith() & 이중 for문 활용.
# But, 효율성 실패
def solution(phone_book):
    answer = True
    cvt_book = []

    # 과정 1. 전화번호부를 오름차순으로 맞게 정렬, 이를 위해 key값과 value를 해싱
    for number in phone_book:
        cvt_book.append(int(number))

    # 정렬 수행
    cvt_book.sort()
    
    for number in cvt_book:
        for str_number in phone_book:
            if (str_number.startswith(str(number))) and (str_number != str(number)):
                print(number)
                print(str_number)
                answer = False
                return answer

    return answer

fin_answer = solution(["119", "1195524421", "97674223"])
print(fin_answer)