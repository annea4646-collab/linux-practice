''' PEP 8 (Python Enhance Proposal 8)
    1. 들여쓰기(indentation)'''
# if condition:
#     do_something()

''' 2. 줄 길이(Line Length: 한 줄의 길이는 최대 79자로 제한) '''
# result = some_function(param1, param2, param3,
#                        param4, param5)

''' 3. 빈 줄(blank Lines: 클래스와 함수 정의 사이에는 두 줄의 빈 줄을 둠) '''
# class MyClass:


#     def method(self):
#         pass

#     def another_method(self):
#         pass

''' 4. 임포트(Imports: Import는 파일 최상단에 위치)
    각기 다른 종류의 임포트 구별(표준 라이브러리, 서드파티 라이브러리, 로컬 모듈 순) '''
# import os       # [표준 라이브러리] 파이썬 설치 시 들어있는 기본 도구(운영체제 제어)
# import sys      # [표준 라이브러리] 파이썬 인터프리터 제어

# import requests # [서드파티 라이브러리] pip install로 설치한 외부 도구(HTTP 통신)

# from mymodule import my_function, add_numbers    # [로컬 모듈] 같은 폴더의 mymodule.py에서 만든 함수


#''' requests 테스트 '''
# response = requests.get('https://api.github.com')
# data = response.json()

# print(f'사용자 정보 주소: {data["user_url"]}')
#''' sys 테스트 '''
# print('--- 파이썬 모듈 검색 경로 ---')
# for path in sys.path:
#     print(path)

# ''' mymodule 테스트'''
# print('--- 테스트 시작 ---')
# greeting = my_function('홍길동')
# print(f'인사말 결과: {greeting}')

# sum_result = add_numbers(10, 20)
# print(f'더하기 결과: {sum_result}')

# print(add_numbers(5, 5))
# print('--- 테스트 종료')

''' 5. 함수와 변수 이름(snake_case 사용) '''
# def my_fuction():
#     my_variable = 10

''' 6. 클래스 이름(CamelCase 사용) '''
# class MyClass:
#     pass

''' 7. 상수(Constanct, 모든 글자를 대문자로 하되 단어 사이는 밑줄) '''
# MAX_RETRIES = 5

''' 8. 공백(whitecpae 사용)'''
# my_list = [1, 2, 3]         # 콤마, 콜론, 세미콜론 뒤에는 공백 추가
# result = my_fuction(3, 5)   # 함수 정의와 호출 시 괄호 안쪽에는 공백 사용하지 않음
# result = (a + b) * (c - d)  # 연산자의 양쪽에는 공백을 사용

''' 9. 주석(Commdents: 명확하고 간결하게 코드 의도 설명, 코드와 동일한 줄에 사용, # 뒤에 공백 추가)'''
# # 이 함수는 값을 더하는 함수입니다.
# def add(a, b):
#     return a + b

''' 10. 도큐스트링(Docstrings: 함수, 클래스, 모듈에는 도큐스트링 사용하여 설명 작성)
    일반주석(#)은 파이썬이 무시하지만, Docstring은 파이썬이 따로 저장함'''
# def add(a, b):
#     '''
#     두 수를 더해서 반환합니다.

#     매개변수:
#         a (int): 첫 번째 숫자
#         b (int): 두 번째 숫자

#     반환값:
#         int: 두 숫자의 합
#     '''
#     return a + b

# print(add.__doc__)      # docstring 출력: __doc__ 는 이 함수의 설명서 내용을 가져오라는 명령어



''' 클래스와 객체 '''
# class Cookie:
#     pass

# a = Cookie()
# b = Cookie()

# print(f'a의 메모리 주소는 {id(a)}')
# print(f'b의 메모리 주소는 {id(b)}')


''' 파이썬에는 접근제한자(public, private, protected) 키워드가 없음
    접근 제어를 강제하지 않고, 개발자 간의 약속(convention)으로 처리
        name : public 취급
        _name : protected처럼 취급
        __name : name mangling(이름 변경)에 의해 외부 접근이 private처럼 어렵게 됨
'''
# class Parent:
#     def __init__(self):
#         print("Parent init id: ", id(self))

# class Child(Parent):
#     def __init__(self):
#         print("Child init BEFORE super id: ", id(self))
#         super().__init__()      # super()__init__()은 자식 인스턴스(=self)를 Parent 클래스의 __init__에 넘겨서, Parent가 자신의 초기화를 하도록 하는 것임.
#                                 # Child가 __init__()을 재정의(override) 했으므로, 부모의 init__은 가려짐.
#                                 # 따라서 부모의 초기화 로직을 실행하려면 반드시 super()__init__()을 명시적으로 추출해야함.
#         print("Child init AFTER super id: ", id(self))

# c = Child()
# print("final c id: ", id(c))


''' Child 클래스가 Parent를 상속 받았고, Child에 자체적인 __init__()이 정의되지 않았을 때 
        Child.__init__가 없다  ==> Parent.__init__ 사용함
        즉, Child는 init을 override 하지 않았기 때문에, 
        Child()를 호출하는 순간 파이썬은 자동으로 Parent.__init__을 호출함
'''

# class Parent:
#     def __init__(self):
#         print("Parent init 실행됨")
#         self.x = 10

# class Child(Parent):
#     pass

# c = Child()     # Child가 __init__을 정의하지 않았으므로,
#                 # 부모의 __init__ 메서드를 그대로 상속받아 사용함.
#                 # 즉, 별도의 super 호출 없이도 부모의 로직이 자동으로 수행됨.
# print(c.x)



''' Practice 1 '''
# class Parent:

#     def __init__(self):
#         print("Parent: 10억(x)을 유산으로 남긴다")
#         self.x = 10


# class Child(Parent):
#     def __init__(self):
#         # 부모의 금고를 먼저 연다.(super 호출)
#         super().__init__()

#         # 내 능력을 추가한다.
#         print("Child: 나는 코딩 능력(y)를 개발했다.")
#         self.y=50

# # 인스턴스화
# c = Child()

# print(f'자식의 재산: x={c.x}, y={c.y}')


''' Practice 2 
        Parent field -  소속
        Child  field -  이름, 대표전화번호, 주소, 이메일, 직급, 성별 ...
'''


class Parent:
    def __init__(self, organization):
        self.organization = organization  # 소속 (공통 필드)

class Child(Parent):
    def __init__(self, organization, name, phone, email):
        # 부모의 __init__을 호출하며 '소속' 정보를 전달함
        super().__init__(organization) 
        
        # 자식만의 고유 정보 (개별 필드)
        self.name = name
        self.phone = phone
        self.email = email

# 인스턴스화
c = Child("우리은행", "김철수", "010-1234-5678", "chulsoo@example.com")
print(f"소속: {c.organization}, 이름: {c.name}")


