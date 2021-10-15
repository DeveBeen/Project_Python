# 랜덤으로 수 반환 함수 모듈

import random


def win_number(win_list): # 난수로 받은 로또 당첨 번호를 튜플로 변환시켜 안전성을 높이는 함수 (당첨 번호 고정 함수)
    return tuple(win_list)

def random_list(random_list): # 리스트를 받아 초기화 후 다른 난수를 입력하여 return 해주는 함수

    random_list.clear() # 리스트 값을 초기화

    for i in range(6):
        random_list.append(random.randint(1,45)) # 1 ~ 45 중에서 랜덤으로 추가

        if i == 0: # 만약 i가 0이면 IndexError가 발생하니 i = 1부터 조건문 계산
            i += 1
        else:
            for j in range(i): # i 까지 반복하여 리스트 내에 i번째 값이랑 겹치는 것이 있는지 판단.
                if random_list[i] == random_list[j]: # 리스트 내에 겹치는 값이 있는 경우 (j는 i-1까지만 인덱싱하므로 i == j인 경우는 없다.)
                    random_list.pop() # pop()을 사용하여 마지막 원소를 제거 (마지막 원소 = i 원소)
                    random_list.append(random.randint(1,45)) # 다시 숫자를 리스트에 입력 (append도 리스트 마지막을 기준으로 채워지므로, i번째에 다시 들어간다.)
                    j = 0 # 새로 들어온 원소 값은 다시 다른 원소랑 같을 수 있으므로 처음부터 다시 점검
                else:
                    j += 1
            i += 1 # 위에 반복문을 한 번 돌렸으므로 다음 원소 값을 대입 후 다시 점검

    return random_list

# ------------------------------------------------------------------------------------------

def random_list_test(random_list): # 리스트를 받아 초기화 후 다른 난수를 입력하여 return 해주는 함수

    random_list.clear() # 리스트 값을 초기화

    for i in range(6):
        random_list.append(random.randint(1,6))
        print(random_list)

        if i == 0: # 만약 i가 0이면 IndexError가 발생하니 i = 1부터 조건문 계산
            i += 1
        else:
            for j in range(i): # i 까지 반복하여 리스트 내에 i번째 값이랑 겹치는 것이 있는지 판단.
                if random_list[i] == random_list[j]: # 리스트 내에 겹치는 값이 있는 경우 (j는 i-1까지만 인덱싱하므로 i == j인 경우는 없다.)
                    random_list.pop() # pop()을 사용하여 마지막 원소를 제거 (마지막 원소 = i 원소)
                    random_list.append(random.randint(1,6)) # 다시 숫자를 리스트에 입력 (append도 리스트 마지막을 기준으로 채워지므로, i번째에 다시 들어간다.)
                    j = 0 # 새로 들어온 원소 값은 다시 다른 원소랑 같을 수 있으므로 처음부터 다시 점검
                else:
                    j += 1
            i += 1 # 위에 반복문을 한 번 돌렸으므로 다음 원소 값을 대입 후 다시 점검

    return random_list


if __name__ == '__main__':
    print(random_list_test([]))
