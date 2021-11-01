# 영화 상영정보 관리
from movie import *

def family_movie_info(select_movie): # 선택한 영화의 줄거리를 출력해주는 함수

    swich = 0 # 영화를 구변하기 위한 스위치 변수

    with open('./movie_info/family_movie.txt', 'r', encoding='UTF-8') as family_movie: # 가족 영화 줄거리가 써있는 텍스트 파일을 open
        lines = family_movie.readlines()
    lines = [line.rstrip('\n') for line in lines] # 엔터를 제거하고 리스트에 모든 요소를 한 줄 씩 넣어준다.

    for i in range(0, len(lines)):
        if lines[i] == family_movie_list.name[select_movie-1]:
            swich = 1 # 만약 유저가 입력한 영화의 이름이 리스트안에 동일한 라인부터 스위치 on
        elif lines[i] == family_movie_list.name[select_movie]:
            swich = 0 # 다음 영화가 나오면 스위치 off

        if swich == 1:
            print(lines[i])


if __name__ == '__main__':
    family_movie_info(1)
