# 영화관 키오스크 프로그램

from admin import *
from food import *
from movie import *
from function import *

while True:
    select_service = user_select_service() # 처음 서비스 선택

    if select_service == 0: # 서비스 종료
        print('서비스를 종료합니다.')
        break
    else: # 유저가 메뉴를 선택하였을 때

            if select_service == 1:

                print('-' * 35)
                print('-            음식 선택            -')
                print('-' * 35)
                print('1. 시크 메뉴')
                print('2. 애니메이션 영화 2관')
                print('3. 프리미엄 영화 3관')
                print('(종료를 원하시면 0번을 누르십시오.)')
                select_food = int(input('입력 : ')) # 음식 선택지 입력

            elif select_service == 2:

                print('-' * 35)
                print('-           영화관 선택           -')
                print('-' * 35)
                print('1. 가족 영화 3관')
                print('2. 애니메이션 영화 2관')
                print('3. 프리미엄 영화 3관')
                print('(종료를 원하시면 0번을 누르십시오.)')
                select_cinema = int(input('입력 : ')) # 영화 선택지 입력

            elif select_service == 3:
                print('상영정보 - 제작중')
            elif select_service == 7477:
                print('관리자 모드 - 제작중')
