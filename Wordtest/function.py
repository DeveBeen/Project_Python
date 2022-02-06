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

        append_day = int(input("Plese input day number that you want. (range : 1~30, End : 0) : "))

        if append_day == 0:
            break
        else:
            day_list.append(append_day) # 입력한 Day 수 리스트에 추가

    set_list = set(day_list) # 중복제거를 위해 set 변경
    day_list = sorted(list(set_list)) # 중복제거 후 다시 list 변경 후 순서대로 정렬

    return day_list

# -------------------------------------------------------------------------------------------------------------------------------

def word_extract(day_list): # 받은 시험 Day 리스트를 바탕으로 단어를 가져오는 함수

    for i in range(0, len(day_list)):
        for j in range(0, len(voca)):
            if int(voca[j]._day) == day_list[i]:
                test_day.append(day_list[i])
                test_word.append(voca[j]._word)
                test_mean.append(voca[j]._mean)

    for i in range(1, len(test_day)+1):
        test_num.append(i)

    return test_num

# -------------------------------------------------------------------------------------------------------------------------------

def create_code(type_random_list, correct_random_list, example_random_list, answer_random_list): # 문제 제작 난수들을 통합하여 최종 문제코드 난수를 리스트로 반환하는 함수

    test_code_list = [] # 반환시킬 리스트 생성

    for i in range(0, len(type_random_list)):

        cal_v = 0 # 계산 변수 초기화

        if correct_random_list[i] == 4:
            cal_v = int(type_random_list[i] * 100000000000000000 + correct_random_list[i] * 10000000000000000 + example_random_list[i][0] * 1000000000000 + example_random_list[i][1] * 100000000 + example_random_list[i][2] * 10000 + answer_random_list[i])
            test_code_list.append(cal_v)

        elif correct_random_list[i] == 3:
            cal_v = int(type_random_list[i] * 100000000000000000 + correct_random_list[i] * 10000000000000000 + example_random_list[i][0] * 1000000000000 + example_random_list[i][1] * 100000000 + answer_random_list[i] * 10000 + example_random_list[i][2])
            test_code_list.append(cal_v)

        elif correct_random_list[i] == 2:
            cal_v = int(type_random_list[i] * 100000000000000000 + correct_random_list[i] * 10000000000000000 + example_random_list[i][0] * 1000000000000 + answer_random_list[i] * 100000000 + example_random_list[i][1] * 10000 + example_random_list[i][2])
            test_code_list.append(cal_v)

        elif correct_random_list[i] == 1:
            cal_v = int(type_random_list[i] * 100000000000000000 + correct_random_list[i] * 10000000000000000 + answer_random_list[i] * 1000000000000 + example_random_list[i][0] * 100000000 + example_random_list[i][1] * 10000 + example_random_list[i][2])
            test_code_list.append(cal_v)
        else:
            print('Error')
            break

    return test_code_list

# -------------------------------------------------------------------------------------------------------------------------------

def k_shift_code(word_code): # 단어 코드를 받아 한국어로 변환 시켜주는 함수
    for i in range(0,len(test_num)):
        if test_num[i] == word_code:
            return test_mean[i]
            break

def e_shift_code(word_code): # 단어 코드를 받아 영어로 변환 시켜주는 함수
    for i in range(0,len(test_num)):
        if test_num[i] == word_code:
            return test_word[i]
            break

# -------------------------------------------------------------------------------------------------------------------------------

def question_discriminate(test_code_list): # 문제 코드를 받아 문제를 출력하는 함수

    user_select_example_list = [] # 사용자가 입력할 답 리스트를 선언

    for i in range(0, len(test_code_list)):

        user_select = ''

        print()
        print('-'*100)
        print()

        question_code = int(test_code_list[i] / math.pow(10,17))
        correct_code = int((test_code_list[i] -int(question_code * math.pow(10,17))) / math.pow(10,16))
        num_one_code = int((test_code_list[i] - int(question_code * math.pow(10,17)) - int(correct_code * math.pow(10,16))) / math.pow(10,12))
        num_two_code = int((test_code_list[i] - int(question_code * math.pow(10,17)) - int(correct_code * math.pow(10,16)) - int(num_one_code * math.pow(10,12))) / math.pow(10,8))
        num_three_code = int((test_code_list[i] - int(question_code * math.pow(10,17)) - int(correct_code * math.pow(10,16)) - int(num_one_code * math.pow(10,12)) - int(num_two_code * math.pow(10,8))) / math.pow(10,4))
        num_four_code = int(test_code_list[i] - int(question_code * math.pow(10,17)) - int(correct_code * math.pow(10,16)) - int(num_one_code * math.pow(10,12)) - int(num_two_code * math.pow(10,8)) - int(num_three_code * math.pow(10,4)))

        if question_code == 1: # 문제 타입이 1인 경우 -> 영어 단어를 보고 뜻을 고르는 문제 출력

            if correct_code == 1:
                print('No.{0} Select meaning of next eng_word in the example. - {1}'.format(i+1, e_shift_code(num_one_code)))
                print('ⓐ {}'.format(k_shift_code(num_one_code)))
                print('ⓑ {}'.format(k_shift_code(num_two_code)))
                print('ⓒ {}'.format(k_shift_code(num_three_code)))
                print('ⓓ {}'.format(k_shift_code(num_four_code)))
                print(test_code_list[i])
                user_select = str(input('Input your answer : '))
                user_select_example_list.append(user_select)
            elif correct_code == 2:
                print('No.{0} Select meaning of next eng_word in the example. - {1}'.format(i+1, e_shift_code(num_two_code)))
                print('ⓐ {}'.format(k_shift_code(num_one_code)))
                print('ⓑ {}'.format(k_shift_code(num_two_code)))
                print('ⓒ {}'.format(k_shift_code(num_three_code)))
                print('ⓓ {}'.format(k_shift_code(num_four_code)))
                print(test_code_list[i])
                user_select = str(input('Input your answer : '))
                user_select_example_list.append(user_select)
            elif correct_code == 3:
                print('No.{0} Select meaning of next eng_word in the example. - {1}'.format(i+1, e_shift_code(num_three_code)))
                print('ⓐ {}'.format(k_shift_code(num_one_code)))
                print('ⓑ {}'.format(k_shift_code(num_two_code)))
                print('ⓒ {}'.format(k_shift_code(num_three_code)))
                print('ⓓ {}'.format(k_shift_code(num_four_code)))
                print(test_code_list[i])
                user_select = str(input('Input your answer : '))
                user_select_example_list.append(user_select)
            elif correct_code == 4:
                print('No.{0} Select meaning of next eng_word in the example. - {1}'.format(i+1, e_shift_code(num_four_code)))
                print('ⓐ {}'.format(k_shift_code(num_one_code)))
                print('ⓑ {}'.format(k_shift_code(num_two_code)))
                print('ⓒ {}'.format(k_shift_code(num_three_code)))
                print('ⓓ {}'.format(k_shift_code(num_four_code)))
                print(test_code_list[i])
                user_select = str(input('Input your answer : '))
                user_select_example_list.append(user_select)
            else:
                print('Error')

        elif question_code == 2: # 문제 타입이 2인 경우 -> 뜻을 보고 영어단어를 고르는 문제 출력

            if correct_code == 1:
                print('No.{0} Select eng_word that include meaning of next word in the example. - {1}'.format(i+1, k_shift_code(num_one_code)))
                print('ⓐ {}'.format(e_shift_code(num_one_code)))
                print('ⓑ {}'.format(e_shift_code(num_two_code)))
                print('ⓒ {}'.format(e_shift_code(num_three_code)))
                print('ⓓ {}'.format(e_shift_code(num_four_code)))
                print(test_code_list[i])
                user_select = str(input('Input your answer : '))
                user_select_example_list.append(user_select)
            elif correct_code == 2:
                print('No.{0} Select eng_word that include meaning of next word in the example. - {1}'.format(i+1, k_shift_code(num_two_code)))
                print('ⓐ {}'.format(e_shift_code(num_one_code)))
                print('ⓑ {}'.format(e_shift_code(num_two_code)))
                print('ⓒ {}'.format(e_shift_code(num_three_code)))
                print('ⓓ {}'.format(e_shift_code(num_four_code)))
                print(test_code_list[i])
                user_select = str(input('Input your answer : '))
                user_select_example_list.append(user_select)
            elif correct_code == 3:
                print('No.{0} Select eng_word that include meaning of next word in the example. - {1}'.format(i+1, k_shift_code(num_three_code)))
                print('ⓐ {}'.format(e_shift_code(num_one_code)))
                print('ⓑ {}'.format(e_shift_code(num_two_code)))
                print('ⓒ {}'.format(e_shift_code(num_three_code)))
                print('ⓓ {}'.format(e_shift_code(num_four_code)))
                print(test_code_list[i])
                user_select = str(input('Input your answer : '))
                user_select_example_list.append(user_select)
            elif correct_code == 4:
                print('No.{0} Select eng_word that include meaning of next word in the example. - {1}'.format(i+1, k_shift_code(num_four_code)))
                print('ⓐ {}'.format(e_shift_code(num_one_code)))
                print('ⓑ {}'.format(e_shift_code(num_two_code)))
                print('ⓒ {}'.format(e_shift_code(num_three_code)))
                print('ⓓ {}'.format(e_shift_code(num_four_code)))
                print(test_code_list[i])
                user_select = str(input('Input your answer : '))
                user_select_example_list.append(user_select)
            else:
                print('Error')

        elif question_code == 3: # 문제 타입이 3인 경우 -> 뜻을 보고 영어단어를 쓰는 문제 출력

            if correct_code == 1:
                print('No.{0} Write eng_word that include meaning of next word. - {1}'.format(i+1, k_shift_code(num_one_code)))
                print(test_code_list[i])
                user_select = str(input('Input your answer : '))
                user_select_example_list.append(user_select)
            elif correct_code == 2:
                print('No.{0} Write eng_word that include meaning of next word. - {1}'.format(i+1, k_shift_code(num_two_code)))
                print(test_code_list[i])
                user_select = str(input('Input your answer : '))
                user_select_example_list.append(user_select)
            elif correct_code == 3:
                print('No.{0} Write eng_word that include meaning of next word. - {1}'.format(i+1, k_shift_code(num_three_code)))
                print(test_code_list[i])
                user_select = str(input('Input your answer : '))
                user_select_example_list.append(user_select)
            elif correct_code == 4:
                print('No.{0} Write eng_word that include meaning of next word. - {1}'.format(i+1, k_shift_code(num_four_code)))
                print(test_code_list[i])
                user_select = str(input('Input your answer : '))
                user_select_example_list.append(user_select)
            else:
                print('Error')

        else:
            print('Error')

    print(user_select_example_list)

    return user_select_example_list # 답지 확인을 위해 사용자가 선택한 답안지 리스트 반환

# -------------------------------------------------------------------------------------------------------------------------------

def convert_number(select_example): # 사용자가 입력한 문자를 숫자로 변형하여 채점 프로그램에서 사용할 함수

    if select_example == 'a':
        return 1
    elif select_example == 'b':
        return 2
    elif select_example == 'c':
        return 3
    elif select_example == 'd':
        return 4
    else:
        return 0

# -------------------------------------------------------------------------------------------------------------------------------

def grade_type3(test_code_list, user_select_example_list):

    question_code = int(test_code_list / math.pow(10,17))
    correct_code = int((test_code_list -int(question_code * math.pow(10,17))) / math.pow(10,16))
    num_one_code = int((test_code_list - int(question_code * math.pow(10,17)) - int(correct_code * math.pow(10,16))) / math.pow(10,12))
    num_two_code = int((test_code_list - int(question_code * math.pow(10,17)) - int(correct_code * math.pow(10,16)) - int(num_one_code * math.pow(10,12))) / math.pow(10,8))
    num_three_code = int((test_code_list - int(question_code * math.pow(10,17)) - int(correct_code * math.pow(10,16)) - int(num_one_code * math.pow(10,12)) - int(num_two_code * math.pow(10,8))) / math.pow(10,4))
    num_four_code = int(test_code_list - int(question_code * math.pow(10,17)) - int(correct_code * math.pow(10,16)) - int(num_one_code * math.pow(10,12)) - int(num_two_code * math.pow(10,8)) - int(num_three_code * math.pow(10,4)))

    if correct_code == 1:
        if e_shift_code(num_one_code) == user_select_example_list:
            return 1
        else:
            return 0
    elif correct_code == 2:
        if e_shift_code(num_two_code) == user_select_example_list:
            return 1
        else:
            return 0
    elif correct_code == 3:
        if e_shift_code(num_three_code) == user_select_example_list:
            return 1
        else:
            return 0
    elif correct_code == 4:
        if e_shift_code(num_four_code) == user_select_example_list:
            return 1
        else:
            return 0
    else:
        print('Error')
        return 0


# -------------------------------------------------------------------------------------------------------------------------------

def grade_exam(test_code_list, user_select_example_list): # 채점 후에 점수와 오답 문제 번호을 출력해주는 함수

    wrong_list = [] # 틀린문제 번호를 받을 리스트
    score = 0 # 점수

    for i in range(0,len(test_code_list)):

        question_code = int(test_code_list[i] / math.pow(10,17))
        correct_code = int((test_code_list[i] -int(question_code * math.pow(10,17))) / math.pow(10,16))

        if question_code == 3:
            if grade_type3(test_code_list[i], user_select_example_list[i]) == 1:
                score += int(1000/len(test_code_list))
            else:
                wrong_list.append(i+1)
        elif correct_code == convert_number(user_select_example_list[i]):
            score += int(1000/len(test_code_list)) # 1000점 만점 기준으로 맞을 때마다 +되는 형식
        else:
            wrong_list.append(i+1)

    print()
    print('-'*100)
    print()
    print('Your score : {} / 1000'.format(score))
    print('Your wrong question number : {}'.format(wrong_list))

    return 0






if __name__ == '__main__':
    add_day(day_list)
    word_extract(day_list)
    print(test_num)
    print(test_day)
    print(test_word)
    print(test_mean)
    print(create_code([1,1,1,1,1], [1,1,1,1,1], [[1,1,2], [1,1,3], [1,1,4], [1,1,5], [1,1,6]], [19,20,21,22,23]))
