# 함수 모음 모듈

import random


def win_number(win_list): # 난수로 받은 로또 당첨 번호를 튜플로 변환시켜 안전성을 높이는 함수 (당첨 번호 고정 함수)
    return tuple(win_list)

def random_list(random_list): # 리스트를 받아 초기화 후 다른 난수를 입력하여 return 해주는 함수
    i = 0 # 반복함수 while 사용을 위해 변수 i 선언
    random_list = [] # 받은 리스트를 빈 리스트로 초기화
    while i < 6: # 6가지의 랜덤 수를 리스트에 할당
        random_list.append(random.randint(1, 45)) # 복권 번호 범위 설정 1-45
    if i == 1: # i가 1이면 IndexError가 발생하므로 i + 1
        i += 1
    elif random_list[i-1] == random_list[i]: # i가 2이상인 자연수일 때, 같은 난수가 반환될 수 있으므로 같은 번호가 입력될 때, 리스트에서 제거 (i+1 안함 : 또다시 같은 수가 들어올 수 있기 때문에)
        random_list.pop()
    else: # 다른 수가 나올 때는 다음 난수를 받는거로 넘어감
        i += 1
    return sorted(random_list) # 작은 수 순서로 정렬 후 반환


def lotto_rank1(win_list, random_list): # 받은 리스트가 1등 번호인지 확인하는 함수
    count = 0 # 맞는 횟수 판별 변수 선언
    for i in range(0,6):
        for j in range(0,6):
            if win_list[i] == random_list[j]:
                count += 1
            j += 1
        i += 1
    if count == 6: # 입력한 번호가 6개가 일치하면 1등
        return 1
    else:
        return 0

def lotto_rank2(win_list, random_list): # 받은 리스트가 2등 번호인지 확인하는 함수
    count = 0 # 맞는 횟수 판별 변수 선언
    for i in range(0,6):
        for j in range(0,6):
            if win_list[i] == random_list[j]:
                count += 1
            j += 1
        i += 1
    if count == 5: # 입력한 번호가 5개가 일치하면 2등
        return 1
    else:
        return 0

def lotto_rank3(win_list, random_list): # 받은 리스트가 3등 번호인지 확인하는 함수
    count = 0 # 맞는 횟수 판별 변수 선언
    for i in range(0,6):
        for j in range(0,6):
            if win_list[i] == random_list[j]:
                count += 1
            j += 1
        i += 1
    if count == 4: # 입력한 번호가 4개가 일치하면 3등
        return 1
    else:
        return 0

def lotto_rank4(win_list, random_list): # 받은 리스트가 4등 번호인지 확인하는 함수
    count = 0 # 맞는 횟수 판별 변수 선언
    for i in range(0,6):
        for j in range(0,6):
            if win_list[i] == random_list[j]:
                count += 1
            j += 1
        i += 1
    if count == 3: # 입력한 번호가 3개가 일치하면 4등
        return 1
    else:
        return 0

if __name__ == '__main__':
    print(win_number([1,2,3,4,5,6]))
    print(random_list([]))

    a = win_number([1,2,3,4,5,6])
    b = random_list([])

    print(lotto_rank1(a, b))
