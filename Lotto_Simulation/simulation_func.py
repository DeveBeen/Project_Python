# 한 회차에 입력한 수 만큼 자동 로또를 발급하였을 때, 당첨 횟수를 구해주는 시뮬레이션 프로그램

from random_func import *
from rank_func import *
from rank_class import *
import random

def lotto_simulation(iter_num, iter_lotto_num):

    count_rank1 = 0 # 각각의 우승 횟수를 할당할 변수 선언
    count_rank2 = 0 # 각각의 우승 횟수를 할당할 변수 선언
    count_rank3 = 0 # 각각의 우승 횟수를 할당할 변수 선언
    count_rank4 = 0 # 각각의 우승 횟수를 할당할 변수 선언

    iteration_num = iter_num
    iteration_lotto_num = iter_lotto_num

    logic = input('총 {}회,{}장씩 총 {}번 시뮬레이션 가동합니다. 실행하시겠습니까? (yes/all) : '.format(iteration_num, iteration_lotto_num, iteration_num*iteration_lotto_num))

    if logic == 'yes' and iteration_num*iteration_lotto_num <= 8145060: # 컴퓨터가 못버틸 수도 있으므로 시뮬레이션 losic을 한 번 걸치고 돌린다.

        for a in range(0, iteration_num):

            win_set = set(random_set([])) # 우승 리스트를 win_set에 할당

            for b in range(0, iteration_lotto_num):

                lotto_auto = random_set([]) # 자동 lotto를 입력받는다.

                count_rank1 += lotto_rank1(win_set, lotto_auto) # 1등 횟수 카운트
                count_rank2 += lotto_rank2(win_set, lotto_auto) # 2등 횟수 카운트
                count_rank3 += lotto_rank3(win_set, lotto_auto) # 3등 횟수 카운트
                count_rank4 += lotto_rank4(win_set, lotto_auto) # 4등 횟수 카운트

                lotto_info[a].lotto_num.append(a)
                lotto_info[a].rank1.append(rank1)
                lotto_info[a].rank2.append(rank2)
                lotto_info[a].rank3.append(rank3)
                lotto_info[a].rank4.append(rank4)

        for c in range(0, iteration_num):
            print('{}회 결과'.format(rank_num[c].lotto_num))
            print('1등 : {}회'.format(rank_num[c].rank1))
            print('2등 : {}회'.format(rank_num[c].rank2))
            print('3등 : {}회'.format(rank_num[c].rank3))
            print('4등 : {}회'.format(rank_num[c].rank4))
            print('-' * 15)

            print('시뮬레이션을 종료합니다.')

    else:
        print('시뮬레이션을 종료합니다 (시뮬레이션 수가 일정 수치를 넘으면 강제종료 됩니다)')

if __name__ == '__main__':
    lotto_simulation(5, 5)
