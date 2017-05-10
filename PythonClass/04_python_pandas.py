# 문제
import pandas as pd

emp = pd.DataFrame.from_csv("C:\data\emp.csv")
empresult = emp.groupby(['deptno', 'job'])['sal'].sum()
print(empresult)

import pandas as pd

emp = pd.DataFrame.from_csv("C:\\data\\mit_ttt2.csv")

result1 = emp[(emp['PLAYER'] == 1) &
              (emp['C1'] == 1) &
              (emp['C2'] == 2) &
              (emp['C3'] == 1) &
              (emp['C4'] == 2) &
              (emp['C7'] == 1) &
              (emp['C9'] == 2) &
              (emp['C5'] + emp['C6'] + emp['C8'] == 1)]

result2 = result1.groupby(['C5', 'C6', 'C8'])['LEARNING_ORDER'].max()

print(result2)

# 문제 101. JONES 보다 더 많은 월급을 받는 사원들의 이름과 월급을 출력하시오
import pandas as pd

emp = pd.DataFrame.from_csv("C:\data\emp.csv")
empresult = emp.groupby(['deptno', 'job'])['sal'].sum()
print(empresult)

# 문제 103. 관리자인 사원들의 이름을 출력하시오
result = emp[['ename']][emp['empno']].isin(emp['mgr'])]
print(result)

# 문제 104.

import pandas as pd

emp = pd.DataFrame.from_csv("C:\data\mit_ttt2.csv")

result1 = emp[(emp['PLAYER'] == 1) &
(emp['C1'] == 1) &
(emp['C2'] == 2) &
(emp['C3'] == 1) &
(emp['C4'] == 2) &
(emp['C7'] == 1) &
(emp['C9'] == 2) &
(emp['C5'] + emp['C6'] + emp['C8'] == 1)]

result2 = result1.groupby(['C5', 'C6', 'C8'])['LEARNING_ORDER'].max()
result3 = emp[emp['LEARNING_ORDER'].isin(result2) & (emp['PLAYER'] == 1)]

print(result3)

dic = {}
dic['나는'] = ('I', 0)
dic['소년'] = ('boy', 2)
dic['이다'] = ('am', 1)
dic['피자를'] = ('pizza', 2)
dic['먹는다'] = ('eat', 1)
result = ''
input_kor = input('입력하세요.(나는 소년 이다 / 나는 피자를 먹는다) :')
input_list = input_kor.split(' ')
for i in range(len(input_list)):
    for
j in input_list:
if dic[j][1] == i:
    result = result + dic[j][0] + ' '
print(result)

import csv

smt_dic = {}
file = open("C:\data\smt_dic.csv", 'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    smt_dic[emp_list[1]] = (emp_list[3], emp_list[4])
smt_dic[emp_list[2]] = (emp_list[3], emp_list[4])
# print(smt_dic)
result = ''
input_kor = input('입력하세요 : ')
input_list = input_kor.split(' ')
for i in range(len(input_list)):
    for
j in input_list:
if int(smt_dic[j][1]) == i:
    result = result + smt_dic[j][0] + ' '
break
print(result)



