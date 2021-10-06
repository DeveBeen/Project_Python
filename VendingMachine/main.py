# Python Vending Machine

machine_swich = 'Yes' # 기계 구동 스위치 값을 'Yes' 값으로 선언

while True: # 무한 반복문 설정

    if machine_swich == 'Yes': # 기계 구동 스위치 값이 'Yes' 일 시에 프로그램 다시 시작
        user_money = int(input('5000원 이하의 돈을 입력하여 주십시오.')) # 유저는 항상 큰 지폐 단위부터 돈을 입력한다 가정

        if user_money > 5000: # 만약 5000원 이상의 돈을 입력했을 시
            print('5000원 이하의 돈을 입력하여 주시길 바랍니다.')
            user_money = 0 # 투입 한 돈 값을 0으로 재설정

        else:
            # 초기 셋팅한 음료수 딕셔너리 출력 {name:cost} 형태

            while True: # 무한 반복문 설정
                user_drink = input('원하는 음료를 입력해 주시길 바랍니다.')

                if 음료딕셔너리.get(user_drink) == 'None': # 음료 딕셔너리 안에 음료가 존재하지 않을 때
                    print('{}는 자판기에 존재하지 않는 상품입니다. 다시 선택해주세요.'.format(user_drink))

                else:
                    print('{}를 선택하셨습니다.'.format(음료 딕셔너리.get(user_drink)))


    else: # 기계 구동 스위치 값이 'Yes'가 아니므로 잔돈 출력 후 반복문을 종료
        break
