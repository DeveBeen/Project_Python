# 함수 모음집
from word import *
from random_sort import *

day_list = []
test_num = []
test_day = []
test_word = []
test_mean = []

def add_day(day_list): # 시험에 입력한 Day 수를 추가 해주는 함수

    while True:

        append_day = int(input("시험에 추가 할 Day 수를 입력해주세요(입력:1~30, 종료:0) : "))

        if append_day == 0:
            break
        else:
            day_list.append(append_day) # 입력한 Day 수 리스트에 추가

    set_list = set(day_list) # 중복제거를 위해 set 변경
    day_list = sorted(list(set_list)) # 중복제거 후 다시 list 변경 후 순서대로 정렬

    return day_list

def word_extract(day_list):

    for i in range(0, len(day_list)):
        for j in range(0, len(voca)):
            if int(voca[j]._day) == day_list[i]:
                test_day.append(day_list[i])
                test_word.append(voca[j]._word)
                test_mean.append(voca[j]._mean)

    for i in range(1,len(test_day)):
        test_num.append(i)

if __name__ == '__main__':
    add_day(day_list)
    word_extract(day_list)
    print(test_num)
    print(test_day)
    print(test_word)
    print(test_mean)
