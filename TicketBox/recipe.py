# 영수증 출력을 위한 결재 시스템 모듈

from movie import *
from food import *

class recipe: # 구입한 품목의 코드를 입력받는 객체

    def __init__(self, code, cost):
        self.code = code # 구입 품목 고유 코드
        self.cost = cost # 구입 품목 가격

# ------------------------------------------ 행 변경 함수 ---------------------------------------------

def row_column_return(row, column): # 아스키 코드를 사용하여 좌석 행열번호 문자로 출력
    return chr(abs(row-74)) + str(column)

# ----------------------------------------- 중복 체크 함수 ---------------------------------------------

def food_overlap_check(foodname_lists): # 영수증 출력을 위해, 중복된 요소가 있는 foodname_list에 중복요소를 계산하여 중복 요소 카운팅 값을 출력
    count = {}
    parchase_food_num = []
    for i in foodname_lists: # try,except 문을 사용하여 리스트 내 중복된 값을 카운팅해서 딕셔너리형으로 반환 후
        try: count[i] += 1
        except: count[i] = 1
    for i,j in count.items(): # 중복된 개수가 저장된 values값을 parchase_food_num 에 저장
        parchase_food_num.append(j)
    return list(parchase_food_num)

def list_overlap_check(lists): # 입력한 리스트 내 중복요소를 체크하여 중복 없이 리스트를 반환해주는 함수 (순서유지 장점이 있다.)
    overlap_check_list = [] # 중복요소를 체크한 후 반환 할 리스트 선언
    for i in lists: # 리스트 요소 반복 인덱싱
        if i not in overlap_check_list: # not in 메소드를 사용하여 중복요소를 제외하고 선언한 리스트에 추가
            overlap_check_list.append(i)
    return overlap_check_list # 중복요소가 체크된 리스트 반환

def food_cost_check(foodname_lists): # 영수증 출력 시 음식 이름에 따른 가격을 return 시켜 주는 cost 판별 함수
    parchase_food_cost = []
    for i in range(0, len(foodname_lists)):
        for j in range(0, len(food_list)):
            if foodname_lists[i] == food_list[j].name: # food_list 안에 있는 음식에 name값이랑 같을 때, 그 객체에 가격을 parchase_food_cost 리스트에 추가
                parchase_food_cost.append(food_list[j].cost)
    return parchase_food_cost

# --------------------------------------- 총합 계산 함수 ---------------------------------------------------

def total_cost(movie_cost, food_cost, food_num): # 영화 가격과 음식 가격을 모두 더해준 것을 반환 시키는 함수
    total = 0
    for i in range(0, len(movie_cost)):
        total += movie_cost[i]
    for j in range(0, len(food_cost)):
        total += food_cost[j]*food_num[j]
    return total

# --------------------------------------- 영수증 출력 함수 --------------------------------------------------

def trans_recipe(ticket_recipe): # 받은 레시피 리스트를 정렬하고 정리하여

    parchase_movie_name = [] # 구매한 영화 제목 정렬 리스트
    parchase_movie_cost = [] # 구매한 영화 가격 정렬 리스트
    parchase_movie_seat = [] # 구매한 영화 좌석 정렬 리스트
    parchase_food_name = [] # 구매한 음식 이름 정렬 리스트 -> 음식은 중복데이터를 검사하므로 name을 분해

    for i in range(0, len(ticket_recipe)):

        cinema_code = int(ticket_recipe[i].code / 10000) # 만의자리는 영화관 구별 코드
        movie_code = int((ticket_recipe[i].code - 10000*cinema_code) / 1000) # 천의자리는 영화 번호 코드
        row_code = int((ticket_recipe[i].code - 10000*cinema_code - 1000*movie_code) / 100) # 백의자리는 영화 행번호 코드
        column_code = int(ticket_recipe[i].code - 10000*cinema_code - 1000*movie_code - 100*row_code) # 나머지 두자리는 영화 열번호 코드, 만약 영화가 아니라면 음식 코드

        if cinema_code == 0: # 영화관 구별 코드가 없다는 뜻은 식품 구매
            parchase_food_name.append(food_list[column_code-1].name) # 식품 구매코드는 column_code이므로 이를 사용하여 리스트에 추가
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

    parchase_food_num = food_overlap_check(parchase_food_name) # set자료형을 통해 중복 값을 없애기 전에 중복값을 계산하는 함수를 사용해 각각 물건의 개수를 입력 받는다.
    parchase_food_name = list_overlap_check(parchase_food_name) # set으로 바꿔 중복요소를 바꿔주고 다시 리스트형으로 바꿔준다.[set으로 바뀌면서 시퀀스 성질을 잃어 순서가 바뀌는 오류를 발견]
    parchase_food_cost = food_cost_check(parchase_food_name) # 중복요소가 제거된 food_name 리스트를 통하여 가격을 뽑아주는 함수를 사용

    print('-' * 79)
    print('-                                 영수증 출력                                 -')
    print('-' * 79)
    if len(parchase_movie_name) == 0 and len(parchase_food_name) == 0:
        print('구매한 이력이 없습니다.')
    else:
        print('[구매한 영화]')
        for j in range(0, len(parchase_movie_name)):
            print('영화 : {} | 가격 : {}₩ | 좌석 : {}'.format(parchase_movie_name[j], parchase_movie_cost[j], parchase_movie_seat[j]))
        print('[구매한 식품]')
        for k in range(0, len(parchase_food_name)):
            print('식품 : {} | 가격 : {}₩ | 개수 : {}'.format(parchase_food_name[k], parchase_food_cost[k], parchase_food_num[k]))
    print('-' * 79)
    print('합계 금액 : {}₩'.format(total_cost(parchase_movie_cost, parchase_food_cost, parchase_food_num)))
    print('-' * 79)
    print('결재가 완료되었습니다.')


if __name__ == '__main__':
    ticket_recipe = []
    for i in range(0,2):
        ticket_recipe.append(recipe(11416, 8900))
    for j in range(0,2):
        ticket_recipe.append(recipe(2, 3200))
    trans_recipe(ticket_recipe)
