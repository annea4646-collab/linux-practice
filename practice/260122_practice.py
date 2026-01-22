''' 정규 표현식(regular expressions) '''
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
        {}      : {m,n} 반복 횟수가 m부터 n까지인 문자와 매치할 수 있음
        {m}     : 반드시 m번 반복,  ca(2)t -> "caat"
        ?       : {0, 1}을 의미하는 메타문자,   ab?c -> "a + b가_있어도_없어도_됨 + c" -> abc, ac 둘 다 참
'''


''' re(regular expression ) 모듈 '''
# >>> import re
# >>> p = re.compile('ab*')

''' 정규식을 이용한 문자열 검색 
        match     : 문자열의 처음부터 정규식과 매치되는지 조사
        search    : 문자열 전체를 검색하여 정규식과 매치되는지 조사
        findall   : 정규식과 매치되는 모든 문자열을 리스트로 리턴
        finditer  : 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 리턴
'''

# 패턴 예)
# >>> import re
# >>> p = re.compile('[a-z]+')          # 소문자 알파벳이 최소 1개 이상 나오는 패턴

''' match '''
# >>> m = p.match("python")
# >>> print(m)
# <re.Match object; span=(0, 6), match='python'>    # span=(0, 6)은 매칭이 시작 ~ 끝 위치

# >>> m = p.match("3 python")
# >>> print(m)
# None              # 설정된 패턴 [a-z]+는 소문자 알파벳만 허용하기 때문에, 첫 글자인 숫자 3에 매칭 실패

            # import re
            # p = re.compile('[a-z]+')
            # m = p.match('python')
            # if m:
            #     print('Match found: ', m.group())           # Match found:  python
            # else:
            #     print('No match')

''' findall '''
# >>> import re
# >>> p = re.compile('[a-z]+')
# >>> result = p.findall("life is too short")
# >>> print(result)
# ['life', 'is', 'too', 'short']

''' finditer'''
# >>> import re
# >>> p = re.compile('[a-z]+')
# >>> result = p.finditer("life is too short")
# >>> print(result)
# <callable_iterator object at 0x75277d39f9d0>
# >>> for r in result: print(r)
# ... 
# <re.Match object; span=(0, 4), match='life'>
# <re.Match object; span=(5, 7), match='is'>
# <re.Match object; span=(8, 11), match='too'>
# <re.Match object; span=(12, 17), match='short'>

''' search '''
# >>> import re
# >>> p = re.compile('[a-z]+')
# >>> m = p.search('python')
# >>> print(m)
# <re.Match object; span=(0, 6), match='python'>

# >>> m=p.search('3 python')
# >>> print(m)
# <re.Match object; span=(2, 8), match='python'>

''' match 객체의 매서드 
        group   : 매치된 문자열 리턴
        start   : 매치된 문자열의 시작 위치 리턴
        end     : 매치된 문자열의 끝 위치 리턴
        span    : 매치된 문자열의 (시작, 끝)에 해당하는 튜플 리턴
'''
# >>> import re
# >>> p = re.compile('[a-z]+')
# >>> m=p.match('python')
# >>> m.group()
# 'python'
# >>> m.start()
# 0
# >>> m.end()
# 6
# >>> m.span()
# (0, 6)


''' 컴파일 옵션 :       정규식을 컴파일 할 때 사용할 수 있는 옵션
        DOTALL          S       .(dot)이 줄바꿈 문자를 포함해 모든 문자와 매치될 수 있게 함
        IGNORECASE      I       대소문자에 관계없이 매치될 수 있게 함
        MULTILINE       M       여러 줄과 매치될 수 있게 함. ^,$ 메타 문자 사용와 관계있는 옵션
        VERBOSE         X       verbose 모드를 사용할 수 있게 함. 정규식을 보기 편하게, 주석 등을 사용 가능케

'''

''' DOTALL, S   :  .(dot)이 줄바꿈 문자를 포함해 모든 문자와 매치될 수 있게 함 '''
# >>> p=re.compile('a.b', re.DOTALL)
# >>> m=p.match('a\nb')
# >>> print(m)
# <re.Match object; span=(0, 3), match='a\nb'>

''' IGNORECASE, I       :  대소문자에 관계없이 매치될 수 있게 함 '''
# >>> p=re.compile('[a-z]+',re.I)
# >>> p.match('python')
# <re.Match object; span=(0, 6), match='python'>
# >>> p.match('Python')
# <re.Match object; span=(0, 6), match='Python'>
# >>> p.match('PYTHON')
# <re.Match object; span=(0, 6), match='PYTHON'>

''' MULTILINE, M        :  여러 줄과 매치될 수 있게 함. ^,$ 메타 문자 사용와 관계있는 옵션 '''
# import re

# # python 다음에 공백이 오고(\s) 최소 한단어(\w+)가 ㅗ아야됨
# p=re.compile("^python\s\w+", re.MULTILINE)

# data='''
# python one
# life is too short
# python two
# you need python
# python three
# '''
# print(p.findall(data))                  # ['python one', 'python two', 'python three']



''' VERBOSE, X  : verbose 모드를 사용할 수 있게 함. 정규식을 보기 편하게, 주석 등을 사용 가능케 '''
import re
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')


# 1. 정규식 컴파일 (re.VERBOSE를 사용하여 가독성 높임)
charref = re.compile(r"""
&[#]                # 시작 문자 &#
(
        0[0-7]+     # 8진수 형태
        | [0-9]+    # 10진수 형태
        | x[0-9a-fA-F]+  # 16진수 형태
)
;                   # 세미콜론으로 마무리
""", re.VERBOSE)

# # 2. 찾은 숫자를 실제 문자로 바꿔주는 함수
# def convert_to_char(match):
#     code = match.group(1) # 괄호 안의 숫자 부분만 추출
#     if code.startswith('x'):
#         return chr(int(code[1:], 16)) # 16진수 -> 문자
#     elif code.startswith('0'):
#         return chr(int(code, 8))      # 8진수 -> 문자
#     else:
#         return chr(int(code))         # 10진수 -> 문자

# # 3. 실제 문자열에 적용
# text = "A는 &#65;이고, 콜론은 &#x3a;입니다."
# result = charref.sub(convert_to_char, text)

# print(result) 
# # 출력 결과: A는 A이고, 콜론은 :입니다.


''' 역슬래시 문제 '''
# >>> import re
# >>> p=re.compile('\\\\section')       # 파이썬은 \\를 하나의 \로 해석, \\\\ -> \\
# >>> p=re.compile(r'\\section')        # 문자열 앞에 r(Raw String)을 붙이면 \를 특수문자로 해석하지 않고 보이는대로 놔둠. \\ -> \\




