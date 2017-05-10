# 문제 15. 이름과 직업을 출력하는데 소문자로 출력하시오
import csv

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1].lower(), emp_list[2].lower())

# 문제 16. (MIT TTT 코드 이해를 위한 중요 기초 문제)
# 이름을 출력하는데 소문자로 이름의 첫글자만 출력하시오

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1][0].lower())

# 문제 17. 이름의 두번째 철자부터 마지막까지 소문자로 출력하시오
file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1][1:].lower())


# 문제 18. 이름의 첫번째 글자는 대문자, 두번째부터는 소문자로 출력하시오
def initcap(val):
    return val[0].upper() + val[1:].lower()


import csv

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(initcap(emp_list[1]))

# 문제 19. 이름의 첫번째 철자부터 세번째 철자까지 출력하시오
file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1][0:3])


# 문제 20. 이름의 첫번째 철자부터 세번째까지 출력하는데 substr 함수를 만들어서 출력하시오
def substr(val, num1, num2):
    return val[num1 - 1:num2]


import csv

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(substr(emp_list[1], 1, 3))

# 문제 21. 이름과 월급을 출력할때, 월급 0 대신 *을 출력하시오
import csv

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1], emp_list[5].replace('0', '*'))

# 문제 22. 이름, 월급 출력할때, 월급 0-2를 *로 출력하시오
import re  # 정규식모듈 import
import csv

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1], re.sub('[0-2]', '*', emp_list[5]))

# 문제 23. 이름과 이름의 길이를 출력하시오
file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1], len(emp_list[1]))

# 문제 24. 아래의 split 함수의 예제를 수행하시오
file = 'a b c d e f g'
print(file.split(' '))

# 문제 25. 아래의 file 변수의 요소들을 리스트 변수로 담아내서 두번째 요소인 b만 출력해보시오
file = 'a b c d e f g'
a = file.split(' ')
print(a[1])

# 문제 26. 겨울왕국 대본을 공백을 구분으로 두고 나눠서 리스트 변수로 저장되게 하시오

file = open("C:\data\winter.txt", 'r')
for winter_list in file:
    a = winter_list.split(' ')
    print(a)

# 문제 27. (점심시간 문제) 위의 스크립트를 이용해서 겨울왕국 각 리스트 변수 안에 단어가 몇 개가 있는지
# 아래와 같이 출력하시오

file = open("C:\data\winter.txt", 'r')
for winter_list in file:
    a = winter_list.split(' ')
    print(len(a))
# 겨울왕국 전체 단어 개수
sum_cnt = 0

file = open("C:\data\winter.txt", 'r')
for winter_list in file:
    sum_cnt += len(winter_list.split(' '))
print(sum_cnt)

a = 'Hello'
b = a.count('1')  # a 변수에서 1이 몇 개 있는가?
print(b)
# count 함수
c = ['anna', 'elsa', 'anna', 'elsa']
d = c.count('elsa')
print(d)

# 문제 29. 겨울왕국 대본에는 elsa가 몇 번 나오는지 카운트 하시오
sum = 0

file = open("C:\data\winter.txt", 'r')
for winter_list in file:
    a = winter_list.split(' ')
    sum = sum + a.count('Elsa')
print(sum)

# 문제 30. emp.csv.에서 14개의 리스트 변수 중에 5번째 요소(월급) 부분만
# 담아서 리스트 변수로 아래와 같이 생성하시오 !
# 함수 : append() : 기존의 리스트 변수에 추가하는 함수
######################
a = [1, 2, 3]
a.append(4)
print(a)

b = []
b.append(1)
b.append(2)
b.append(3)
print(b)
######################
sal = []

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    sal.append(emp_list[5])
print(sal)

# 문제 31. 겨울왕국 대본을 단어별로 출력하시오
['anna', 'elsa', 'she', 'you']

a = ['anna', 'elsa', 'she', 'you', 'orders']
for i in a:
    print(i)

file = open("C:\data\winter.txt", 'r')
for winter_list in file:
    a = winter_list.split(' ')  # 스크립트 -> 리스트 변수
    # print(a)
    for i in a:
        print(i)

# 문제 32. 위의 출력된 단어들을 하나의 list 변수에 담으시오 : append 함수(p.102)
b = []
file = open("C:\data\winter.txt", 'r')
for winter_list in file:
    a = winter_list.split(' ')  # 스크립트 -> 리스트 변수
    for i in a:
        b.append(i)
print(b)

# 문제 33. 출력된 단어들 중에 \n은 잘라내시오
win = []
file = open("C:\data\winter.txt", 'r')
for winter_list in file:
    a = winter_list.split(' ')  # 스크립트 -> 리스트 변수
    for i in a:
        b = i.strip('\n')
        print(win.append(b))
print(win)

# 문제 34. rpad 함수를 생성하고 아래와 같이 실행하시오
# 월급을 출력할 때 전체 10자리를 잡고 남은 왼쪽에 *을 채워 넣으시오
# 함수 : .ljust(), .rjust(),

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1].ljust(10), emp_list[5].rjust(10, '*'))


def rpad(var, num, val):
    for _ in range(num - len(var)):
        var = var + val
    return (var)


file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1], rpad(emp_list[5], 10, '*'))


# 문제 35. instr 함수를 파이썬으로 구현하시오
def instr(word, target):
    for i in range(len(word)):
        if word[i] == target:
            return i + 1


word = 'smith'
result = instr(word, 'm')
print(result)
############################
word = 'smith'
print(word[1])


# 문제36. 이름, 이름에 M 자가 몇 번째 자리에 있는지 출력하시오
def instr(word, target):
    for i in range(len(word)):
        if word[i] == target:
            return i + 1


import csv

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1], instr(emp_list[1], 'M'))

# 문제37. 이름, 월급, 보너스를 출력하는데 보너스는 월급의 15%로 출력하시오
# 함수 : round 함수

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1], emp_list[5], int(emp_list[5]) * 0.15)

# 문제 38. 위의 결과를 다시 출력하는데 컬럼명도 출력되게 하시오
# 함수 : round
file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
print('이름', '월급', '보너스')
for emp_list in emp_csv:
    print(emp_list[1], emp_list[5], int(emp_list[5]) * 0.15)

# 문제39. 보너스의 소숫점을 반올림하시오
file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
print('이름', '월급', '보너스')
for emp_list in emp_csv:
    print(emp_list[1], emp_list[5], round(int(emp_list[5]) * 0.15))

# 문제 40. 보너스를 출력할때 소숫점 이하를 잘라내시오
import math

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
print('이름', '월급', '보너스')
for emp_list in emp_csv:
    print(emp_list[1], emp_list[5], math.trunc(int(emp_list[5]) * 0.15))

# 문제 41. input 명령어를 이용해서 숫자를 입력받아 해당숫자가 짝수/홀수인지 판단하시오
# 연산자 : %

a = int(input('숫자를 입력하세요'))

if a % 2 == 0:
    print('짝수입니다')
else:
    print('홀수입니다')

# 설명 : :-> 사용하는 경우 (if 문, for loop/while loop 문, def 함수 문)

# 문제 42. power 함수를 이용해서 아래의 프로그램을 구현하시오

a = int(input('숫자를 입력하세요'))
b = int(input('지수를 입력하세요'))
result = math.pow(a, b)
import math

print(result)

# 문제 43. 오늘의 날짜를 출력하시오
import datetime

today = datetime.date.today()
print(today)

# 또는
from datetime import date

print(date.todday())

# 문제 44. 오늘부터 세 달 뒤의 날짜를 출력하시오
# 함수 : add_months vs. relativedelta
import datetime
import csv

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    a = datetime.datetime.strptime(emp_list[4], '%Y-%m-%d')  # 문자를 날짜로 변환해주는 작업
    print(emp_list[1], emp_list[4], a + relativedelta(months=+3))

# 문제 46. 올해 2월달의 마지막 날짜를 출력하시오
from calendar import monthrange

print(monthrange(2017, 2))

# 문제 47. 오늘부터 요번달 말일까지 총 몇일 남았는지 출력하시오
from calendar import monthrange
from datetime import date

print(monthrange(2017, 4)[1])
print(date.today().day)
print(monthrange(2014, 4)[1] - date.today().day)
# 설명 : today().day 일, today().month 달, today().year 연도

# 문제 48. 오늘이 무슨 요일인지 출력하시오
# 함수 : next_day vs. 사용자정의함수
import daytime

print(date.today())  # 오늘 날짜 확인
print(date.today().weekday())

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
print(days[0])

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
print(days[date.today().weekday()])

# 문제 49. 이름, 입사요일을 출력하시오
import datetime
import csv

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    a = datetime.datetime.strptime(emp_list[4], '%Y-%m-%d')  # 문자를 날짜로 변환해주는 작업
    print(emp_list[1], days[a.weekday()])

# 문제 50. 오늘날짜에서 하루를 더한 날짜가 어떻게 되는가?
import datetime

print(date.today() + datetime.timedelta(days=1))


# 문제 51. 아래와 같이 실행될 수 있는 사용자 정의함수를 생성하시오
def next_day(val1, val2):
    return (val1 + datetime.timedelta(days=val2))


print(next_day(date.today(), 1))


# 문제 52. 아래와 같이 실행될 수 있는 사용자 정의함수를 생성하시오
def next_day(val1, val2):
    d = datetime.datetime.strptime(val1, '%Y-%m-%d')
    return (d + datetime.timedelta(days=val2))


print(next_day('2017-04-17', 1))


# 문제 53. 아래와 같이 수행하면 지정된 날짜에서 돌아오는 요일의 날짜가 출력되게 하시오
# 수행 : print( next_day('2017-04-17', '화요일'))
def next_day(val1, val2):
    dic = {}
    dic['월요일'] = 0
    dic['화요일'] = 1
    dic['수요일'] = 2
    dic['목요일'] = 3
    dic['금요일'] = 4
    dic['토요일'] = 5
    dic['일요일'] = 6
    c = dic[val2]
    d = datetime.datetime.strptime(val1, '%Y-%m-%d')
    return (d + datetime.timedelta(days=c))


print(next_day('2017-04-17', '화요일'))


################################
def next_day(toDay, wod):
    wods = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    diff = wods.index(wod) - toDay.weekday()
    return toDay + datetime.timedelta(days=diff) if diff > 0 else toDay + datetime.timedelta(days=7 + diff)


print(next_day(datetime.datetime.today().date(), '월요일'))

# 문제 54. 이름, 입사일로부터 오늘까지 총 몇 일 근무했는지 출력하시오
import datetime
import csv

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    a = datetime.datetime.strptime(emp_list[4], '%Y-%m-%d')  # 문자를 날짜로 변환해주는 작업
    print(emp_list[1], datetime.datetime.today() - a)

# 문제 55. if 문을 이용해서 사원번호가 7788인 사원의 이름과 월급을 출력하시오
import csv

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if int(emp_list[0]) == 7788:
        print(emp_list[1], emp_list[5])

# 문제 56.월급이 3000 이상인 사원들의 이름과 월급을 출력하시오
import csv

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if int(emp_list[5]) >= 3000:
        print(emp_list[1], emp_list[5])

# 문제 57. 1981년 11월 17일에 입사한 사원의 이름과 입사일을 출력하시오
import csv

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if emp_list[4] == '1981-11-17':
        print(emp_list[1], emp_list[4])

# 문제 58. (TTT 프로그램을 이해하는데 중요한 문제) 1981년도에 입사한 사원들의 이름과 입사일을 출력하시오
import csv

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if emp_list[4][2:4] == '81':
        print(emp_list[1], emp_list[4])

# 문제 59. 아래의 리스트 변수에서 positive 라는 단어는 몇개가 나오는가?
# 연산자 : in
# 단어 1개만 비교 :
word = ['winter', 'positive', 'negative', 'cold']
sum = 0
for i in word:
    if 'positive' == i:
        sum = sum + 1
print(sum)

# 문제 60. 아래의 리스트 변수에서 positive와 negative 단어가 몇개 포함되어 있는지 알아보시오
# 연산자 : in
# 단어 여러개 비교 :
word = ['winter', 'positive', 'negative', 'cold']
sum = 0
for i in word:
    if i in ('positive', 'negative'):
        sum = sum + 1
print(sum)

# 문제 61. 겨울왕국 대본에는 긍정적인 단어가 몇 개나 들어있는가? (오늘의 마지막 문제)
import csv

file = open("C:\data\positive-words.csv", 'r')
positive_words = csv.reader(file)
# for positive_list in positive_words:
#   print(positive_list)

file = open("C:\data\winter.txt", 'r')
b = []
for winter_list in file:
    a = winter_list.split(' ')
    for i in a:
        i = i.strip('\n')
        i = i.strip('"')
        i = i.strip('.')
        i = i.strip(',')
        i = i.strip('!')
        i = i.strip('?')
        i = i.strip(':')
        i = i.strip(')')
        i = i.strip('(')
        i = i.lower()
        b.append(i)
sum = 0

for k in b:
    if k in positive_list:
        sum += 1
print(sum)

# 문제 62. 직업이 SALESMAN이고 월급이 1200 이상인 사원들의 이름과 직업과 월급을 출력하시오
import csv

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if (int(emp_list[5]) >= 1200) & (emp_list[2] == 'SALESMAN'):
        print(emp_list[1], emp_list[2], emp_list[5])

# 문제 63. 월급이 1000에서 3000 사이인 사원들의 이름과 월급을 출력하시오
import csv

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if (int(emp_list[5]) >= 1000) & (int(emp_list[5]) <= 3000):
        print(emp_list[1], emp_list[5])

# 문제 64. 직업이 ANALYST, CLERK 인 사원들의 이름과 월급과 직업을 출력하시오
import csv

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if (emp_list[2] == 'ANALYST') | (emp_list[2] == 'CLERK'):
        print(emp_list[1], emp_list[2], emp_list[5])

# 문제 65. 직업이 ANALYST, CLERK이 아닌 사원들의 이름과 월급과 직업을 출력하시오
import csv

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if emp_list[2] not in ('ANALYST', 'CLERK'):
        print(emp_list[1], emp_list[2], emp_list[5])

# 문제 66. 커미션이 null 인 사원들의 이름과 커미션을 출력하시오
# 연산자 : is null
import csv

file = open("C:\data\emp_comm.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if emp_list[6] == '':
        print(emp_list[1], emp_list[6])

# 문제 67. 커미션이 null이 아닌 사원들의 이름과 커미션을 출력하시오
import csv

file = open("C:\data\emp_comm.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if emp_list[6] != '':
        print(emp_list[1], emp_list[6])

# 문제 68. 이름의 첫번째 철자가 S로 시작하는 사원들의 이름과 월급을 출력하시오
# 연산자 : like
import csv

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if emp_list[1][0:1] == 'S':
        print(emp_list[1], emp_list[5])

# 문제 69. 이름의 두번째 철자가 M인 사원들의 이름, 월급 출력
import csv

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if emp_list[1][1:2] == 'M':
        print(emp_list[1], emp_list[5])

# 문제 70. 이름의 마지막 철자가 H인 사원들의 이름과 월급을 출력하시오
import csv

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if emp_list[1][-1] == 'H':
        print(emp_list[1], emp_list[5])

a = ['김', '이', '최']
print(type(a))
print(a)
print(a[0])