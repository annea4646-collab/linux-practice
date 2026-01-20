# g_var = "Global" # 글로벌 변수

# class Test:
#     def setdata(self, first, second): # first, second는 로컬 변수
#         self.first = first            # self.first는 인스턴스 변수 (Heap 저장)
#         self.second = second          # self.second는 인스턴스 변수 (Heap 저장)
        
#         # 메서드가 끝나면 로컬 변수 first, second는 메모리에서 사라짐
#         # 하지만 self.first, self.second는 객체에 붙어있으므로 살아남음



# class FourCal:

#     def setdata(self, first, second):
#         self.first = first
#         self.second = second

#     def add(self):
#         result = self.first + self.second
#         return result
    
#     def sub(self):
#         result = self.first - self.second
#         return result
    
#     def mul(self):
#         result = self.first * self.second
#         return result
    
#     def div(self):
#         result = self.first / self.second
#         return result

# a = FourCal()
# b = FourCal()

# a.setdata(1, 2)
# b.setdata(30, 12)

# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div())
# print(id(a))


# print(b.add())
# print(b.sub())
# print(b.mul())
# print(b.div())
# print(id(b))
# # print(id(b.add()))
# # print(id(b.sub()))
# # print(id(b.mul()))
# # print(id(b.div()))




# class FourCal:
    
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second

#     def add(self):
#         result = self.first + self.second
#         return result
    
#     def sub(self):
#         result = self.first - self.second
#         return result
    
#     def mul(self):
#         result = self.first * self.second
#         return result
    
#     def div(self):
#         result = self.first / self.second
#         return result

# a = FourCal(2, 4)
# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div())


# class Parent:

#     def __init__(self, organization="미소속"):
#         self.organization = organization
#         print(f"생성완료! 소속: {self.organization}")

# p1 = Parent()
# print(id(p1))

# p2 = Parent("Google")
# print(id(p2))
# p2 = Parent("Naver")
# print(id(p2))
# p2.organization = "Google"
# print(f"데이터만 수정! 소속: {p2.organization}")
# print(id(p2))

# class Student:
#     def __init__(self, name='미등록', age=0):
#         self.name = name
#         self.age = age
    
# s1 = Student()
# print(s1.name)
# print(s1.age)

''' 일반적인 방식 '''
# f = open("test.txt", "w")
# f.write("Hello")
# f.close()         # f.close() 를 안해주면 파일 오픈 상태 유지(메모리 누수)

''' 컨텍스트 매니저 방식 '''
# with open("test.txt", "w")as f:   # __enter__ 자동 호출
#     f.write("Bye")                # __exit__ 자동 호출

''' 생성자 '''
# class FourCal:
#     def __init__(self, first, second):  # 사용자 정의 생성자
#         self.first = first
#         self.second = second

# a = FourCal(4, 2)       # 값 전달 필수, 생성 시점 데이터 강제 주입
# print(a.first)
# print(a.second)


# class A:            # 기본 생성자 Default
#     pass            # 아무것도 하지 말라는 키워드

# a = A()             # 괄호 안에 값 없이 객체 생성, 틀만 만들고 나중에 데이터 추가

''' 클래스 변수 '''
# class Family():
#     lastname = "김"

# Family.lastname

# a = Family()
# b = Family()

# print(a.lastname)
# print(id(a.lastname))
# print(b.lastname)
# print(id(b.lastname))

# Family.lastname = "박"
# print(a.lastname)
# print(id(a.lastname))
# print(b.lastname)
# print(id(b.lastname))

# # a = Family()
# # print(Family.lastname)
# # print(id(Family.lastname))

# # Family.lastname = "정"
# # print(Family.lastname)
# # print(id(Family.lastname))


''' 클래스 상속 class 클래스_이름(상속할_클래스_이름)'''
# class FourCal:
#     pass

# class MoreFourCal(FourCal):
#     pass


''' Case 1 '''
class FourCal:
    def __init__(self, first, second):      # 부모가 생성자를 가짐
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second
    
class MoreFourCal(FourCal):                 # 자식은 비어있음
    pass

a = MoreFourCal(4, 2)
print(a.add())



''' Case 2 '''
class FourCal:

    def add(self):                          # 부모가 기능을 가짐
        return self.first + self.second
    
class MoreFourCal(FourCal):
    def __init__(self, first, second):      # 자식이 생성자를 가짐
        self.first = first
        self.second = second

a = MoreFourCal(4,2)
print(a.add())