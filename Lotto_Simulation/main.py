# 한 회차에 입력한 수 만큼 자동 로또를 발급하였을 때, 당첨 횟수를 구해주는 시뮬레이션 프로그램

from function import *
from rank_class import *
import random

rank1 = 0 # 각각의 우승 횟수를 할당할 변수 선언
rank2 = 0
rank3 = 0
rank4 = 0

iteration_num = int(input('시뮬레이션 돌릴 횟차 수를 입력하세요. : '))
iteration_lotto_num = int(input('한 횟차 별 시뮬레이션을 돌릴 복권 횟수를 입력하세요. : '))

logic = input('총 {}회,{}장씩 총 {}번 시뮬레이션 가동합니다. 실행하시겠습니까? (yes/all) : '.format(iteration_num, iteration_lotto_num, iteration_num*iteration_lotto_num))

if logic == 'yes': # 컴퓨터가 못버틸 수도 있으므로 시뮬레이션 losic을 한 번 걸치고 돌린다.

    random_num = [] # 시뮬레이션을 돌릴 랜덤 리스트를 선언

    for a in range(0, iteration_num):

        win_list = random_list(random_num) # 우승 리스트를 win_list에 할당

        print(win_list)

        for b in range(0, iteration_lotto_num):

            lotto_auto = random_list(random_num) # 자동 lotto를 입력받는다.

            rank1 += lotto_rank1(win_list, lotto_auto) # 1등 횟수 카운트
            rank2 += lotto_rank2(win_list, lotto_auto) # 2등 횟수 카운트
            rank3 += lotto_rank3(win_list, lotto_auto) # 3등 횟수 카운트
            rank4 += lotto_rank4(win_list, lotto_auto) # 4등 횟수 카운트

        lotto_info[a].lotto_num.append(a)
        lotto_info[a].rank1.append(rank1)
        lotto_info[a].rank2.append(rank2)
        lotto_info[a].rank3.append(rank3)
        lotto_info[a].rank4.append(rank4)

    for c in range(0, iteration_num, 1):
        print('{}회 결과'.format(rank_num[c].lotto_num))
        print('1등 : {}회'.format(rank_num[c].rank1))
        print('2등 : {}회'.format(rank_num[c].rank2))
        print('3등 : {}회'.format(rank_num[c].rank3))
        print('4등 : {}회'.format(rank_num[c].rank4))
        print('-' * 15)

    print('시뮬레이션을 종료합니다.')

else:
    print('시뮬레이션을 종료합니다.')