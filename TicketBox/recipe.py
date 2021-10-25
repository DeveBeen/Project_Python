# 영수증 출력을 위한 결재 시스템 모듈

class recipe: # 구입한 품목의 코드를 입력받는 객체

    def __init__(self, code, cost):
        self.code = code # 구입 품목 고유 코드
        self.cost = cost # 구입 품목 가격

def trans_recipe(ticket_recipe):

    parchase_movie_name = [] # 구매한 영화 제목 정렬 리스트
    parchase_movie_cost = [] # 구매한 영화 가격 정렬 리스트
    parchase_movie_seat = [] # 구매한 영화 좌석 정렬 리스트
    parchase_food_name = [] # 구매한 음식 이름 정렬 리스트
    parchase_food_cost = [] # 구매한 음식 가격 정렬 리스트
    parchase_food_num = [] # 구매한 음식 개수 정렬 리스트

    for i in range(0, len(list)):

        if list[i] > 10000:
