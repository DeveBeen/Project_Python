# 영화 상영정보 관리
from movie import *

# ---------------------------------------- 영화 줄거리 출력 --------------------------------------------------------

def family_movie_info(select_movie): # 선택한 영화의 줄거리를 출력해주는 함수

    swich = 0 # 영화를 구변하기 위한 스위치 변수

    with open('./movie_info/family_movie.txt', 'r', encoding='UTF-8') as family_movie: # 가족 영화 줄거리가 써있는 텍스트 파일을 open
        lines = family_movie.readlines()
    lines = [line.rstrip('\n') for line in lines] # 엔터를 제거하고 리스트에 모든 요소를 한 줄 씩 넣어준다.

    print('-' * 79)
    print('-                                  영화 정보                                  -')
    print('-' * 79)

    for i in range(0, len(lines)):
        if select_movie < len(family_movie_list): # 범위 오류를 해결하기 위해서
            if lines[i] == family_movie_list[select_movie-1].name:
                swich = 1 # 만약 유저가 입력한 영화의 이름이 리스트안에 동일한 라인부터 스위치 on
            elif lines[i] == family_movie_list[select_movie].name:
                swich = 0 # 유저가 입력한 영화 정보를 모두 출력했으므로 스위치 off
        elif select_movie == len(family_movie_list):
            if lines[i] == family_movie_list[select_movie-1].name:
                swich = 1 # 마지막까지 출력하면 되므로 스위치 on

        if swich == 1:
            print(lines[i])

def animation_movie_info(select_movie): # 선택한 영화의 줄거리를 출력해주는 함수

    swich = 0 # 영화를 구변하기 위한 스위치 변수

    with open('./movie_info/animation_movie.txt', 'r', encoding='UTF-8') as animation_movie: # 애니메이션 영화 줄거리가 써있는 텍스트 파일을 open
        lines = animation_movie.readlines()
    lines = [line.rstrip('\n') for line in lines] # 엔터를 제거하고 리스트에 모든 요소를 한 줄 씩 넣어준다.

    print('-' * 79)
    print('-                                  영화 정보                                  -')
    print('-' * 79)

    for i in range(0, len(lines)):
        if select_movie < len(animation_movie_list): # 범위 오류를 해결하기 위해서
            if lines[i] == animation_movie_list[select_movie-1].name:
                swich = 1 # 만약 유저가 입력한 영화의 이름이 리스트안에 동일한 라인부터 스위치 on
            elif lines[i] == animation_movie_list[select_movie].name:
                swich = 0 # 유저가 입력한 영화 정보를 모두 출력했으므로 스위치 off
        elif select_movie == len(animation_movie_list):
            if lines[i] == animation_movie_list[select_movie-1].name:
                swich = 1 # 마지막까지 출력하면 되므로 스위치 on

        if swich == 1:
            print(lines[i])

def premium_movie_info(select_movie): # 선택한 영화의 줄거리를 출력해주는 함수

    swich = 0 # 영화를 구변하기 위한 스위치 변수

    with open('./movie_info/premium_movie.txt', 'r', encoding='UTF-8') as premium_movie: # 프리미엄 영화 줄거리가 써있는 텍스트 파일을 open
        lines = premium_movie.readlines()
    lines = [line.rstrip('\n') for line in lines] # 엔터를 제거하고 리스트에 모든 요소를 한 줄 씩 넣어준다.

    print('-' * 79)
    print('-                                  영화 정보                                  -')
    print('-' * 79)

    for i in range(0, len(lines)):
        if select_movie < len(premium_movie_list): # 범위 오류를 해결하기 위해서
            if lines[i] == premium_movie_list[select_movie-1].name:
                swich = 1 # 만약 유저가 입력한 영화의 이름이 리스트안에 동일한 라인부터 스위치 on
            elif lines[i] == premium_movie_list[select_movie].name:
                swich = 0 # 유저가 입력한 영화 정보를 모두 출력했으므로 스위치 off
        elif select_movie == len(premium_movie_list):
            if lines[i] == premium_movie_list[select_movie-1].name:
                swich = 1 # 마지막까지 출력하면 되므로 스위치 on

        if swich == 1:
            print(lines[i])


if __name__ == '__main__':
    family_movie_info(3)
    animation_movie_info(3)
    premium_movie_info(3)
