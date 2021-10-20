# 인터페이스 구성 기능 함수 모음

from movie import *

def user_select_service(): # 처음 서비스 선택을 하는 메뉴를 출력해주는 함수
    select_service = 0
    print('-' * 35)
    print('-           서비스 선택           -')
    print('-' * 35)
    print('1. 음식 구매')
    print('2. 영화관 예매')
    print('3. 상영정보')
    print('(종료를 원하시면 0번을 누르십시오.)')
    select_service = int(input('입력 : ')) # 1~3번은 영화관 선택, 0번은 종료
    return select_service # 유저가 선택한 값으로 반환

def movie_service(select_cinema):

    if select_cinema == 1:
        print('가족 영화관 함수 - 제작중')
    elif select_cinema == 2:
        print('애니메이션 영화관 함수 - 제작중')
    elif select_cinema == 3:
        print('프리미엄 영화관 함수 - 제작중')

if __name__ == '__main__':
    a = user_select_service()
