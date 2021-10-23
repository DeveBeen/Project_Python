# 영화관 별 좌석 클래스 객체 생성 모듈

from movie import *

class family_movie_seat(): # 가족 영화관 좌석 클래스

    def __init__(self, movie_state, movie_name, row, column):
        self.movie_state = movie_state # 좌석의 상태
        self.movie_name = movie_name # 영화 이름
        self.row = row # 행 번호
        self.column = column # 열 번호

class animation_movie_seat(): # 애니메이션 영화관 좌석 클래스

    def __init__(self, movie_state, movie_name, row, column):
        self.movie_state = movie_state
        self.movie_name = movie_name
        self.row = row
        self.column = column

class premium_movie_seat(): # 프리미어 영화관 좌석 클래스

    def __init__(self, movie_state, movie_name, row, column):
        self.movie_state = movie_state
        self.movie_name = movie_name
        self.row = row
        self.column = column

# ------------------------------------ <초기설정> ------------------------------------------------------------------------------------

family_movie_seat_list = []
animation_movie_seat_list = []
premium_movie_seat_list = []
row_number_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] # 행 문자 10행

for i in range(0, len(family_movie_list)):
    for j in range(0, len(row_number_list)):
        for k in range(0, 10):
            family_movie_seat_list.append(family_movie_seat('[]', family_movie_list[i].name, row_number_list[j], k))

for i in range(0, len(animation_movie_list)):
    for j in range(0, len(row_number_list)):
        for k in range(0, 10):
            animation_movie_seat_list.append(animation_movie_seat('[]', animation_movie_list[i].name, row_number_list[j], k))

for i in range(0, len(premium_movie_list)):
    for j in range(0, len(row_number_list)):
        for k in range(0, 10):
            premium_movie_seat_list.append(premium_movie_seat('[]', premium_movie_list[i].name, row_number_list[j], k))

# ----------------------------------- < 좌석 상태 출력 및 체크 시스템 > ------------------------------------------------------------------


if __name__ == '__main__':
    print(family_movie_seat_list)
