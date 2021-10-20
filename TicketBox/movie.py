# 영화정보 클래스 저장

class family_movie: # 가족 영화관 클래스

    def __init__(self, menu_num, name, cost, extra_seat): # 메뉴번호와 영화 제목, 가격, 남은 좌석 수를 받는 메소드
        self.menu_num = menu_num
        self.name = name
        self.cost = cost
        self.extra_seat = extra_seat

class animation_movie: # 애니메이션 영화관 클래스

    def __init__(self, menu_num, name, cost, extra_seat): # 메뉴번호와 영화 제목, 가격, 남은 좌석 수를 받는 메소드
        self.menu_num = menu_num
        self.name = name
        self.cost = cost
        self.extra_seat = extra_seat

class premium_movie: # 프리미엄 영화관 클래스

    def __init__(self, menu_num, name, cost, extra_seat): # 메뉴번호와 영화 제목, 가격, 남은 좌석 수를 받는 메소드
        self.menu_num = menu_num
        self.name = name
        self.cost = cost
        self.extra_seat = extra_seat

# ----------------------------------- <초기설정> -----------------------------------------
family_movie_list = []
animation_movie_list = []
premium_movie_list = []

for i in range(0,3):
    family_movie_list.append(family_movie(i, 0, 0, 200)) # 모든 class 3개 씩 리스트 초기화
    animation_movie_list.append(animation_movie(i, 0, 0, 200))
    premium_movie_list.append(premium_movie(i, 0, 0, 200))
# -------------------------------------------------------------------------------------


def family_movie_append(family_movie_list ,name, cost): # 입력받은 가족 영화 데이터 class 객체에 추가해주는 함수 (admin에서 사용)

        family_movie_list.append(family_movie(len(family_movie_list)+1, name, cost, 200))

def animation_movie_append(family_movie_list ,name, cost): # 입력받은 애니메이션 영화 데이터 class 객체에 추가해주는 함수 (admin에서 사용)

        animation_movie_list.append(animation_movie(len(animation_movie_list)+1, name, cost, 200))

def premium_movie_append(family_movie_list ,name, cost): # 입력받은 프리미엄 영화 데이터 class 객체에 추가해주는 함수 (admin에서 사용)

        premium_movie_list.append(premium_movie(len(premium_movie_list)+1, name, cost, 200))

if __name__ == '__main__':
    print('no')
