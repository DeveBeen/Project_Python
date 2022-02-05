# Ramdom list 정렬로 문제 난수 제작

import random
from function import *
from word import *

def answer_random_set(question_count, test_num): # 받은 문제의 문항 수 만큼 문제 답의 단어코드를 난수로 받아 리스트로 반환하는 함수

    random_list = [] # 반환할 빈 리스트 받기

    i = 0

    while i < question_count:
        random_list.append(random.randint(1,len(test_num)))

        if i == 0: # 만약 i가 0이면 IndexError가 발생하니 i = 1부터 조건문 계산
            i += 1
        else:
            j = 0 # j = 0으로 초기화
            while j < i: # i 까지 반복하여 리스트 내에 i번째 값이랑 겹치는 것이 있는지 판단.
                if random_list[i] == random_list[j]: # 리스트 내에 겹치는 값이 있는 경우 (j는 i-1까지만 인덱싱하므로 i == j인 경우는 없다.)
                    random_list.pop() # pop()을 사용하여 마지막 원소를 제거 (마지막 원소 = i 원소)
                    random_list.append(random.randint(1,len(test_num))) # 다시 숫자를 리스트에 입력 (append도 리스트 마지막을 기준으로 채워지므로, i번째에 다시 들어간다.)
                    j = 0 # 새로 들어온 원소 값은 다시 다른 원소랑 같을 수 있으므로 처음부터 다시 점검
                else:
                    j += 1
            i += 1 # 위에 반복문을 한 번 돌렸으므로 다음 원소 값을 대입 후 다시 점검

    return random_list # 난수를 받은 리스트를 반환

# -------------------------------------------------------------------------------------------------------------------------------

def type_random_set(question_count): # 받은 문제 문항 수 만큼 그 문제 타입을 지정하여 리스트로 반환하는 함수

    random_list = [] # 반환할 빈 리스트 받기

    i = 0

    while i < question_count:
        random_list.append(random.randint(1,2))
        i += 1

    return random_list # 난수를 받은 리스트를 반환

# -------------------------------------------------------------------------------------------------------------------------------

def correct_random_set(question_count): # 답지 난수 리스트 제작 함수

    random_list = [] # 반환할 빈 리스트 받기

    i = 0

    while i < question_count:
        random_list.append(random.randint(1,4))
        i += 1

    return random_list # 난수를 받은 리스트를 반환

# -------------------------------------------------------------------------------------------------------------------------------

def example_random_set(test_num): # 보기로 출력할 예시 난수 3개를 리스트로 반환하는 함수

    random_list = [] # 반환할 빈 리스트 받기

    i = 0

    while i < 3:
        random_list.append(random.randint(1,len(test_num)))

        if i == 0: # 만약 i가 0이면 IndexError가 발생하니 i = 1부터 조건문 계산
            i += 1
        else:
            j = 0 # j = 0으로 초기화
            while j < i: # i 까지 반복하여 리스트 내에 i번째 값이랑 겹치는 것이 있는지 판단.
                if random_list[i] == random_list[j]: # 리스트 내에 겹치는 값이 있는 경우 (j는 i-1까지만 인덱싱하므로 i == j인 경우는 없다.)
                    random_list.pop() # pop()을 사용하여 마지막 원소를 제거 (마지막 원소 = i 원소)
                    random_list.append(random.randint(1,len(test_num))) # 다시 숫자를 리스트에 입력 (append도 리스트 마지막을 기준으로 채워지므로, i번째에 다시 들어간다.)
                    j = 0 # 새로 들어온 원소 값은 다시 다른 원소랑 같을 수 있으므로 처음부터 다시 점검
                else:
                    j += 1
            i += 1 # 위에 반복문을 한 번 돌렸으므로 다음 원소 값을 대입 후 다시 점검

    return random_list # 난수를 받은 리스트를 반환

# -------------------------------------------------------------------------------------------------------------------------------

def example_random_set_list(question_count, answer_random_list, test_num): # 예시 리스트가 정답 리스트와 겹치는 것을 방지하여 최종적인 예시 리스트를 묶어서 반환하는 리스트

    random_list = [] # 최종적으로 반환시킬 리스트
    count = 0 # 중복 검사 count 변수

    for code in answer_random_list: # answer_random_list 안에 있는 코드를 가져온다.

        while True: # 무한반복
            example_list = example_random_set(test_num) # example_random_set을 사용하여 난수 3개 부여

            for ex in example_list:

                if ex == code:
                    count += 1

            if count == 0:
                random_list.append(example_list) # count가 안됬다는 것은 중복된 값이 없다는 의미 -> 리스트에 추가
                break

            else:
                count = 0

    return random_list

if __name__ == '__main__':
    print(answer_random_set(question_count))
    print(type_random_set(question_count))
    print(correct_random_set(question_count))
    print(example_random_set())
    print(example_random_set_list(question_count,answer_random_set(question_count)))
