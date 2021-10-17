# 돌린 시뮬레이션 횟수를 통하여, 사용가격과 얻은 상금으로 기댓값을 출력해주는 함수 모듈

from random_func import *
from rank_class import *
from rank_func import *
from simulation_func import *

def lotto_round_money(iteration_lotto_num):
    return 500 * iteration_lotto_num # 입력한 시뮬레이션의 한 횟차의 수익금의 50%

def lotto_rank1_money(total_money, rank1):
    return (total_money * 0.75) / rank1 # 1등은 쌓여있는 금액을 모두 받는다.

def lotto_rank2_money(total_money, rank2):
    return (total_money * 0.25) / rank2
