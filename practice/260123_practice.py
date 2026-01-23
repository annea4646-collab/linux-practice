''' 종합 복습 '''
# import sys
# a=[1,2,3]
# b=a
# print(id(a))                        # 132789644729920
# print(id(b))                        # 132789644729920   : 메모리 공유
# print(sys.getsizeof(a))             # 88    : a가 차지하고 있는 메모리(byte) 점유 크기

''' 함수 프로그래밍 : 무엇을 실행할 것인가?(동작 중심)'''
''' 클래스 프로그래밍 : 누가 무엇을 가지고 어떤 일을 할 것인가?(객체 중심)'''

''' 클래스
        - Field/Attribute   : 객체의 데이터 변수
            자동차(색상, 모델명, 현재 속도)
        - Method            : 객체가 할 수 있는 기능(함수)
            자동차(가속하기(), 감속하기(), 경적울리기())
    설계: class Car     (Heap에 자동차 객체)생성: my_car=Car()     참조: 변수 my_car는 Stack 영역에 생성(Heap에 있는 객체 id를 가리킴)
'''

''' numpy '''
# import numpy as np
# arr = np.array([1,2,3,4,5])
# result = arr * 2
# print(np.mean(arr))         # 3.0   : 평균, 나눗셈 결과나 평균값은 Float 타입 반환
# print(np.sum(arr))          # 15
# print(result)               # [ 2  4  6  8 10]

''' Stack Memory '''
# def my_function(a,b):
#     x = 10
#     y = [1,2,3]
#     z = 'hello'
#     return a + b
# my_function(5, [100, 200])


# def my_function(a, b):
#     print("id(a): ", id(a))         # 128918920102256
#     print("id(b): ", id(b))             # 128918919307072
# x=5
# y=[100,200]
# print("id(x): ", id(x))             # 128918920102256
# print("id(y): ", id(y))                 # 128918919307072
# my_function(x, y)

