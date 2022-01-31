# 프로그램 가동 main 페이지

from function import *
from word import *
from randomfunction import *

while True:

    program_swich1 = int(input('Welcome to Happy_Been word test program!! Plese pless anything number. (End : 0)'))

    if program_swich1 == 0:
        print('End the program.')
        break

    elif program_swich1 == 76693598:
        print('You activate admin mode.')

    else:
        add_day(day_list) # 시험볼 Day 리스트 확인
        word_extract(day_list) # 단어 가져오기 함수
