# mymodule.py

def my_function(name):
    """
    이 함수는 이름을 받아서 환영 메시지를 반환하는 로컬 함수입니다.
    """
    return f"안녕하세요, {name}님! 로컬 모듈 호출에 성공했습니다."

def add_numbers(a, b):
    return a + b

# 모듈이 직접 실행될 때만 작동하는 테스트 코드
if __name__ == "__main__":
    print("mymodule이 직접 실행되었습니다.")