# 음료수 재고 관리 모듈

class drink_stock: # 음료수 재고 관리용 클래스 선언

    drink_kinds = 20

    def __init__(self, name, cost, num):
        self.name = name
        self.cost = cost
        self.num = num
        drink_stock.drink_kinds -= 1 # 음료수 종류를 20개로 고정하기 위해 개수가 하나 선언 될 때마다 -1씩 실행

drink = [] # 각각의 음료수 객체를 받을 리스트 생성
name=['청포도에이드', '아메리카노', '카페라떼', '카푸치노', '헤이즐넛아메리카노', '헤이즐넛라떼', '헤이즐넛카푸치노', '바닐라라떼', '카페모카', '화이트초코모카', '민트초코우유', '생수', '생수', '레쓰비', '레쓰비', '봉봉', '갈아먹는배', '코코팜', '아이스티', '식혜']
cost = [1500, 1000, 1200, 1400, 1200, 1400, 1600, 1500, 2000, 2100, 3400, 300, 300, 700, 700, 900, 1300, 1000, 1000, 800]
num = [15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15]

for i in range(0,20):
    drink.append(drink_stock(name[i],cost[i],num[i])) # 입력한 초기 자판기 정보 할당

def retouch(): # 수정 함수
    admin = int(input('관리자모드를 활성화 하였습니다. 관리자 code를 입력하세요.'))

    if admin == 7477:
        print('관리자님 환영합니다.')

        while True:
            option = int(input('몇 번 칸에 음료수 정보를 수정하기를 윈하십니까? : 1 ~ 20, 종료 : 0'))

            if option == 0:
                break
            else:
                drink[option-1].name = input()
                drink[option-1].cost = int(input())
                drink[option-1].num = int(input())

                print(drink[option-1].name, drink[option-1].cost, drink[option-1].num)
    else:
        print('잘못된 관리자 코드입니다. 관리자 모드를 다시 활성화 해주십시오.')
