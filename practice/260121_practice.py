''' 7-1 파이썬과 유니코드 '''

''' 유니코드로 문자열 다루기    1. 인코딩 하기 '''
# >>> a="Life is too short"
# >>> b=a.encode('utf-8')
# >>> b
# b'Life is too short'
# >>> type(b)
# <class 'bytes'>


# >>> a='한글'
# >>> a.encode('euc-kr')            # euc-kr(한글 2byte)를 인수로 인코딩
# b'\xc7\xd1\xb1\xdb'
# >>> a.encode('utf-8')             # utf-8(한글 3byte)를 인수로 인코딩
# b'\xed\x95\x9c\xea\xb8\x80'


''' 유니코드로 문자열 다루기    2. 디코딩 하기
         : 인코딩한 바이트 문자열을 유니코드 문자열로 반환하려면 인코딩 방식을 똑같이 맞춰야함  '''
# >>> a='한글'
# >>> b=a.encode('euc-kr')
# >>> b.decode('euc-kr')
# '한글'

# >>> b.decode('utf-8')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc7 in position 0: invalid continuation byte


''' 유니코드로 문자열 다루기    3. 입출력과 인코딩 '''
# with open('practice/euc-kr.txt', encoding='euc-kr') as f:
#     data = f.read()

# data = data + "\n" + "추가 문자열"

# with open('practice/euc-kr.txt', encoding='euc-kr', mode='w') as f:
#     f.write(data)


''' 문자의 저장/ 출력 방식 '''
# >>> a='A';
# >>> b='\u0042';
# >>> c='1';
# >>> d=97;
# >>> e=0xac00;
# >>> print(a)
# A
# >>> print(b)
# B
# >>> print(c)
# 1
# >>> print(d)
# 97
# >>> print(e)
# 44032

''' closure : 외부 함수의 변수에 접근할 수 있는 내부 함수를 클로저라고 함 '''
# def mul(m):                         # 함수를 찍어내는 틀
#     def wrapper(n):
#         return m*n
#     return wrapper

# if __name__ == "__main__":
#     mul3=mul(3)                     # def wrapper(n):   return 3 * n (특정 설정값이 고정된 전용 함수를 만듬)
#     mul5=mul(5)

#     print(mul3(10))                 # wrapper(10) -> return 3 * 10 ->   30
#     print(mul5(10))                 # 50


''' closure를 사용하는 이유는:  
        함수에 상태를 저장해두면서, 객체보다 가볍게 재사용 가능한 기능 단위룰 만들기 위함 '''
# def make_counter():                 # 객체보다 가벼운 상태 저장소: 클로저가 데이터를 저장하는 용도로 사용
#     count = 0

#     def counter():
#         nonlocal count              # 내부 함수에서 외부 함수의 변수값을 수정하기 위해 사용
#         count += 1
#         return count
    
#     return counter

# counter1 = make_counter()           # counter1, counter2는 각각 자신만의 count 변수를 가짐
# print(counter1())                       # 1
# print(counter1())                       # 2
# print(counter1())                       # 3

# counter2 = make_counter()
# print(counter2())                       # 1
# print(counter2())                       # 2



''' decorator   
        : 데코레이터는 다른 함수에 붙여서 새로운 기능을 달아주는 도구 
         - 함수를 수정하지 않고도 새로운 기능을 덧붙일 수 있음 '''

# import time

# def elapsed(original_func):
#     def wrapper():                      # 오직 인수가 없는 함수만 포장 가능
#         start = time.time()
#         result = original_func()
#         end = time.time()
#         print("함수 수행 시간:%f" % (end-start))
#         return result
#     return wrapper

# @elapsed    # 정의한 함수를 @데코레이터로 활용, myfunc()가 실행될 때 '추가행동'이 자동으로 따라 붙음.
# def myfunc():
#     print("함수가 실행됩니다")

# myfunc()


''' 데코레이터는 기존 함수의 입력 인수에 상관없이 동작하도록(어떤 함수에든 붙을 수 있도록) 만들어야 함. 
    - 기존 함수의 입력 인수를 알 수 없는 경우 *args와 **kwargs 매개변수 이용  '''
# import time

# def elapsed(original_func):
#     def wrapper(*args, **kwargs):           # 인수가 있든 없든, 몇 개든 상관없이 모든 함수를 포장할 수 있음
#         # *args(Arguments): 여러개의 위치 인자를 튜플로 묶어서 받음
#             # myfunc("Hello", "Python") -> args는 ("Hello", "Python")
#         # **kwargs(Keyword Arguments): 딕셔너리 형태로 인자를 받음
#             # myfunc(msg="Hello",count=3) -> kwargs는 {'msg':"Hello", 'count': 3}
#         start = time.time()
#         result = original_func(*args, **kwargs)
#         end = time.time()
#         print("함수 수행 시간:%f" % (end-start))
#         return result
#     return wrapper

# @elapsed    
# def myfunc(msg):
#     print("%s를 출력합니다" %msg)

# myfunc("You need python")

''' 예시 '''
# def check_admin(func):
#     def wrapper(user_name, *args, **kwargs):
#         if user_name != "admin":
#             print(f"경고: '{user_name}'님은 관리자 권한이 없어 '{func.__name__}'을 실행할 수 없습니다.")
#             return
#         return func(user_name, *args, **kwargs)
#     return wrapper

# @check_admin
# def delete_database(user_name):
#     print(f"[{user_name}] 데이터베이스를 삭제합니다. (위험!!)")

# delete_database("guest")  # 거부됨
# delete_database("admin")  # 실행됨



''' 내장 데코레이터     @abstractmethod, @property, @staticmethod
    - @staticmethod:    정적메서드는 클래스나 인스턴스의 상태를 참조하지 않고 독립적으로 동작하는 메소드 
        * 유지해야될 정보를 고정하면 편리, class.method() 로 호출
    - @property:    메서드를 변수처럼 접근하게 함(getter 역할), obj.method 로 호출
    - @abstractmethod:  추상메서드는 자식 클래스에서 반드시 overriding 필요 ,상속 후 호출
'''
# class MathUtils:
#     @staticmethod
#     def add(x, y):
#         return x + y
# # 인스턴스(self) 생성 없이 직접 호출 가능
# result = MathUtils.add(3, 5)            # 클래스명.메소드명()으로 즉시 실행 가능
# print(result)


''' @staticmethod 활용 예시) ERP 프로그램 '''
# class ERP:
#     def __init__(self, name, rank, salary):
#         self.name = name
#         self.rank = rank
#         self.salary = salary

#     @staticmethod
#     def calculate_raise(salary, rank):
#         if rank == "대리":
#             return salary * 0.05
#         elif rank == "과장":
#             return salary * 0.10
#         else:
#             return 0

#     def apply_raise(self):
#         # 클래스 이름을 통해 정적 메서드에 바로 접근
#         raise_amount = ERP.calculate_raise(self.salary, self.rank)
#         self.salary += raise_amount
#         print(f"{self.name}({self.rank})님의 급여가 {raise_amount}원 인상되어 총 {self.salary}원이 되었습니다.")

# # 1. 인스턴스 생성 없이 직접 호출 가능 (정적 메서드의 특징)
# # 특정 사원과 상관없이 "과장이면 얼마 올라?"를 바로 계산해볼 수 있음
# sample_raise = ERP.calculate_raise(5000000, "과장")
# print(f"과장급 기본 인상분 계산 결과: {sample_raise}원")

# print("-" * 30)

# # 2. 실제 사원 객체 활용
# emp1 = ERP("김철수", "대리", 4000000)
# emp2 = ERP("이영희", "과장", 6000000)

# emp1.apply_raise()
# emp2.apply_raise()


''' class namespace
    : 클래스 본문 내부에서 만든 이름들은 하나의 dict 안에 저장되는데 이 dict를 네임스페이스라 함
    class A:     def f(): ...
    A.__dict__["f"] = staticmethod(function)
'''
# def my_independent_func(msg):           # 포장되지 않은 순수 함수 정의
#     print(f"메시지 출력: {msg}")

# class A:                                # 반 클래스 생성
#     pass

# print("1. 처음 상태: ", A.__dict__.keys())      # dict_keys(['__module__', '__dict__', '__weakref__', '__doc__'])

# A.f = staticmethod(my_independent_func)     # 객체.이름: 클래서 A안에 f를 넣음
#     # 여기서 f는 클래스 A의 네임스페이스에 등록된 staticmethod가 됨

# print("2. 주입 후 상태: ", A.__dict__.keys())   # dict_keys(['__module__', '__dict__', '__weakref__', '__doc__', 'f'])
# print("3. f의 정체: ", A.__dict__['f'])         # <staticmethod(<function my_independent_func at 0x75fc405abf40>)>

# A.f("Hello Python!")                            # 메시지 출력: Hello Python!


''' iterator    : 값을 차례대로 꺼낼 수 있는 객체. next 함수 호출 시 계속 그 다음값 리턴
         __iter__() 메서드를 가지고 있고, 호출 시 자기 자신(self)를 반환해야함
         __next__() 메서드를 가지고 있으며, 호출할때 
                - 다음 요소를 반환하거나 
                - 더 이상 반환요소 없을 시 stopiteration 예외 발생시켜야함
'''

# a=[1, 2, 3]   # 리스트처럼 반복 가능하다고 해서 이터레이터는 아님
# next(a)             # Traceback (most recent call last):
                    #   File "/home/annea4646/doit/practice/260121_practice.py", line 241, in <module>
                    #     next(a)
                    # TypeError: 'list' object is not an iterator

# a=[1,2,3]
# ia=iter(a)      # iter 함수를 이용해 이터레이터로 만들 수 있음
# print(type(ia))     # <class 'list_iterator'>

# print(next(ia))     # 1
# print(next(ia))     # 2
# print(next(ia))     # 3


''' 수동으로 이터레이터 조작(for문 없이) '''
# my_list= [10, 20, 30]
# my_iter = iter(my_list)

# print(type(my_iter))    # <class 'list_iterator'>

# print(next(my_iter))    # 10
# print(next(my_iter))    # 20
# print(next(my_iter))    # 30

# try:
#     print(next(my_iter))
# except StopIteration:
#     print("데이터 소진: 반복 종료") # 데이터 소진: 반복 종료 => 4번째 next에서 리턴

''' 제너레이터
        - 이터레이터를 생성하는 함수 user-defined function
        - 제너레이터로 생성한 객체는 next() 함수 호출 시 그 값을 차례로 얻을 수 있음
        - 제너레이터는 함수 내부에서 값을 한번에 모두 반환하지 않고, 필요할때마다 하나씩 반환하는 방식
            - yield 키워드 사용
            - __iter__()와 __next__() 메서드를 자동으로 구현
            - next() 함수로 값을 하나씩 가져올 수 있음.
'''
# def mygen():
#     yield 'a'
#     yield 'b'
#     yield 'c'
# g = mygen()

# print(next(g))      # a
# print(next(g))      # b
# print(next(g))      # c
# print(next(g))      # Traceback (most recent call last):
#                     #   File "/home/annea4646/doit/practice/260121_practice.py", line 287, in <module>
#                     #     print(next(g))
#                     # StopIteration

''' 제너레이터 표현식(generator expression) '''
# def mygen():
#     for i in range(1, 1000):
#         result = i * i
#         yield result
# gen = mygen()
# print(next(gen))        # 1
# print(next(gen))        # 4
# print(next(gen))        # 9

# # 리스트 컴프리헨션 버전
# values = [i*i for i in range(1, 1000)]
# print(values[0])        # 1
# print(values[1])        # 4
# print(values[2])        # 9


''' 파이썬은 동적 프로그래밍 언어(dynamic programming language) '''
# >>> a=1
# >>> type(a)
# <class 'int'>
# >>> a='1'
# >>> type(a)
# <class 'str'>

''' 자바는 정적 프로그래밍 언어(static programming language) '''
# int a = 1;      # a 변수를 int 형으로 지정
# a = "1"         # a 변수에 문자열을 대입할 수 없으므로 컴파일 오류 발생


''' 파이썬 타입 어노테이션(type annotation) : 타입 힌트를 알려주는 정도 기능 지원 '''
# num: int = 1                    # 변수 어노테이션: 해당 모듈이나 클래스의 __annotations__ 딕셔너리에 저장, int는 타입 힌트를 나타내기 위한 구문
# def add(a: int, b: int) -> int: # 함수 어노테이션:  함수 객체 내부에도 타입 정보 저장,  -> int: 은 리턴 타입 힌트를 나타내기 위한 구문(Return Annotation)
#     return a+b
# print(add.__annotations__)      # {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}


''' mypy : 파이썬 어노테이션을 적극 활용하기 위함. pip install mypy 설치 후 사용 '''
# def add(a: int, b: int) -> int:
#     return a+b
# result = add(3,4)
# print(result)




''' 정규 표현식(regular expressions) 살펴보기 '''
''' 정규식을 사용하지 않은 풀이법 '''
# data="""
# park 800905-1049118
# kim 700905-1059119
# """
# result = []

# for line in data.split("\n"):               # 줄바꿈 기준으로 나눔 ['', 'park 800905-1049118', 'kim 700905-1059119', '']
#     word_result = []
#     for word in line.split(" "):            # 각 줄을 공백 기준으로 단어별로 나눔 ['park', '800905-1049118']
#         if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():   
#                         # 길이가 14글자? 앞 6글자는 숫자? 뒤 7자는 숫자? True 확인
#             word = word[:6] + "-" + "*******"
#         word_result.append(word)
#     result.append(" ".join(word_result))    # 나눈 단어 공백포함 조립하기
# print("\n".join(result))                        # park 800905-*******
#                                                 # kim 700905-*******

''' 정규식을 사용한 풀이법 '''
import re
data ="""
park 800905-1049118
kim 700905-1059119
"""
# 앞자리 6자리와 뒷자리 7자리로 분리하는 정규식 패턴
pat = re.compile("(\d{6})[-](\d{7})")
# g<1> 첫번째 그룹은 유지하고(앞자리 6자리) 뒷자리 7자리를 *로 대체
print(pat.sub("\g<1>-*******",data))            # park 800905-*******
                                                # kim 700905-*******

''' 정규 표현식의 기초, 메타 문자        . ^ $ * + ? {} [] \ | ()   '''
''' 1. 문자 클래스(character class)  
        []      :   []사이의 문자들와 매치  [abc]   => a,b,c 중 문자 하나가 들어가면 매치
        [-]     : []안의 두 문자 사이에 하이픈(-) 사용 시 두 문자 사이의 범위를 의미    [a-zA-Z]   => 모든 알파벳
        .       : \n을 제외한 모든 문자와 매치  a.b => "a + 모든 문자 + b"
        [.]     : [] 안에 . 이 있는 경우    a[.]b => a.b
        *       : 0부터 무한대까지 반복될때 사용(실제 2억개 정도만 가능)  ca*t => *바로 앞의 a가 0부터 무한대까지 반복될 수 있음
        +       : 최소 1번 이상 반복될때 사용, +는 반복횟수가 1부터     ca+t => "c + a가_1번이상_반복 + t"

'''