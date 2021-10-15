# 1등,2등,3등,4등 랭크를 선정해주는 함수 모듈

import random
from random_func import *
from rank_class import *

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

if __name__ == '__main__': # rank 함수 테스트
