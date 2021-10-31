# 영화 상영정보 관리




def family_movie_info(select_movie):
    if select_movie == 1:
        with open('./movie_info/family_movie_1.txt', 'r', encoding='UTF-8') as family_movie:
