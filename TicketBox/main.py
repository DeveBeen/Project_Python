# 영화관 키오스크 프로그램

from admin import *
from food import *
from movie import *
from function import *
from movie_seat import *
from recipe import *

ticket_recipe = [] # 최종 영수증 출력 시, 구입 폼목 코드를 받을 리스트 선언

while True:
    select_service = user_select_service() # 처음 서비스 선택s

    if select_service == 0: # 서비스 종료
        if len(ticket_recipe) == 0:
            print('결재 내역이 존재하지 않습니다. 서비스를 종료합니다.')
            break
        else:
            print('결재를 진행하겠습니다.')
            trans_recipe(ticket_recipe)
            break

    else: # 유저가 서비스를 선택하였을 때

            if select_service == 1: # user가 음식 주문 서비스를 선택하였을 때

                while True:
                    select_food = user_select_food()

                    if select_food == 0:
                        break

                    else:
                        print('{}을(를) 결재내역에 추가하였습니다.'.format(food_list[select_food-1].name))
                        food_recipe(ticket_recipe, select_food) # 선택한 음식을 영수증 내역에 추가

            elif select_service == 2: # user가 영화 예매 서비스를 선택하였을 때

                while True:
                    select_cinema = user_select_movie() # 영화관 종류 서비스 함수 실행

                    if select_cinema == 0: # 뒤로가기
                        break
                    else:
                        while True:
                            select_movie = movie_service(select_cinema) # 영화 예매 서비스 함수 실행

                            if select_cinema == 1:
                                print_family_movie_seat(select_movie)
                                row = input('원하는 자리의 행문자를 입력하세요. : ')
                                column = int(input('원하는 자리의 열번호를 입력하세요. : '))
                                ticket_recipe.append(recipe(ticketing_family_movie_seat(select_movie, row, column), family_movie_list[select_movie-1].cost)) # 구매한 영화 코드와 가격을 객체에 저장
                                break

                            elif select_cinema == 2:
                                print_animation_movie_seat(select_movie)
                                row = input('원하는 자리의 행문자를 입력하세요. : ')
                                column = int(input('원하는 자리의 열번호를 입력하세요. : '))
                                ticket_recipe.append(recipe(ticketing_animation_movie_seat(select_movie, row, column), animation_movie_list[select_movie-1].cost))
                                break

                            elif select_cinema == 3:
                                print_premium_movie_seat(select_movie)
                                row = input('원하는 자리의 행문자를 입력하세요. : ')
                                column = int(input('원하는 자리의 열번호를 입력하세요. : '))
                                ticket_recipe.append(recipe(ticketing_premium_movie_seat(select_movie, row, column), premium_movie_list[select_movie-1].cost))
                                break

                            else:
                                break



            elif select_service == 3: # user가 상영정보 시스템 선택

                while True:
                    print('상영정보를 보고싶은 영화관을 선택해주십시오')
                    select_cinema = user_select_movie()

                    if select_cinema == 0:
                        break

                    else:

                        while True:
                            select_movie = movie_service(select_cinema) # 상영정보 영화 선택

                            if select_cinema == 1:

                                break

                            elif select_cinema == 2:

                                break

                            elif select_cinema == 3:

                                break

                            else:
                                break
