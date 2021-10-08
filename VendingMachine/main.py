# Python Vending Machine

from drink_class import *
from money_class import *

machine_swich = 'yes' # 기계 구동 스위치 값을 'yes' 값으로 선언
change = 0 # 거스름돈 변수선언 :만약 기계내에서 user_money에 거스름돈 변수가 더해지는 형식으로 가면 동전 개수에서 오류가 나므로 밖에서 선언 후 더해주는 방식

while True: # 무한 반복문 설정

    if machine_swich == 'yes': # 기계 구동 스위치 값이 'Yes' 일 시에 프로그램 다시 시작
        user_money = int(input('5000원 이하의 돈을 입력하여 주십시오. : ')) # 유저는 항상 큰 지폐 단위부터 돈을 입력한다 가정
        print('현재 입력하신 금액 : {}'.format(user_money + change))
        if user_money == 12345: # 관리자 활성 번호 12345가 입력되면 관리자모드 활성화
            retouch()

        elif user_money > 5000: # 만약 5000원 이상의 돈을 입력했을 시
            print('5000원 이하의 돈을 입력하여 주시길 바랍니다. : ')
            user_money = 0 # 투입 한 돈 값을 0으로 재설정

        else:
            input_money(user_money) # 유저의 돈이 자판기에 분류되어 들어감

            for i in range(0, 20):
                print('|{}-{}:{}원|'.format(i+1,drink[i].name,drink[i].cost), end='  ')
                i += 1
            user_drink = int(input('원하는 음료를 선택하여 주십시오 1 ~ 20 : '))

            if drink[user_drink-1].cost > user_money + change:
                print('입력하신 돈이 부족합니다.')
                out_money(user_money)

            else:
                if drink[user_drink-1].num == 0:
                    print('{}이(가) 매진되었습니다. 다른 음료를 선택해주시길 바랍니다.')
                    continue
                else:
                    print('{}이(가) 나왔습니다.'.format(drink[user_drink-1].name))
                    drink[user_drink-1].num -= 1
                    change = user_money - drink[user_drink-1].cost + change
                    machine_swich = input('자판기 사용을 계속 하시겠습니까? (사용 -> yes, 잔돈반환 -> 아무버튼) : ')


    else: # 기계 구동 스위치 값이 'Yes'가 아니므로 잔돈 출력 후 반복문을 종료
        print('거스름돈 {}원을 가져가 주십시오.'.format(out_money(change)))
        break
