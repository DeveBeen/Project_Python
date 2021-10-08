# 각각의 지폐 및 동전 객체

ten_coin = [] # 10원 동전이 들어갈 리스트
fifty_coin = [] # 10원 동전이 들어갈 리스트
hundred_coin = [] # 10원 동전이 들어갈 리스트
fivehundred_coin = [] # 10원 동전이 들어갈 리스트
thousand_coin = [] # 10원 동전이 들어갈 리스트

for i in range(0, 50): # 모든 동전을 50개 씩 입력
    ten_coin.append(10)
    fifty_coin.append(50)
    hundred_coin.append(100)
    fivehundred_coin.append(500)
    thousand_coin.append(1000)

if __name__ == '__main__':
    print(len(ten_coin))
    print(len(fifty_coin))
    print(len(hundred_coin))
    print(len(fivehundred_coin))
    print(len(thousand_coin))

def input_money(money):
    thousand = int(money / 1000) # 유저가 입력한 금액의 돈을 각가의 지폐 또는 동전으로 개수화
    fivehundred = int((money - 1000 * thousand) / 500)
    hundred = int((money - 1000 * thousand - 500 * fivehundred) / 100)
    fifty = int((money - 1000 * thousand - 500 * fivehundred - 100 * hundred) / 50)
    ten = int((money - 1000 * thousand - 500 * fivehundred - 100 * hundred - 50 * fifty) / 10)

    for th in range(0, thousand): # 유저가 입력한 것을 자판기에 입력
        thousand_coin.append(1000)
    for fi in range(0, fivehundred):
        fivehundred_coin.append(500)
    for h in range(0, hundred):
        hundred_coin.append(100)
    for f in range(0, fifty):
        fifty_coin.append(50)
    for t in range(0, ten):
        ten_coin.append(10)

def out_money(money):
    thousand = int(money / 1000) # 남은 금액의 돈을 각가의 지폐 또는 동전으로 개수화
    fivehundred = int((money - 1000 * thousand) / 500)
    hundred = int((money - 1000 * thousand - 500 * fivehundred) / 100)
    fifty = int((money - 1000 * thousand - 500 * fivehundred - 100 * hundred) / 50)
    ten = int((money - 1000 * thousand - 500 * fivehundred - 100 * hundred - 50 * fifty) / 10)

    for th in range(0, thousand): # 남은 금액을 자판기에서 제외
        if len(thousand_coin) == 0: # 단, 자판기에서 더이상 줄 수 있는 지폐가 존재하지 않을 시, 그 아래 단위로 거슬러줌
            fivehundred += 2 * th
            break
        else:
            thousand_coin.pop()
    for fi in range(0, fivehundred):
        if len(fivehundred_coin) == 0:
            hundred += 5 * fi
            break
        else:
            fivehundred_coin.pop()
    for h in range(0, hundred):
        if len(hundred_coin) == 0:
            fifty += 2 * h
            break
        else:
            hundred_coin.pop()
    for f in range(0, fifty):
        if len(fifty_coin) == 0:
            ten += 5 * f
            break
        else:
            fifty_coin.pop()
    for t in range(0, ten):
        ten_coin.pop()

    return money

if __name__ == '__main__':
    print(input_money(1000))
    print(out_money(1660))
