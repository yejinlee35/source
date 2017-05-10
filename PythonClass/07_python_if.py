def my_abs(arg):
    if (arg <0):
        result = arg * -1
    else:
        result =arg
    return result
print(my_abs(-5))


def find_loc(var):
    import pandas as pd
    emp = pd.read_csv("c:\data\emp.csv")
    dept = pd.read_csv("c:\data\dept.csv")
    result = pd.merge(emp, dept, on='deptno')
    print(result[['loc']][result['ename'] == var])

print(find_loc('SMITH'))

# 문제147. 미분계수를 구하는 함수를 생성하는데 함수 f(x) = 2x + 1 일때
# x 가 -2 일때의 기울기(미분계수)를 구하시오 !

def mibun_fun(num):
    delta = 0.0001
    result = (2*(num+delta)*(num+delta)+1- (2*(num*num)+1))/delta
    print('x가',num,'일때 기울기는',result,'입니다')

print(mibun_fun(-2))

def numerical_diff(f,x):
    delta = 0.0001   #1e-4로 해도 된다.
    return (f(x+delta) - f(x-delta)) / (2*delta)

def function_1(x):
    return 2*pow(x,2) +1

print(numerical_diff(function_1,-2))

# 문제148. 함수 f(x) = x2 - x  + 5  함수의 x가 -2 일때의 미분계수를 구하시오!
def numerical_diff(f,x):
    delta = 0.0001   #1e-4로 해도 된다.
    return (f(x+delta) - f(x-delta)) / (2*delta)

def function_1(x):
    return pow(x,2) -x +5

print(numerical_diff(function_1,-2))

#예제.
def print_string(text, count=1):
    for I in range(count):
    print(text)

print_string("안녕하세요")
print_string("안녕하세요", 2)

#문제 149. 아래와 같이 이름만 넣으면 소속 팀과 직위가 출력되는 함수를 생성하시오

def print_inform(name, position='팀장', team='머신러닝팀'):
    print('이름={0}'.format(name))
    print('소속팀={0}'.format(team))
    print('직위={0}'.format(position))
#설명 : 문자열.format()

print_inform(name='장경원', position='팀장')
#이름 = 장경원
#소속팀 = 머신러닝팀
#직위 = 팀장

def merge_string(*text_list):
    result = ''
    for s in text_list:
        result = result + s + ' '
    return result
print(merge_string('아버지가', '방에','들어가신다'))

#문제 150. MIT TTT 코드에서 보드판을 출력하는 printboard 함수를 분석하시오
#(리스트 변수 내의 요소들을 뽑아내는 문법이 나온다)

# States as integer : manual coding
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
DRAW = 3
BOARD_FORMAT = """----------------------------
| {0} | {1} | {2} |
|--------------------------|
| {3} | {4} | {5} |
|--------------------------|
| {6} | {7} | {8} |
----------------------------"""
NAMES = [' ', 'X', 'O']

def printboard(state):
    """ Print the board from the internal state."""
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append(NAMES[state[i][j]].center(6))
    print(cells)
    print(*cells)
    print(BOARD_FORMAT.format(*cells))

printboard([[1,2,0],[2,1,2],[0,0,0]])
print(BOARD_FORMAT.format('a','b','c','d','e','f','g','h','g'))
print(BOARD_FORMAT.format('x','o','x','o','x',' ',' ',' ',' '))
print(BOARD_FORMAT.format('x'.center(6),'o','x','o','x',' ',' ',' ',' '))

#예제
def stop_fun(num):
    for i in range(1, num+1):
        print('숫자 {0} 을 출력합니다'.format(i))
        if i == 5:
            return
stop_fun(10)

#문제 151. (점심시간 문제) 아래와 같이 숫자를 입력하고 함수를 실행하면
# 숫자가 세로로 출력되게 하시오

def print_something(*num_list):
    for i in num_list:
        print(i)
print_something(1, 2, 3, 4, 5, 6, 7, 8, 9)

def scope_test():
    a = 1 #함수 내에서 사용하는 변수(로컬 변수)
    print('a:{0}'.format(a) )

scope_test()

a=0
scope_test()

#문제 152. 위의 스크립트에서 마지막 scope_test()를 실행했을 때 a가
# 0이 아니라 1이 출력되려면 scope_test()를 생성할때 어떻게 해야함?

def scope_test():
    global a #글로벌 변수로 선언한다.
    a = 1 #함수 내에서 사용하는 변수(로컬 변수)
    print('a:{0}'.format(a) )
scope_test()
a = 0
print('a:{0}'.format(a) )

#예 :
def some_func(count):
    if count > 0:
        print(count) # 쌓는것
        some_func(count -1)
    print(count)

print(some_func(10))

#문제 153. 10!를 재귀함수로 구현해서 출력하시오

print(factorial2(10))
########################

def factorial2(count):
    if count > 1:
        count *= factorial2(count -1)
    return count

print(factorial2(10))

#문제 154. 16과 20의 최대공약수를 출력하는데 재귀함수를 이용하시오
print(find_gcd(20,16))
최대공약수는 4

print(find_gcd(108, 72))
최대공약수는 36
---------------------------------
def find_gcd(num1, num2):
    num3 = num1 % num2  # 8, 4
    if num2%num3 == 0:  #12%8 = 4, 8%4=0
        return num3 #4
    else:
        find_gcd(num2, num3)

print('최대공약수는 ', find_gcd(24, 16))

#문제 155. 인자값을 3개를 받아서 최대공약수를 출력하시오 (재귀함수로 구현) (오늘의 마지막 문제)
#print(find(20, 16, 4))
#최대공약수는 4 입니다.

def gcd(num1, num2, num3):
    result = num1%num2%num3
    if result != 0:
        result = num1%num2%num3
        return gcd(num2, num3, result)
    else:
        return num3
print(gcd(100, 50, 20))