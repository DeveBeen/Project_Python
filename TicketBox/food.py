# 음식 기능

class cinema_food: # 음식 객체

    def __init__(self, menu_num, name, cost, stock):
        self.menu_num = menu_num
        self.name = name
        self.cost = cost
        self.stock = stock

#----------------------------------------- <초기설정> ----------------------------------------------

food_list = [1,2,3] # food 객체를 보관할 리스트 선언
food_name = ['팝콘', '콜라', '나쵸'] # food 초기데이터 입력
food_cost = [3000, 2000, 2500] # food 초기데이터 입력
food_stock = [30, 30, 5] # food 초기데이터 입력

for i in range(0, len(food_list)):
    food_list.append(cinema_food(food_list, food_name, food_cost, food_stock))

#----------------------------------------- <초기설정> ----------------------------------------------
