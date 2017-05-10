# 문제 71. a라는 비어있는 리스트 변수를 선언하고 input 명령어를 이용해서 a라는 리스트 변수에 추가할
# 요소를 물어보게 해서 요소가 추가되는 코드를 구현하시오
# emp 리스트에 추가할 요소를 입력하세요 ~ a

k = input('emp_list에 추가할 요소를 입력하세요')
emp_list = []
emp_list.append(k)
print(emp_list)

# 문제 72. emp_list에 추가된 요소를 삭제하는 코드를 구현하시오
k = input('emp_list에 삭제할 요소를 입력하세요')
emp_list = []
emp_list.remove(k)
print(emp_list)

# 문제 73. emp_list에 요소를 추가하고 삭제하고 갯수를 확인하는 코드를 구현하는데 아래와 같이
# 실행되게 하시오
# emp_list에 요소를 추가하려면 1번, 삭제하려면 2번, 갯수확인은 3번을 누르세요.
q = 0
b = ['b', 'a']
k = input('emp_list에 요소를 추가하려면 1번, 삭제하려면 2번, 갯수확인은 3번을 입력하세요.')

emp_list = []
for k in range(5):
    if q == 1:
        a = input('리스트에 추가할 요소를 입력하세요')
        emp_list.append(k)
    elif q == 2:
        a = input('리스트에서 삭제할 요소를 입력하세요')
        b.remove(a)
    elif q == 3:
        b = count(b)
print(b)

# 문제 74. 리스트 메소드 중에 sort를 이용해서 월급을 출력할때 높은 순으로 출력하시오
# 1. sal_list 라는 비어있는 리스트에 emp_list의 5번째 요소를 for loop로 담아낸다

import csv

sal_list = []

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    sal_list.append(emp_list[5])
print(sal_list)

# 2. 위의 코드를 이용해서 이름과 월급이 높은 순으로 나오게.. (점심시간 문제)

import csv

sal_list = []

file = open("C:\data\emp2.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    sal_list.append(int(emp_list[5]))
    sal_list.sort(reverse=True)

for i in sal_list:
    print(i)


# sorted 함수에서 비교 대상으로 사용할 대상 리턴
# int(data[5]) : int로 형변환한 월급
def salCheck(data):
    return int(data[5])


file = open("C:\data\emp2.csv", "r")
emp_csv = csv.reader(file)
emp_list = []
for i in emp_csv:
    emp_list.append(i)

emp_list_sorted = sorted(emp_list, reverse=True, key=salCheck)

for i in emp_list_sorted:
    print(i[1], i[5])


# 문제 75. 이름과 월급을 출력하는데 이름을 알파벳 순서로 출력
def nameCheck(data):
    return data[1]


file = open("C:\data\emp2.csv", "r")
emp_csv = csv.reader(file)
emp_list = []
for i in emp_csv:
    emp_list.append(i)

emp_list_sorted = sorted(emp_list, reverse=False, key=nameCheck)

for i in emp_list_sorted:
    print(i[1], i[5])


# 문제 76. 직업이 SALESMAN인 사원들의 이름, 입사일, 직업을 출력하는데 최근 입사 순으로
def hiredateCheck(data):
    return data[4]


file = open("C:\data\emp2.csv", "r")
emp_csv = csv.reader(file)
emp_list = []
for i in emp_csv:
    emp_list.append(i)

emp_list_sorted = sorted(emp_list, reverse=True, key=hiredateCheck)

for i in emp_list_sorted:
    if i[2] == 'SALESMAN':
        print(i[1], i[4], i[2])