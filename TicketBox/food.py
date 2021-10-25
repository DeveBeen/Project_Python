# 음식 기능

class cinema_food: # 음식 객체

    def __init__(self, menu_num, name, cost, stock):
        self.menu_num = menu_num
        self.name = name
        self.cost = cost
        self.stock = stock

# ----------------------------------------- <초기 설정> ----------------------------------------------

food_list = [] # food 객체를 보관할 리스트 선언
food_name = ['팝콘', '콜라', '나쵸'] # food 초기데이터 입력
food_cost = [3000, 2000, 2500] # food 초기데이터 입력
food_stock = [30, 30, 5] # food 초기데이터 입력

for i in range(0, 3):
    food_list.append(cinema_food(i+1, food_name[i], food_cost[i], food_stock[i]))

# ----------------------------------------- <음식 추가 함수> ----------------------------------------------

def food_append(food_list): # 입력받은 음식 데이터를 객체에 추가시켜주는 함수
    name = input('추가할 음식을 입력하세요. : ')
    cost = int(input('추가할 음식의 가격을 입력하세요. : '))
    stock = int(input('재고를 입력해 주세요. : '))
    food_list.append(cinema_food(len(food_list)+1, name, cost, stock))
    return food_list

# ----------------------------------------- <음식 삭제 함수> ----------------------------------------------

def food_delete(food_list): # 입력받은 음식 번호에 해당하는 음식 제거 후 음식 번호 초기화 함수
    for i in range(0, len(food_list)):
        print('{}. {} | 가격 : {}₩'.format(food_list[i].menu_num, food_list[i].name, food_list[i].cost))
    delete_food = int(input('삭제할 음식의 메뉴 번호를 입력하세요. : '))
    del food_list[delete_food-1] # 원소 번호는 항상 음식번호-1
    for j in range(0, len(food_list)):
        food_list[j].menu_num = j+1 # 메뉴에서 하나 빠졌으므로 넘버를 초기화 시켜준다.

if __name__ == '__main__':
    food_append(food_list)
    for i in range(0, len(food_list)):
        print('{}. {} | 가격 : {}₩'.format(food_list[i].menu_num, food_list[i].name, food_list[i].cost))
