# 1등,2등,3등,4등 랭크를 선정해주는 함수 모듈

import random
from random_func import *

def lotto_rank1(win_set, random_list): # 받은 리스트가 1등 번호인지 확인하는 함수

        if len(win_set.intersection(random_list)) == 6: # 교집합의 개수 매소드로 판단
            return 1
        else:
            return 0

def lotto_rank2(win_set, random_list): # 받은 리스트가 2등 번호인지 확인하는 함수

        if len(win_set.intersection(random_list)) == 5:
            return 1
        else:
            return 0

def lotto_rank3(win_set, random_list): # 받은 리스트가 3등 번호인지 확인하는 함수

        if len(win_set.intersection(random_list)) == 4:
            return 1
        else:
            return 0

def lotto_rank4(win_set, random_list): # 받은 리스트가 4등 번호인지 확인하는 함수

        if len(win_set.intersection(random_list)) == 3:
            return 1
        else:
            return 0

# --------------------------------연금복권------------------------------------------


if __name__ == '__main__': # rank 함수 테스트

        win_set = random_set([])

        simulation = int(input('몇 번 테스트를 할 까요? : '))

        couunt_rank1 = 0
        couunt_rank2 = 0
        couunt_rank3 = 0
        couunt_rank4 = 0

        for i in range(0, simulation):
            random_list = random_set([])

            couunt_rank1 += lotto_rank1(win_set, random_list)
            couunt_rank2 += lotto_rank2(win_set, random_list)
            couunt_rank3 += lotto_rank3(win_set, random_list)
            couunt_rank4 += lotto_rank4(win_set, random_list)

        print('1등 : {}'.format(couunt_rank1))
        print('2등 : {}'.format(couunt_rank2))
        print('3등 : {}'.format(couunt_rank3))
        print('4등 : {}'.format(couunt_rank4))
