''' 클래스의 상속: class 클래스_이름(상속할_클래스_이름)'''

# class FourCal:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second

# class MoreFourCal(FourCal):
#     pass

# class SafeFourCal(FourCal):
#     def div(self):
#         if self.second == 0:
#             return 0
#         else:
#             return self.first / self.second
        
# a = SafeFourCal(4, 2)
# print(a.div())


''' 다중 상속 : super() 함수 '''

# class A:
#     def process(self):
#         print("Process from A")

# class B(A):
#     def process(self):
#         print("Process from B")
#         super().process()

# class C(B):
#     def process(self):
#         print("Process from C")
#         super().process()

# c = C()
# c.process()
# print(C.mro())



''' 추상 클래스(Abstract class)'''

# from abc import ABC, abstractmethod

# # 추상 클래스 정의
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass                                # 추상 메서드, 하위클래스에서 반드시 구현
#     def sleep(self):
#         print("This animal is sleeping")    # 일반 메서드

# # 추상 클래스를 상속받는 구체적인 클래스
# class Dog(Animal):
#     def sound(self):
#         return "Bark"

# class Cat(Animal):
#     def sound(self):
#         return "Meow"
# # 인스턴스 생성
# dog = Dog()
# cat = Cat()

# print(dog.sound())
# print(cat.sound())
# dog.sleep()
# cat.sleep()



''' 추상 클래스 에러 사례'''

# from abc import ABC, abstractmethod

# # 추상 클래스 정의
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass                                # 추상 메서드, 하위클래스에서 반드시 구현
#     def sleep(self):
#         print("This animal is sleeping")    # 일반 메서드

# # 추상 클래스를 상속받는 구체적인 클래스
# class Dog(Animal):
#     # def sound(self):
#     #     return "Bark"
#     pass

# class Cat(Animal):
#     def sound(self):
#         return "Meow"
# # 인스턴스 생성
# dog = Dog()
# cat = Cat()

# print(dog.sound())
# print(cat.sound())
# dog.sleep()
# cat.sleep()

# '''
#     Traceback (most recent call last):
#         File "d:\Python 기초강의\Python 3 좋은 코드를 작성하는 방법\class\note060115.py", line 97, in <module>
#         dog = Dog()
#               ^^^^^
#     TypeError: Can't instantiate abstract class Dog with abstract method sound
#     Dog 클래스로 인스턴스를 만들 수 없다. 왜냐하면 sound라는 추상메서드를 구현하지 않았기 때문.
# '''




''' 모듈과 패키지 '''

''' 모듈 만들기
     mod1.py '''

''' 모듈 불러오기 (cmd) '''

    # Microsoft Windows [Version 10.0.26200.7462](c) Microsoft Corporation. All rights reserved.
    # C:\Users\403_28>d:
    # D:\>cd doit
    # D:\doit>dir
    # D 드라이브의 볼륨에는 이름이 없습니다.
    # 볼륨 일련 번호: 6666-ED7D

    # D:\doit 디렉터리

    # 2026-01-15  오후 02:18    <DIR>          .
    # 2026-01-15  오후 02:18    <DIR>          doing
    # 2026-01-15  오후 02:08                68 mod1.py
    #             1개 파일                  68 바이트
    #             2개 디렉터리  343,066,501,120 바이트 남음

    # D:\doit>python
    # Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
    # Type "help", "copyright", "credits" or "license" for more information.

''' 1. 대화형 인터프리터에서 mod1.py 불러오기 '''
    # >>> import mod1
    # >>> print(mod1.add(3, 4))
    # 7
    # >>> print(mod1.sub(4, 2))
    # 2
    # >>>

''' 2. Import'''

    # >>> from mod1 import add
    # >>> add(3, 4)
    # 7

    # >>> from mod1 import add, sub
    # >>> from mod1 import *
    # >>> add(5, 3)
    # 8
    # >>> sub(5, 3)
    # 2

''' if __name__ == "__main__": 의 의미 '''

    # mod1.py
    #     def add(a, b):
    #         return a + b

    #     def sub(a, b):
    #         return a - b

    #     if __name__ == "__main__":
    #         print(add(1, 4))
    #         print(sub(4, 2))
    
''' -1 다른 파일에서 이 모듈을 불러오거나, 대화형 인터프리터 사용할 경우 if문 수행 안됨 '''
# PS D:\doit> python
# >>> import mod1
# >>> 
''' -2 직접 파일을 실행했을 경우 if문 수행 '''
# PS D:\doit> python mod1.py
# 5
# 2


''' 단일 언더스코어 - 내부에서만 사용하라는 관습적 표시(protected) '''
# class MyClass:
#     def __init__(self):
#         self._internal_variable = 42    # 내부에서만 사용하는 변수임을 암시
# my_instance = MyClass()
# print(my_instance._internal_variable)           # OK - 결과값 42


# ''' 더블 언더스코어 - name mangling을 사용하여 변수 이름을 클래스 내에서 숨기는 방식 '''
# class MyClass:
#     def __init__(self):
#         self.__private_variable = 42    # 네임 맹글링이 적용된 변수
#           # Name Mangling: __private_vatiable 를 _MyClass__private_variable로 바꿈.

# my_instance = MyClass()
# # print(my_instance.__private_variable)   # Error - AttributeError: 'MyClass' object has no attribute '__private_variable'
# print(my_instance._MyClass__private_variable)     # OK - 결과값 42


''' 특별 메소드 - 변수 이름 앞 뒤로 더블 언더스코어가 붙는 것은 특별한 의미를 가짐 
            __init__    : 객체 초기화
            __str__     : 객체의 문자열 표현
            __repr__    : 객체의 공식적인 문자열 표현
            __eq__      : 두 객체의 동등성 비교
'''

# class Person:
#     def __init__(self, name):           # 객체 초기화
#         self.name = name
# p = Person('철수')
# print(p.name)       # "철수" 출력


# class MyClass:
#     def __str__(self):                  # 사람이 읽기 좋은 문자열
#         return "MyClass instance"
# obj = MyClass()
# print(obj)          # print(obj.__str__())와 동일 동작 -  "MyClass instance" 출력 


# class MyClass:
#     def __repr__(self):                 # 공식적인(개발자용) 문자열
#         return "MyClass"
# obj = MyClass()
# obj                 # 인터프리터에서 MyClass()
#                             # >>> class MyClass:
#                             # ...     def __repr__(self):
#                             # ...             return "My Class"
#                             # >>> obj = MyClass()
#                             # >>> obj
#                             # My Class


# class Point:
#     def __init__(self, x):
#         self.x = x
#     def __eq__(self, other):            # 객체 비교 (==)
#         return self.x == other.x
# p1 = Point(3)
# p2 = Point(3)
# p3 = Point(5)
# print(p1 == p2)     # True
# print(p1 == p3)     # False

''' 클래스나 변수 등을 포함한 모듈 - 대화형 인터프리터로 확인 '''

    # mod2.py
    #     PI = 3.141592

    #     class Math:
    #         def solv(self, r):
    #             return PI * (r **2)
    #     def add(a, b):
    #         return a + b

# >>> import mod2
# >>> print(mod2.PI)
# 3.141592
# >>> a = mod2.Math()
# >>> print(a.solv(2))
# 12.566368
# >>> print(mod2.add(mod2.PI, 4.4))
# 7.5415920000000005
# >>>

''' 다른 파일에서 모듈 불러오기 '''

#     modtest.py
#         import mod2

#         result = mod2.add(3, 4)
#         print(result)

# 결과값 : 7


''' 다른 디렉터리에 있는 모듈 불러오는 방법 '''
''' 1. sys.path 사용하기 '''
# PS D:\doit> python

# >>> import sys
# >>> sys.path
# ['', 'C:\\Users\\403_28\\AppData\\Local\\Programs\\Python\\Python311\\python311.zip', 'C:\\Users\\403_28\\AppData\\Local\\Programs\\Python\\Python311\\DLLs', 'C:\\Users\\403_28\\AppData\\Local\\Programs\\Python\\Python311\\Lib', 'C:\\Users\\403_28\\AppData\\Local\\Programs\\Python\\Python311', 'C:\\Users\\403_28\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages']

''' 2. PYTHONPATH 환경변수 사용하기 '''
# D:\doit>set PYTHONPATH=D:\doit\mymod         # cmd 명령어, 모듈 찾을때 D:\doit\mymod 같이 뒤져봐.
# D:\doit>python
# >>> import mod3
# >>> print(mod3.add(7, 8))
# 15

# ------ PowerShell -------
# PS D:\doit> $env:PYTHONPATH = "D:\doit\mymod"       # PowerShell 에서는 set이 아닌 $env:로 작동
# >>> import mod3
# >>> print(mod3.add(4,5))
# 9
