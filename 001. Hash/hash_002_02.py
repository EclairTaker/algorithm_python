def solution(phone_book):
    answer = True
    # dict 자료형 선언
    num_list = {}

    for number in phone_book:
        num_list[number] = 1

    for number in phone_book:
        temp = ""
        for num_str in number:
            temp += num_str
            if (temp in num_list) and (temp != number):
                answer = False
                return answer

    return answer

fin_answer = solution(["119", "1195524421", "97674223"])
print(fin_answer)