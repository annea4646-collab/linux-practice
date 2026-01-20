''' Exception '''
#error_make.py
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."
    
def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)


''' 파이썬 내장(built-in) 함수 '''

''' abs(x) :절대값 리턴 '''
# >>> abs(3)
# 3
# >>> abs(-3)
# 3
# >>> abs(-1.2)
# 1.2

''' all(x): x 요소가 모두 참이면 True, 하나라도 거짓이면 False '''
# >>> all([1,2,3])
# True
# >>> all([1,2,3,0])
# False
# >>> all([])                   # 리스트가 비어있어 거짓인 요소가 하나도 없음(공허한 참)
# True

def custom_all(iterable):
    for element in iterable:
        if not element:
            return False      # 거짓인 요소를 찾으면 즉시 False 반환
    return True               # 반복문이 끝날때까지 False가 없으면 True 반환
print(custom_all([]))

''' any(x): x 요소가 하나라도 참이면 True, 모두 거짓이면 False '''
# >>> any([1,2,3,4])
# True
# >>> any([0,""])
# False
# >>> any([1,2,3,0])
# True
# >>> any([])                   # 참인 요소가 하나도 없음
# False

def custom_any(iterable):
    for element in iterable:
        if element:
            return True     # 참의 요소를 찾으면 즉시 True 반환
    return False            # 반복문이 끝날때까지 참을 못찾으면 False 반환
print(custom_any([]))


''' chr(i) : 유니코드 값을 받아 해당하는 문자 리턴 '''
# >>> chr(97)
# 'a'
# >>> chr(44032)
# '가'

''' dir(x) : 객체가 지닌 변수가 함수를 보여주는 함수 '''
# >>> dir([1,2,3])
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# >>> dir({'1':'Test'})
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']


''' divmod(a,b) : a를 b로 나눈 몫과 나머지는 듀플로 리턴 '''
# >>> divmod(7,3)
# (2, 1)

# >>> 7//3
# 2
# >>> 7%3
# 1

''' enumerate(x) : 순서가 있는 데이터(list, tuple, str)를 입력받아 인덱스값을 포함하는 enumerate 객체 리턴'''
# >>> for i, name in enumerate(['body', 'foo', 'bar']):
# ...     print(i, name)

# 0 body
# 1 foo
# 2 bar

''' eval(expression) : 문자열로 구성된 표현식을 입력받아 실행 결과값 리턴'''
# >>> eval('1 + 2')
# 3
# >>> eval("'hi' + 'a'" )
# 'hia'
# >>> eval('divmod(4, 3)')
# (1, 1)



''' filter(f, iterable)     : filter(함수, 반복가능한데이터) '''
# positive.py
def positive(I):
    result = []
    for i in I:
        if i > 0:
            result.append(i)
    return result
    
print(positive([1,-3,2,0,-5,6]))                            # [1, 2, 6]


# filter1.py
def positive(x):
    return x > 0

print(list(filter(positive,[1,-3,2,0,-5,6])))               # [1, 2, 6]

''' using lambda '''
print(list(filter(lambda x: x>0, [1,-3,2,0,-5,6])))         # [1, 2, 6]


''' hex(x) : 16진수(hexadecimal) 문자열로 리턴 '''
# hex(234)
# hex(3)

''' id(object) : 고유주소값 리턴 '''
# >>> a=3
# >>> id(3)
# 140721253544808
# >>> b=a
# >>> id(b)
# 140721253544808
# >>> id(4)
# 140721253544840

''' input([prompt])'''
# >>> a=input()
# hi
# >>> a
# 'hi'
# >>> b=input('enter: ')
# enter: hi
# >>> b

''' int(x) : 문자열 형태의 숫자나 소수점이 있는 숫자를 정수로 리턴 '''
# >>> int('3')
# 3
# >>> int(3.4)
# 3

''' isinstance(object, class) : 입력받은 객체가 그 클래스의 인스턴스인지 판단 '''
# >>> class Person : pass
# ... 
# >>> a = Person()
# >>> isinstance(a, Person)
# True
# >>> b=3
# >>> isinstance(b, Person)
# False


''' len(s) : length 약자 '''
# >>> len("Python")
# 6
# >>> len([1,2,3])
# 3
# >>> len((1, 'a'))
# 2

''' list(iterable) '''
# >>> list("python")
# ['p', 'y', 't', 'h', 'o', 'n']
# >>> list((1,2,3))
# [1, 2, 3]
# >>> a=[1,2,3]
# >>> b=list(a)
# >>> b
# [1, 2, 3]

''' map(f,iterable) '''
# >>> def two_times(x):
# ...     return x*2
# ... 
# >>> list(map(two_times, [1,2,3,4]))
# [2, 4, 6, 8]


''' max(iterable) '''
# >>> max([1,2,3])
# 3
# >>> max("python")         # 문자열의 경우 유니코드 값이 가장 큰 문자 리턴
# 'y'

''' min(iterable) '''
# >>> min([1,2,3])
# 1
# >>> min("python")
# 'h'

''' oct(x) '''
# >>> oct(34)
# '0o42'
# >>> oct(12345)
# '0o30071'

'''open(filename, [mode])'''
# >>> f = open("binary_file", "rb")

''' 문자열(str) 타입 '''
s='안녕하세요'
print(type(s))
# <class 'str'>

''' 바이트(bytes) 타입 '''
b=b"Hello"
print(type(b))
# <class 'bytes'>

''' 변환 방법 '''
s="안녕하세요"
b= s.encode('utf-8')
print(b)                            # b'\xec\x95\x88\xeb\x85\x95\xed\x95\x98\xec\x84\xb8\xec\x9a\x94'

s2 = b.decode('utf-8')
print(s2)                           # 안녕하세요

''' 영어 파일을 바이너리로 읽을 때 '''
with open('D:\\doit\\note\\english.txt', 'rb') as f:
    data = f.read()
print(data)                         # b'Rivers know this : there is no hurry. We shall get there someday.'


''' 한글 파일을 바이너리로 읽을 때 '''

with open('D:\\doit\\note\\korean.txt', 'rb') as f:
    data = f.read()
print(data)                         # b'\xea\xb0\x95\xeb\xac\xbc\xec\x9d\x80 \xec\x95\x8c\xea\xb3\xa0 \xec\x9e\x88\xec\xa7\x80\xec\x9a\x94. \xec\x84\x9c\xeb\x91\x90\xeb\xa5\xbc \xed\x95\x84\xec\x9a\x94\xea\xb0\x80 \xec\x97\x86\xeb\x8b\xa4\xeb\x8a\x94 \xea\xb2\x83\xec\x9d\x84. \xec\x9a\xb0\xeb\xa6\xac\xeb\x8a\x94 \xec\x96\xb8\xec\xa0\xa0\xea\xb0\x80 \xeb\x8f\x84\xec\xb0\xa9\xed\x95\xa0\xea\xb1\xb0\xeb\x8b\x88\xea\xb9\x8c.'

with open('D:\\doit\\note\\korean.txt', 'rb') as f:
    data = f.read()
    text = data.decode('utf-8')         
print(text)                         # 강물은 알고 있지요. 서두를 필요가 없다는 것을. 우리는 언젠가 도착할거니까.


''' ord(c): 문자의 유니코드 숫자 값을 리턴 '''
# >>> ord('a')
# 97
# >>> ord('가')
# 44032


''' range([start,] stop [,step]) : 반복 가능한 객체로 만들어 리턴'''
# >>> list(range(5))                            # 인수가 하나일 경우 / range 함수는 0부터 시작
# [0, 1, 2, 3, 4]
# >>> list(range(5, 10))                        # 인수가 2개일 경우 / 끝 숫자는 해당 범위에 포함되지 않음
# [5, 6, 7, 8, 9]
# >>> list(range(1, 10, 2))                     # 인수가 3개일 경우 / 세번째 인수는 숫자 사이의 거리
# [1, 3, 5, 7, 9]
# >>> list(range(0, -10, -1))
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]


''' round(number[, ndigits]) : 반올림, [소수점 자리수] '''
# >>> round(4.6)
# 5
# >>> round(4.2)
# 4
# >>> round(5.678, 2)
# 5.68


''' sorted(iterable) '''
# >>> sorted([3,1,2])
# [1, 2, 3]
# >>> sorted("zero")
# ['e', 'o', 'r', 'z']


''' str(object) '''
# >>> str(3)
# '3'
# >>> str('hi')
# 'hi'

''' sum(object) '''
# >>> sum([1,2,3])
# 6
# >>> sum((4,5,6))
# 15

''' tuple(iterable) : 반복 가능한 데이터를 튜플로 리턴 '''
# >>> tuple('abc')
# ('a', 'b', 'c')
# >>> tuple([1,2,3])
# (1, 2, 3)
# >>> tuple((1,2,3))
# (1, 2, 3)


''' type(object)'''
# >>> type('abc')
# <class 'str'>                     <- 'abc'는 문자열 자료형
# >>> type([])
# <class 'list'>                    <- []는 리스트 자료형
# >>> type(open("test", "w")) 
# <class '_io.TextIOWrapper'>       <- 파일 자료형


''' zip(*iterable) : 각 개체의 동일한 인덱스에 있는 요소들을 하나씩 묶음 '''
# >>> list(zip([1,2,3],[4,5,6]))
# [(1, 4), (2, 5), (3, 6)]
# >>> list(zip([1,2,3],[4,5,6],[7,8,9]))
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
# >>> list(zip("abc","def"))
# [('a', 'd'), ('b', 'e'), ('c', 'f')]

# >>> list(zip([1,2,3],[4,5]))              <- 길이가 다를 경우 짧은 쪽 요소까지만 묶음
# [(1, 4), (2, 5)]









''' 표준 & 외부 라이브러리 '''
''' timedelta : 날짜/시간 차이를 일수로 표현한 객체 '''
# >>> import datetime
# >>> day1 = datetime.date(2021, 12, 14)
# >>> day2 = datetime.date(2023, 4, 5)
# >>> diff = day2 - day1
# >>> diff
# datetime.timedelta(days=477)


''' datetime.date '''
# >>> import datetime
# >>> day = datetime.date(2021, 12, 14)
# >>> day.weekday()
# 1                                 <- 0은 월요일, 1은 화요일 ... 6은 일요일
# >>> day.isoweekday()              # isoweekday() : ISO 8601을 따르도록 설계, 국제 표준 날짜 및 시간 표기법
# 2                                 <- 1은 월요일, 2는 화요일 ... 7은 일요일


''' time.time() : UTC를 사용하여 현재 시간을 실수 형태로 리턴'''
# >>> import time
# >>> time.time()                   
# 1768795457.4791415                # 1970/1/1 0:0:0 기준으로 지난 시간을 초 단위로 리턴

''' time.localtime() : time.time()이 리턴한 값을 연, 월, 일, 시, 분, 초,.. 의 형태로 변환 '''
# >>> time.localtime(time.time())
# time.struct_time(tm_year=2026, tm_mon=1, tm_mday=19, tm_hour=13, tm_min=4, tm_sec=33, tm_wday=0, tm_yday=19, tm_isdst=0)

''' NTP(Network Time Protocol)
        네트워크 장비의 시스템 시각을 
        UTC(Universal Time Coordinated, 협정 세계 표준시) 기준으로 동기화. 
        - Using UDP 123 port 
'''



''' time.asctime() : 시간을 ASCII 형식 문자열로 반환 '''
# >>> time.asctime()
# 'Mon Jan 19 16:37:42 2026'

''' time.ctime() : 항상 현재 시간만을 리턴 '''
# >>> time.ctime()
# 'Mon Jan 19 16:38:20 2026'


''' time.sleep() '''
#  >>> import time
#  >>> for i in range(10):
# ...     print(i)
# ...     time.sleep(1)
# ... 
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

''' random.random() : 0.0~1.0 실수 중 난수값'''
# >>> import random
# >>> random.random()
# 0.08327164208488502

''' random.randint() : 1~10 사이 정수 중 난수값 '''
# >>> random.randint(1, 10)
# 2

''' random.sample(대상, 뽑을 개수) : 대상은 리스트, 튜플, 문자열 등 '''
# >>> import random
# >>> data=[1,2,3,4,5]
# >>> random.sample(data, len(data))
# [5, 3, 4, 1, 2]
# >>> data
# [1, 2, 3, 4, 5]
# >>> random.sample(data,3)
# [1, 2, 4]



''' itertools.zip_longest 
        itertools.zip_longest는 가장 긴 리스트 기준, itertools 모듈(import 필요)
            - 남는 데이터는 유지되며, 빈값은 None 또는 지정한 값(fillvalue)으로 채움
        cf) zip: 가장 짧은 리스트 기준, 내장 함수, 남는 데이터는 버려짐
'''
import itertools
students = ['한민서','황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초콜릿', '젤리']

result = itertools.zip_longest(students, snacks, fillvalue='새우깡')
print(list(result))                 # [('한민서', '사탕'), ('황지민', '초콜릿'), ('이영철', '젤리'), ('이광수', '새우깡'), ('김승민', '새우깡')]  


''' itertools.permutation : 반복가능객체 안에서 r개를 선택한 순열을 이터레이터로 리턴  '''
import itertools
items = [1, 2]

    # 1. 순열(permutations) : 순서가 중요하므로 (1,2)와 (2,1) 모두 생성
print(list(itertools.permutations(items, 2)))           # [(1, 2), (2, 1)]
    # 2. 조합(combinations : 순서를 따지지 않으므로 (1, 2) 하나만 생성
print(list(itertools.combinations(items, 2)))           # [(1, 2)] 



''' functools.reduce : 하나의 값으로 합치는 함수 '''
import functools
data = [1,2,3,4,5]
result = functools.reduce(lambda x, y: x+y, data)
print(result)                           # 결과: 15

data = [1,2,3,4,5]
result = functools.reduce(lambda x,y: x+y, data, 10)
print(result)                           # 결과: 25
                    # result = 10            # 초기값 10
                    # for x in data:
                    #     result = result + x


''' operator.itemgetter : sorted같은 함수의 key 매개변수에 적용하여 다양한 기준으로 정렬 '''
from operator import itemgetter

students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B')
]
result = sorted(students, key=itemgetter(1))
print(result)                   # [('sally', 17, 'B'), ('Jane', 22, 'A'), ('dave', 32, 'B')]
# result = sorted(students, key=itemgetter(0))
# print(result)                   # [('dave', 32, 'B'), ('jane', 22, 'A'), ('sally', 17, 'B')]
# result = sorted(students, key=itemgetter(2))
# print(result)                   # [('jane', 22, 'A'), ('dave', 32, 'B'), ('sally', 17, 'B')]


# students 리스트가 딕셔너리일 경우 
from operator import itemgetter

students = [
    {"name": "jane", "age": 22, "grade": 'A'},
    {"name": "dave", "age": 32, "grade": 'B'},
    {"name": "sally", "age": 17, "grade": 'B'}, 
]
result = sorted(students, key=itemgetter('age'))
print(result)                   # [{'name': 'sally', 'age': 17, 'grade': 'B'}, {'name': 'jane', 'age': 22, 'grade': 'A'}, {'name': 'dave', 'age': 32, 'grade': 'B'}]