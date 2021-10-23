# 관리자 기능

from movie import *

def admin_movie(): # 관리자가 선택한 종류 영화관을 관리해주는 함수 (영화 추가와 제거 기능이 존재)

    while True:

        admin_select = int(input('수정을 원하시는 관 번호를 입력해주세요.(종료 : 0) : '))

        if admin_select == 0:
            break

        elif admin_select == 1: # 관리자가 선택한 영화관이 가족 영화관인 경우

            while True:
                admin_option = int(input('가족 영화관 수정을 선택하셨습니다, 추가를 원하십니까 삭제를 원하십니까? (뒤로가기 : 0, 추가 : 1, 삭제 : 2) : '))

                if admin_option == 0:
                    break

                elif admin_option == 1:
                    family_movie_append(family_movie_list) # 영화 추가 함수 실행
                    for i in range(0, len(family_movie_list)): # 확인용 영화 객체 출력
                        print('{}. {}|가격:{}₩|남은좌석:200/{}'.format(family_movie_list[i].menu_num, family_movie_list[i].name, family_movie_list[i].cost, family_movie_list[i].extra_seat))

                elif admin_option == 2:
                    family_movie_delete(family_movie_list) # 영화 제거 함수 실행

                else:
                    print('입력형식이 잘못되었습니다.')

        elif admin_select == 2: # 관리자가 선택한 영화관 애니메이션 영화관인 경우

            while True:
                admin_option = int(input('애니메이션 영화관 수정을 선택하셨습니다, 추가를 원하십니까 삭제를 원하십니까? (뒤로가기 : 0, 추가 : 1, 삭제 : 2) : '))

                if admin_option == 0:
                    break

                elif admin_option == 1:
                    animation_movie_append(animation_movie_list) # 영화 추가 함수 실행
                    for i in range(0, len(animation_movie_list)): # 확인용 영화 객체 출력
                        print('{}. {}|가격:{}₩|남은좌석:200/{}'.format(animation_movie_list[i].menu_num, animation_movie_list[i].name, animation_movie_list[i].cost, animation_movie_list[i].extra_seat))

                elif admin_option == 2:
                    animation_movie_delete(animation_movie_list) # 영화 제거 함수 실행

                else:
                    print('입력형식이 잘못되었습니다.')

        elif admin_select == 3: # 관리자가 선택한 영화관이 프리미엄 영화관인 경우

            while True:
                admin_option = int(input('프리미엄 영화관 수정을 선택하셨습니다, 추가를 원하십니까 삭제를 원하십니까? (뒤로가기 : 0, 추가 : 1, 삭제 : 2) : '))

                if admin_option == 0:
                    break

                elif admin_option == 1:
                    premium_movie_append(premium_movie_list) # 영화 추가 함수 실행
                    for i in range(0, len(premium_movie_list)): # 확인용 영화 객체 출력
                        print('{}. {}|가격:{}₩|남은좌석:200/{}'.format(premium_movie_list[i].menu_num, premium_movie_list[i].name, premium_movie_list[i].cost, premium_movie_list[i].extra_seat))

                elif admin_option == 2:
                    premium_movie_delete(premium_movie_list) # 영화 제거 함수 실행

                else:
                    print('입력형식이 잘못되었습니다.')

        else: # 입력형태가 잘못된경우
            print('입력형식이 잘못되었습니다.')

# ---------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    admin_movie()
