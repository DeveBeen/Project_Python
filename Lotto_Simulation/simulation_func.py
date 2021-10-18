# 한 회차에 입력한 수 만큼 자동 로또를 발급하였을 때, 당첨 횟수를 구해주는 시뮬레이션 프로그램

from random_func import *
from rank_func import *
from rank_class import *
from money_calculator import *
import random

def lotto_simulation(iter_num, iter_lotto_num):

    iteration_num = iter_num # 로또 횟차 수를 입력받는 변수 선언
    iteration_lotto_num = iter_lotto_num # 한 회당 로또 수를 입력받는 변수 선언

    logic = input('총 {}회,{}장씩 총 {}번 시뮬레이션 가동합니다. 실행하시겠습니까? (yes/all) : '.format(iteration_num, iteration_lotto_num, iteration_num*iteration_lotto_num))

    if logic == 'yes' and iteration_num*iteration_lotto_num <= 8145060: # 컴퓨터가 못버틸 수도 있으므로 시뮬레이션 losic을 한 번 걸치고 돌린다.

        lotto_total_money = 0 # 상금 계산 변수 선언

        for a in range(0, iteration_num):

            if a > 0:
                lotto_total_money -= lotto_money[a-1].win_money # 전 회차 우승 상금을 뺀다.

            lotto_total_money += 4072530000 # 로또의 모든 경우의 수를 사용자가 구매하였음을 가정, 한 회차당 쌓이는 금액을 더해준다. (구매금액의 50%는 상금이므로, 모든 경우의 수인 8145060 * 1000원 * 0.5)
            count_rank1 = 0 # 각각의 우승 횟수를 할당할 변수 선언
            count_rank2 = 0 # 각각의 우승 횟수를 할당할 변수 선언
            count_rank3 = 0 # 각각의 우승 횟수를 할당할 변수 선언
            count_rank4 = 0 # 각각의 우승 횟수를 할당할 변수 선언

            win_set = set(random_set([])) # 우승 리스트를 win_set에 할당

            for b in range(0, iteration_lotto_num):

                lotto_auto = random_set([]) # 자동 lotto를 입력받는다.
                list_len(iteration_num)

                count_rank1 += lotto_rank1(win_set, lotto_auto) # 1등 횟수 카운트
                count_rank2 += lotto_rank2(win_set, lotto_auto) # 2등 횟수 카운트
                count_rank3 += lotto_rank3(win_set, lotto_auto) # 3등 횟수 카운트
                count_rank4 += lotto_rank4(win_set, lotto_auto) # 4등 횟수 카운트

            lotto_info[a].rank1 = count_rank1 # 회차별 1등 횟수데이터를 저장
            lotto_info[a].rank2 = count_rank2 # 회차별 2등 횟수데이터를 저장
            lotto_info[a].rank3 = count_rank3 # 회차별 3등 횟수데이터를 저장
            lotto_info[a].rank4 = count_rank4 # 회차별 4등 횟수데이터를 저장

            money_list_len(iteration_num) # 상금 리스트를 할당

            lotto_money[a].total_money = lotto_total_money - 50000 * count_rank3 - 5000 * count_rank4 # 회차별 남은 상금을 저장
            lotto_money[a].win_money = lotto_round_rank1_money(lotto_total_money, count_rank1) * count_rank1 + lotto_round_rank2_money(lotto_total_money, count_rank2) * count_rank2 + 50000 * count_rank3 + 5000 * count_rank4 # 이번 회차에 받을 상금을 저장

        for c in range(0, iteration_num):
            print('{}회 결과'.format(lotto_info[c].round_num))
            print('1등 : {}회 | 인당 당첨금액 : {}원'.format(lotto_info[c].rank1, lotto_round_rank1_money(lotto_money[c].total_money ,lotto_info[c].rank1)))
            print('2등 : {}회 | 인당 당첨금액 : {}원'.format(lotto_info[c].rank2, lotto_round_rank2_money(lotto_money[c].total_money ,lotto_info[c].rank2)))
            print('3등 : {}회 | 인당 당첨금액 : {}원'.format(lotto_info[c].rank3, 50000))
            print('4등 : {}회 | 인당 당첨금액 : {}원'.format(lotto_info[c].rank4, 5000))
            print('사용금액 : {}원 | 당첨금 : {}원 | 수익률 : {}%'.format(lotto_round_money(iter_lotto_num), lotto_money[c].win_money, revenue(lotto_round_money(iter_lotto_num), lotto_money[c].win_money)))
            print('-' * 15)

        print('총사용금액 : {}원 | 총당청금 : {}원 | 총수익률 : {}%'.format(lotto_round_money(iter_lotto_num)*iteration_num, iter_sum(iteration_num, lotto_money), revenue(lotto_round_money(iter_lotto_num)*iteration_num, iter_sum(iteration_num, lotto_money))))
        print('실행결과 출력이 완료되었습니다.')

    else:
        print('시뮬레이션을 종료합니다 (시뮬레이션 수가 일정 수치를 넘으면 강제종료 됩니다)')

# -----------------------------연금복권--------------------------------------------

def pention_simulation(iter_num, iter_lotto_num):

    iteration_num = iter_num
    iteration_lotto_num = iter_lotto_num

    logic = input('총 {}회,{}장씩 총 {}번 시뮬레이션 가동합니다. 실행하시겠습니까? (yes/all) : '.format(iteration_num, iteration_lotto_num, iteration_num*iteration_lotto_num))

    if logic == 'yes' and iteration_num*iteration_lotto_num <= 5000000: # 컴퓨터가 못버틸 수도 있으므로 시뮬레이션 losic을 한 번 걸치고 돌린다.

        for a in range(0, iteration_num):

            count_pention_rank1 = 0 # 각각의 우승 횟수를 할당할 변수 선언
            count_pention_rank2 = 0 # 각각의 우승 횟수를 할당할 변수 선언
            count_pention_rank3 = 0 # 각각의 우승 횟수를 할당할 변수 선언
            count_pention_rank4 = 0 # 각각의 우승 횟수를 할당할 변수 선언

            win_list = random_pention_list([]) # 우승 리스트를 win_set에 할당

            for b in range(0, iteration_lotto_num):

                pention_auto = random_pention_list([]) # 자동 lotto를 입력받는다.
                pention_list_len(iteration_num)

                count_pention_rank1 += pention_rank1(win_list, pention_auto) # 1등 횟수 카운트
                count_pention_rank2 += pention_rank2(win_list, pention_auto) # 2등 횟수 카운트
                count_pention_rank3 += pention_rank3(win_list, pention_auto) # 3등 횟수 카운트
                count_pention_rank4 += pention_rank4(win_list, pention_auto) # 4등 횟수 카운트

            pention_info[a].pention_rank1 = count_pention_rank1 # 회차별 1등 횟수데이터를 저장
            pention_info[a].pention_rank2 = count_pention_rank2 # 회차별 2등 횟수데이터를 저장
            pention_info[a].pention_rank3 = count_pention_rank3 # 회차별 3등 횟수데이터를 저장
            pention_info[a].pention_rank4 = count_pention_rank4 # 회차별 4등 횟수데이터를 저장

        for c in range(0, iteration_num):
            print('{}회 결과'.format(pention_info[c].pention_round_num))
            print('1등 : {}회'.format(pention_info[c].pention_rank1))
            print('2등 : {}회'.format(pention_info[c].pention_rank2))
            print('3등 : {}회'.format(pention_info[c].pention_rank3))
            print('4등 : {}회'.format(pention_info[c].pention_rank4))
            print('-' * 15)

        print('실행결과 출력이 완료되었습니다.')

    else:
        print('시뮬레이션을 종료합니다 (시뮬레이션 수가 일정 수치를 넘으면 강제종료 됩니다)')

if __name__ == '__main__':
    lotto_simulation(5,100)
