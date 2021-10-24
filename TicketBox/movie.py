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
family_movie_name = ['형', '싱크홀', '백두산']
animation_movie_name = ['귀멸의칼날-무한열차', '하울의 움직이는 성', '겨울왕국2']
premium_movie_name = ['기생충', '도둑들', '태극기휘날리며']
family_movie_cost = [9900, 9900, 9900]
animation_movie_cost = [10900, 10900, 10900]
premium_movie_cost = [12900, 12900, 12900]

for i in range(0,3):
    family_movie_list.append(family_movie(i+1, family_movie_name[i], family_movie_cost[i], 200)) # 모든 class 3개 씩 리스트 설정
    animation_movie_list.append(animation_movie(i+1, animation_movie_name[i], animation_movie_cost[i], 200))
    premium_movie_list.append(premium_movie(i+1, premium_movie_name[i], premium_movie_cost[i], 200))

# ------------------------------------<영화 추가 함수>-------------------------------------------------

def family_movie_append(family_movie_list): # 입력받은 가족 영화 데이터 class 객체에 추가해주는 함수 (admin에서 사용)
    movie_name = input('추가할 영화의 제목을 입력하세요. : ')
    movie_cost = int(input('추가할 영화의 가격을 입력하세요. : '))
    family_movie_list.append(family_movie(len(family_movie_list)+1, movie_name, movie_cost, 200))
    return family_movie_list

def animation_movie_append(animation_movie_list): # 입력받은 애니메이션 영화 데이터 class 객체에 추가해주는 함수 (admin에서 사용)
    movie_name = input('추가할 영화의 제목을 입력하세요. : ')
    movie_cost = int(input('추가할 영화의 가격을 입력하세요. : '))
    animation_movie_list.append(animation_movie(len(animation_movie_list)+1, movie_name, movie_cost, 200))
    return animation_movie_list

def premium_movie_append(premium_movie_list): # 입력받은 프리미엄 영화 데이터 class 객체에 추가해주는 함수 (admin에서 사용)
    movie_name = input('추가할 영화의 제목을 입력하세요. : ')
    movie_cost = int(input('추가할 영화의 가격을 입력하세요. : '))
    premium_movie_list.append(premium_movie(len(premium_movie_list)+1, movie_name, movie_cost, 200))
    return premium_movie_list

# ------------------------------------<영화 제거 함수>-------------------------------------------------

def family_movie_delete(family_movie_list): # 입력받은 영화 번호에 해당하는 영화 제거 후 영화 번호 초기화
    for i in range(0, len(family_movie_list)):
        print('{}. {}|가격:{}₩|남은좌석:200/{}'.format(family_movie_list[i].menu_num, family_movie_list[i].name, family_movie_list[i].cost, family_movie_list[i].extra_seat))
    delete_movie = int(input('삭제할 영화 번호를 입력하세요. : '))
    del family_movie_list[delete_movie-1] # 원소 번호는 항상 영화 번호-1
    for j in range(0, len(family_movie_list)):
        family_movie_list[j].menu_num = j+1 # 메뉴에서 하나 빠졌으므로 넘버를 초기화 시켜준다.

def animation_movie_delete(animation_movie_list):# 입력받은 영화 번호에 해당하는 영화 제거 후 영화 번호 초기화
    for i in range(0, len(animation_movie_list)):
        print('{}. {}|가격:{}₩|남은좌석:200/{}'.format(animation_movie_list[i].menu_num, animation_movie_list[i].name, animation_movie_list[i].cost, animation_movie_list[i].extra_seat))
    delete_movie = int(input('삭제할 영화 번호를 입력하세요. : '))
    del animation_movie_list[delete_movie-1] # 원소 번호는 항상 영화 번호-1
    for j in range(0, len(animation_movie_list)):
        animation_movie_list[j].menu_num = j+1 # 메뉴에서 하나 빠졌으므로 넘버를 초기화 시켜준다.

def premium_movie_delete(premium_movie_list):# 입력받은 영화 번호에 해당하는 영화 제거 후 영화 번호 초기화
    for i in range(0, len(premium_movie_list)):
        print('{}. {}|가격:{}₩|남은좌석:200/{}'.format(premium_movie_list[i].menu_num, premium_movie_list[i].name, premium_movie_list[i].cost, premium_movie_list[i].extra_seat))
    delete_movie = int(input('삭제할 영화 번호를 입력하세요. : '))
    del premium_movie_list[delete_movie-1] # 원소 번호는 항상 영화 번호-1
    for j in range(0, len(premium_movie_list)):
        premium_movie_list[j].menu_num = j+1 # 메뉴에서 하나 빠졌으므로 넘버를 초기화 시켜준다.





if __name__ == '__main__':
    print('no')
