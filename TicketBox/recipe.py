# 영수증 출력을 위한 결재 시스템 모듈

from movie import *
from food import *

class recipe: # 구입한 품목의 코드를 입력받는 객체

    def __init__(self, code, cost):
        self.code = code # 구입 품목 고유 코드
        self.cost = cost # 구입 품목 가격

def row_column_return(row, column): # 아스키 코드를 사용하여 좌석 행열번호 문자로 출력
    return chr(abs(row-74)) + str(16)

def trans_recipe(ticket_recipe): # 받은 레시피 리스트를 정렬하고 정리하여

    parchase_movie_name = [] # 구매한 영화 제목 정렬 리스트
    parchase_movie_cost = [] # 구매한 영화 가격 정렬 리스트
    parchase_movie_seat = [] # 구매한 영화 좌석 정렬 리스트
    parchase_food_name = [] # 구매한 음식 이름 정렬 리스트
    parchase_food_cost = [] # 구매한 음식 가격 정렬 리스트
    parchase_food_num = [] # 구매한 음식 개수 정렬 리스트

    for i in range(0, len(ticket_recipe)):

        cinema_code = int(ticket_recipe[i].code / 10000) # 만의자리는 영화관 구별 코드
        movie_code = int((ticket_recipe[i].code - 10000*cinema_code) / 1000) # 천의자리는 영화 번호 코드
        row_code = int((ticket_recipe[i].code - 10000*cinema_code - 1000*movie_code) / 100) # 백의자리는 영화 행번호 코드
        column_code = int(ticket_recipe[i].code - 10000*cinema_code - 1000*movie_code - 100*row_code) # 나머지 두자리는 영화 열번호 코드, 만약 영화가 아니라면 음식 코드

        if cinema_code == 0: # 영화관 구별 코드가 없다는 뜻은 식품 구매
            parchase_food_name.append(food_list[column_code-1].name) # 식품 구매코드는 column_code이므로 이를 사용하여 리스트에 추가
            parchase_food_cost.append(food_list[column_code-1].cost) # 식품 구매코드는 column_code이므로 이를 사용하여 리스트에 추가
            parchase_food_num.append(1) # 아직은 제작중 1로 대체
        elif cinema_code == 1: # 가족영화관 코드인 경우
            parchase_movie_name.append(family_movie_list[movie_code-1].name) # 구매 코드를 분석하여 영화 제목을 리스트에 추가
            parchase_movie_cost.append(family_movie_list[movie_code-1].cost) # 구매 코드를 분석하여 영화 가격을 리스트에 추가
            parchase_movie_seat.append(row_column_return(row_code, column_code)) # 구매 코드를 분석하여 영화관 좌석을 리스트에 추가
        elif cinema_code == 2: # 애니메이션 영화관 코드
            parchase_movie_name.append(animation_movie_list[movie_code-1].name) # 구매 코드를 분석하여 영화 제목을 리스트에 추가
            parchase_movie_cost.append(animation_movie_list[movie_code-1].cost) # 구매 코드를 분석하여 영화 가격을 리스트에 추가
            parchase_movie_seat.append(row_column_return(row_code, column_code)) # 구매 코드를 분석하여 영화관 좌석을 리스트에 추가
        elif cinema_code == 3:
            parchase_movie_name.append(premium_movie_list[movie_code-1].name) # 구매 코드를 분석하여 영화 제목을 리스트에 추가
            parchase_movie_cost.append(premium_movie_list[movie_code-1].cost) # 구매 코드를 분석하여 영화 가격을 리스트에 추가
            parchase_movie_seat.append(row_column_return(row_code, column_code)) # 구매 코드를 분석하여 영화관 좌석을 리스트에 추가

    print('-' * 79)
    print('-                                 영수증 출력                                 -')
    print('-' * 79)
    if len(parchase_movie_name) == 0 and len(parchase_food_name) == 0:
        print('구매한 이력이 없습니다.')
    else:
        print('[구매한 영화]')
        for j in range(0, len(parchase_movie_name)):
            print('영화 : {} 가격 : {}₩ 좌석 : {}'.format(parchase_movie_name[j], parchase_movie_cost[j], parchase_movie_seat[j]))
        print('[구매한 식품]')
        for k in range(0, len(parchase_food_name)):
            print('식품 : {} 가격 : {}₩  X{}'.format(parchase_food_name[j], parchase_food_cost[j], parchase_food_num[j]))


if __name__ == '__main__':
    ticket_recipe = []
    for i in range(0,2):
        ticket_recipe.append(recipe(11416, 8900))
    for j in range(0,2):
        ticket_recipe.append(recipe(2, 3200))
    trans_recipe(ticket_recipe)
