# 프로그램 가동 main 페이지

from function import *
from word import *
from randomfunction import *

while True:

    program_swich1 = int(input('Welcome to Happy_Been word test program!! Please pless anything number. (End : 0)'))

    if program_swich1 == 0:
        print('End the program.')
        break

    else:
        add_day(day_list) # 시험볼 Day 리스트 확인
        word_extract(day_list) # 단어 가져오기 함수

        question_count = int(input('Please select you want number of question.'))
        question_answer = answer_random_set(question_count) # 함수가 연속으로 실행되면 값이 난수 값으로 계속 변경되므로 변수에 각각 할당한다.
        question_type = type_random_set(question_count)
        question_correct = correct_random_set(question_count)
        question_example = example_random_set_list(question_count, question_answer)

        test_code_list = create_code(question_type, question_correct, question_example, question_answer)

        print()

        grade_exam(test_code_list,question_discriminate(test_code_list))

        break
