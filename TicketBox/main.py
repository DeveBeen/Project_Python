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

            if select_service == 1: # user가 음식 주문 서비스를 선택하였을 때
                print('음식 주문 시스템 - 제작중')

            elif select_service == 2: # user가 영화 예매 서비스를 선택하였을 때

                while True:
                    select_cinema = user_select_movie() # 영화관 종류 서비스 함수 실행

                    if select_cinema == 0: # 뒤로가기
                        break
                    else:
                        select_movie = movie_service(select_cinema) # 영화 예매 서비스 함수 실행

            elif select_service == 3: # user가 상영정보 시스템 선택
                print('상영정보 시스템 - 제작중')
            else:
                continue
