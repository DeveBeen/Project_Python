# 함수 모음집

import math
from word import *
from randomfunction import *

day_list = []
test_num = []
test_day = []
test_word = []
test_mean = []

def add_day(day_list): # 시험에 입력한 Day 수를 추가 해주는 함수

    while True:

        append_day = int(input("시험에 추가 할 Day수를 입력해주세요(입력:1~30, 종료:0) : "))

        if append_day == 0:
            break
        else:
            day_list.append(append_day) # 입력한 Day 수 리스트에 추가

    set_list = set(day_list) # 중복제거를 위해 set 변경
    day_list = sorted(list(set_list)) # 중복제거 후 다시 list 변경 후 순서대로 정렬

    return day_list

def word_extract(day_list): # 받은 시험 Day 리스트를 바탕으로 단어를 가져오는 함수

    for i in range(0, len(day_list)):
        for j in range(0, len(voca)):
            if int(voca[j]._day) == day_list[i]:
                test_day.append(day_list[i])
                test_word.append(voca[j]._word)
                test_mean.append(voca[j]._mean)

    for i in range(1,len(test_day)):
        test_num.append(i)

def create_code(type_random_list, correct_random_list, example_random_list, answer_random_list): # 문제 제작 난수들을 통합하여 최종 문제코드 난수를 리스트로 반환하는 함수

    test_code_list = [] # 반환시킬 리스트 생성

    for i in range(0, len(type_random_list)):

        cal_v = 0 # 계산 변수 초기화

        if correct_random_list[i] == 4:
            cal_v = type_random_list[i] * math.pow(10,17) + correct_random_list[i] * math.pow(10,16) + example_random_list[i][0] * math.pow(10,12) + example_random_list[i][1] * math.pow(10,8) + example_random_list[i][2] * math.pow(10,4) + answer_random_list[i]
            test_code_list.append(cal_v)

        elif correct_random_list[i] == 3:
            cal_v = type_random_list[i] * math.pow(10,17) + correct_random_list[i] * math.pow(10,16) + example_random_list[i][0] * math.pow(10,12) + example_random_list[i][1] * math.pow(10,8) + answer_random_list[i] * math.pow(10,4) + example_random_list[i][2]
            test_code_list.append(cal_v)

        elif correct_random_list[i] == 2:
            cal_v = type_random_list[i] * math.pow(10,17) + correct_random_list[i] * math.pow(10,16) + example_random_list[i][0] * math.pow(10,12) + answer_random_list[i] * math.pow(10,8) + example_random_list[i][1] * math.pow(10,4) + example_random_list[i][2]
            test_code_list.append(cal_v)

        elif correct_random_list[i] == 1:
            cal_v = type_random_list[i] * math.pow(10,17) + correct_random_list[i] * math.pow(10,16) + answer_random_list[i] * math.pow(10,12) + example_random_list[i][0] * math.pow(10,8) + example_random_list[i][1] * math.pow(10,4) + example_random_list[i][2]
            test_code_list.append(cal_v)
        else:
            print('Error')
            break

    return test_code_list

def decipher_code(test_code_list): # 문제 제작 코드를 읽고 해독하여 문제로 반환해주는 함수
    print('제작중')

def question_discriminate(test_code_list): # 문제 코드를 받아 문제를 출력하는 함수

    question_discriminate_code = 0 # 문제 코드 판별 변수 0으로 초기화

    for i in range(0,len(test_code_list)):
        question_discriminate_code = int(test_code_list[i] / math.pow(10,17))

        if question_discriminate_code == 1:
            print('{0}. 다음 단어의 뜻을 보기에서 선택하시오. 단어 : {1}'.format(i+1, 1))






if __name__ == '__main__':
    add_day(day_list)
    word_extract(day_list)
    print(test_num)
    print(test_day)
    print(test_word)
    print(test_mean)
    print(create_code([1,2,1,2,1,2], [1,2,3,4,1,2], [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]], [19,20,21,22,23,24]))
    print(english_word_code(110019000100020003))
