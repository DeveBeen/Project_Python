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
        for k in range(0, 20):
            family_movie_seat_list.append(family_movie_seat('[{}]'.format(k+1), family_movie_list[i].name, row_number_list[j], k))

for i in range(0, len(animation_movie_list)):
    for j in range(0, len(row_number_list)):
        for k in range(0, 20):
            animation_movie_seat_list.append(animation_movie_seat('[{}]'.format(k+1), animation_movie_list[i].name, row_number_list[j], k))

for i in range(0, len(premium_movie_list)):
    for j in range(0, len(row_number_list)):
        for k in range(0, 20):
            premium_movie_seat_list.append(premium_movie_seat('[{}]'.format(k+1), premium_movie_list[i].name, row_number_list[j], k))

# ----------------------------------- < 좌석 상태 출력 및 체크 시스템 > ------------------------------------------------------------------

def print_family_movie_seat(movie_num): # 가족관 좌석상태 출력
    print('-' * 79)
    print('-                                영화좌석 선택                                -')
    print('-' * 79)
    print('{} 좌석상태 ([열] : 예매가능, [$] : 매진석)'.format(family_movie_seat_list[200*(movie_num-1)].movie_name))
    for i in range(0, 10):
        print()
        print('{}행'.format(row_number_list[9-i]), end=' ')
        for j in range(0, 20):
            print(family_movie_seat_list[200 * (movie_num-1)+20 * i + j].movie_state, end = ' ')
    print() # 줄바꿈
    print('-' * 44, end = '')
    print('스크린', end = '')
    print('-' * 44)
    return 0

def print_animation_movie_seat(movie_num): # 애니메이션관 좌석상태 출력
    print('-' * 79)
    print('-                                영화좌석 선택                                -')
    print('-' * 79)
    print('{} 좌석상태 ([열] : 예매가능, [$] : 매진석)'.format(animation_movie_seat_list[200*(movie_num-1)].movie_name))
    for i in range(0, 10):
        print()
        print('{}행'.format(row_number_list[9-i]), end=' ')
        for j in range(0, 20):
            print(animation_movie_seat_list[200 * (movie_num-1)+20 * i + j].movie_state, end = ' ')
    print() # 줄바꿈
    print('-' * 44, end = '')
    print('스크린', end = '')
    print('-' * 44)
    return 0

def print_premium_movie_seat(movie_num): # 프리미엄관 좌석상태 출력
    print('-' * 79)
    print('-                                영화좌석 선택                                -')
    print('-' * 79)
    print('{} 좌석상태 ([열] : 예매가능, [$] : 매진석)'.format(premium_movie_seat_list[200*(movie_num-1)].movie_name))
    for i in range(0, 10):
        print()
        print('{}행'.format(row_number_list[9-i]), end=' ')
        for j in range(0, 20):
            print(premium_movie_seat_list[200 * (movie_num-1)+20 * i + j].movie_state, end = ' ')
    print() # 줄바꿈
    print('-' * 44, end = '')
    print('스크린', end = '')
    print('-' * 44)
    return 0

def row_return(row_string): # 사용자가 입력한 문자를 행 번호로 바꿔주는 함수(아스키코드 값 사용)
    return abs(ord(row_string)-74)

def ticketing_family_movie_seat(movie_num, row, column): # 사용자가 입력한 자리가 판매되었는지 아닌지 판별 후 예매를 도와주는 시스템
    if family_movie_seat_list[200 * (movie_num-1) + 20 * row_return(row) + (column-1)].movie_state == '[$]':
        print('이미 판매된 자리입니다. 다른자리를 선택해주세요.')
        return 0
    else:
        family_movie_seat_list[200 * (movie_num-1) + 20 * row_return(row) + (column-1)].movie_state = '[$]'
        print('{}행 {}열 자리를 예매하셨습니다.'.format(row, column))
        family_movie_list[movie_num-1].extra_seat -= 1
        return 10000 + 1000 * movie_num + 100 * (row_return(row)) + column # 영화예매 정보 코드로 반환
        # 다섯자리 : 영화관 코드 + 영화 코드 + 행 코드 + 열 코드 두 자리

def ticketing_animation_movie_seat(movie_num, row, column):
    if animation_movie_seat_list[200 * (movie_num-1) + 20 * row_return(row) + (column-1)].movie_state == '[$]':
        print('이미 판매된 자리입니다. 다른자리를 선택해주세요.')
        return 0
    else:
        animation_movie_seat_list[200 * (movie_num-1) + 20 * row_return(row) + (column-1)].movie_state = '[$]'
        print('{}행 {}열 자리를 예매하셨습니다.'.format(row, column))
        animation_movie_list[movie_num-1].extra_seat -= 1
        return 20000 + 1000 * movie_num + 100 * (row_return(row)) + column

def ticketing_premium_movie_seat(movie_num, row, column):
    if premium_movie_seat_list[200 * (movie_num-1) + 20 * row_return(row) + (column-1)].movie_state == '[$]':
        print('이미 판매된 자리입니다. 다른자리를 선택해주세요.')
        return 0
    else:
        premium_movie_seat_list[200 * (movie_num-1) + 20 * row_return(row) + (column-1)].movie_state = '[$]'
        print('{}행 {}열 자리를 예매하셨습니다.'.format(row, column))
        premium_movie_list[movie_num-1].extra_seat -= 1
        return 30000 + 1000 * movie_num + 100 * (row_return(row)) + column



if __name__ == '__main__':
    print_family_movie_seat(1)
    print(ticketing_family_movie_seat(1,'F',16))
