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

def pention_rank1(win_list, random_list): # 받은 리스트가 1등 번호인지 확인하는 함수

        count = 0

        if win_list[0] != random_list[0]:
            return 0
        else:
            for i in range(1, 7):
                if win_list[i] == random_list[i]:
                    count += 1

        if count == 6:
            return 1
        else:
            return 0

def pention_rank2(win_list, random_list): # 받은 리스트가 1등 번호인지 확인하는 함수

        count = 0

        if win_list[0] != random_list[0]:
            return 0
        else:
            for i in range(1, 7):
                if win_list[i] == random_list[i]:
                    count += 1

        if count == 5:
            return 1
        else:
            return 0

def pention_rank3(win_list, random_list): # 받은 리스트가 1등 번호인지 확인하는 함수

        count = 0

        if win_list[0] != random_list[0]:
            return 0
        else:
            for i in range(1, 7):
                if win_list[i] == random_list[i]:
                    count += 1

        if count == 4:
            return 1
        else:
            return 0

def pention_rank4(win_list, random_list): # 받은 리스트가 1등 번호인지 확인하는 함수

        count = 0

        if win_list[0] != random_list[0]:
            return 0
        else:
            for i in range(1, 7):
                if win_list[i] == random_list[i]:
                    count += 1

        if count == 3:
            return 1
        else:
            return 0


if __name__ == '__main__': # rank 함수 테스트

        win_set = random_set([])

        simulation = int(input('몇 번 테스트를 할 까요? : '))

        count_rank1 = 0
        count_rank2 = 0
        count_rank3 = 0
        count_rank4 = 0

        for i in range(0, simulation):
            random_list = random_set([])

            count_rank1 += lotto_rank1(win_set, random_list)
            count_rank2 += lotto_rank2(win_set, random_list)
            count_rank3 += lotto_rank3(win_set, random_list)
            count_rank4 += lotto_rank4(win_set, random_list)

        print('1등 : {}'.format(count_rank1))
        print('2등 : {}'.format(count_rank2))
        print('3등 : {}'.format(count_rank3))
        print('4등 : {}'.format(count_rank4))

        # 연금복권

        win_list = random_pention_list([])

        pention_simulation = int(input('몇 번 테스트를 할 까요? : '))

        count_pention_rank1 = 0
        count_pention_rank2 = 0
        count_pention_rank3 = 0
        count_pention_rank4 = 0

        for i in range(0, pention_simulation):
            random_pention_list = random_pention_list([])

            count_pention_rank1 += pention_rank1(win_list, random_pention_list)
            count_pention_rank2 += pention_rank2(win_list, random_pention_list)
            count_pention_rank3 += pention_rank3(win_list, random_pention_list)
            count_pention_rank4 += pention_rank4(win_list, random_pention_list)

        print('1등 : {}'.format(count_pention_rank1))
        print('2등 : {}'.format(count_pention_rank2))
        print('3등 : {}'.format(count_pention_rank3))
        print('4등 : {}'.format(count_pention_rank4))
