# 본격적으로 프로그램이 돌아가는 페이지

import random
from random_func import *
from rank_class import *
from rank_func import *
from simulation_func import *

simulation_swich = 'start'

while True:

    if simulation_swich == 'end': # 시뮬레이션 종료 코드
        print('시뮬레이션을 종료하였습니다.')
        break

    else:
        select_lotto = input('연금복권과 로또 중에 원하는 시뮬레이션을 입력하세요. (종료를 원하시면 아무키를 누르세요.) : ')

        if select_lotto == '연금복권':
            print('제작중')

        elif select_lotto == '로또':
            iter_num = int(input('시뮬레이션을 돌릴 회차 수를 입력하세요. : '))
            iter_lotto_num = int(input('시뮬레이션에서 각 회차별 로또 개수를 입력하세요. : '))

            lotto_simulation(iter_num, iter_lotto_num)
        else:
            simulation_swich = input('입력형식이 잘못되었습니다. (종료하시려면 \'end\'를 입력하세요) : ')
