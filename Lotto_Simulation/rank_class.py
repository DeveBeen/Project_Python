# 횟차 객체를 생성하여 각 횟차마다 등수 데이터를 저장

class rank_num: # 로또 시뮬레이션의 각 회차 객체 제작 class

    def __init__(self, lotto_num, rank1, rank2, rank3, rank4):

        self.lotto_num = lotto_num # 회차 데이터
        self.rank1 = rank1 # 회차별 1등 횟수
        self.rank2 = rank2 # 회차별 2등 횟수
        self.rank3 = rank3 # 회차별 3등 횟수
        self.rank4 = rank4 # 회차별 4등 횟수

lotto_info = [] # 회차별 로또 데이터를 받을 리스트 선언
