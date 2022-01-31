# word 객체 생성

import csv # csv 파일을 딕셔너리 형으로 뽑아 올 것이기 때문에

num = []
day = []
word = []
mean = []
voca = []

with open('./word_text.csv', 'r') as wd: # csv파일 읽어오기 명령어
    reader = csv.DictReader(wd) # csv파일을 dict형으로 reader 할당

    for c in reader:
        num.append(c.get('Num')) # num list에 reader로 받아온 dict에 Key가 'Num'인 value 값 추가
        day.append(c.get('Day')) # day list에 reader로 받아온 dict에 Key가 'Day'인 value 값 추가
        word.append(c.get('Word')) # word list에 reader로 받아온 dict에 Key가 'Word'인 value 값 추가
        mean.append(c.get('Mean')) # mean list에 reader로 받아온 dict에 Key가 'Mean'인 value 값 추가

class vocabulary: # 단어 인식 개체 생성

    def __init__(self, num, day, word, mean): # voca 객체에 num,day,word,mean 인스턴스 객체를 추가
        self._num = num
        self._day = day
        self._word = word
        self._mean = mean

for i in range(0, len(num)):
    voca.append(vocabulary(num[i], day[i], word[i], mean[i]))

if __name__ == '__main__':

    for i in range(0,len(num)):
        print(voca[i]._num, voca[i]._day, voca[i]._word, voca[i]._mean)

    print('nomal operate!!')
