# 돌린 시뮬레이션 횟수를 통하여, 사용가격과 얻은 상금으로 기댓값을 출력해주는 함수 모듈

from random_func import *
from rank_class import *
from rank_func import *
from simulation_func import *

class lotto_money_class:

    def __init__(self, round_num, total_money, win_money):
        self.round_num = round_num # 각 회차 번호
        self.total_money = total_money # 각 회차에 남은 금액을 보관하는 객체
        self.win_money = win_money # 각 회차 총 상금 저장


lotto_money = [] # 회차별 상금을 보관할 리스트 생성

def money_list_len(iteration_num): # 리스트의 정보를 보관한 리스트 자릿수 추가 함수
    for i in range(1, iteration_num + 1):
        lotto_money.append(lotto_money_class(i, 0, 0))

def lotto_round_money(iteration_lotto_num):
    return 1000 * iteration_lotto_num # 한 횟차에 구입한 로또 총 금액

def lotto_round_rank1_money(total_money, rank1):

    if rank1 == 0:
        return 0
    else:
        return (total_money * 0.75) / rank1 # 1등은 3등과 4등에게 나누어준 금액의 75% 1/n씩 나눠서 수령

def lotto_round_rank2_money(total_money, rank2):

    if rank2 == 0:
        return 0
    else:
        return (total_money * 0.25) / rank2 # 2등은 3등과 4등에게 나누어준 금액의 25% 1/n씩 나눠서 수령

def revenue(round_money, win_money):
    return (win_money / round_money - 1) * 100 # 원금 회수률을 계산

def iter_sum(iter_num, sum_list): # 총 상금 계산기

    sum = 0 # 반환값 지정 변수

    for i in range(0, iter_num):
        sum += sum_list[i].win_money

    return sum
