# 횟차 객체를 생성하여 각 횟차마다 등수 데이터를 저장

class rank_num: # 로또 시뮬레이션의 각 회차 객체 제작 class

    def __init__(self, round_num, rank1, rank2, rank3, rank4):

        self.round_num = round_num # 회차 번호 설정
        self.rank1 = rank1 # 회차별 1등 횟수
        self.rank2 = rank2 # 회차별 2등 횟수
        self.rank3 = rank3 # 회차별 3등 횟수
        self.rank4 = rank4 # 회차별 4등 횟수

lotto_info = [] # 회차별 로또 데이터를 받을 리스트 선언

def list_len(iteration_num): # 리스트의 정보를 보관한 리스트 자릿수 추가 함수
    for i in range(1, iteration_num + 1):
        lotto_info.append(rank_num(i,0,0,0,0))

# ------------------------연금복권-------------------------------------------------

class rank_pention_num:

    def __init__(self, pention_round_num, pention_rank1, pention_rank2, pention_rank3, pention_rank4):

        self.pention_round_num = pention_round_num # 연금복권 회차 번호 설정
        self.pention_rank1 = pention_rank1 # 연금복권 회차별 1등 횟수
        self.pention_rank2 = pention_rank2 # 연금복권 회차별 2등 횟수
        self.pention_rank3 = pention_rank3 # 연금복권 회차별 3등 횟수
        self.pention_rank4 = pention_rank4 # 연금복권 회차별 4등 횟수

pention_info = []

def pention_list_len(iteration_num):
    for i in range(1, iteration_num + 1):
        pention_info.append(rank_pention_num(i, 0, 0, 0, 0))

if __name__ == '__main__':
    lotto_info = []
    list_len(10)
    print(lotto_info)

    pention_info = []
    pention_list_len(10)
    print(pention_info)
