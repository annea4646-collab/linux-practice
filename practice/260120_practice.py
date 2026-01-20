''' glob(global pattern matching) : 특정 디렉터리 안의 파일 이름을 읽어서 리스트로 리턴 '''
# >>> import glob
# >>> glob.glob("D:\\doit\\practice\\26*")
# []
# >>> glob.glob("/mnt/d/doit/practice/26*")         # *는 임의의 길이(0개 이상) 문자열
# ['/mnt/d/doit/practice/260112_practice.py', '/mnt/d/doit/practice/260113_practice.py', '/mnt/d/doit/practice/260115_practice.py', '/mnt/d/doit/practice/260119_practice.py', '/mnt/d/doit/practice/260120_practice.py']
# >>> glob.glob("/mnt/d/doit/practice/2?")          # ?는 1자리 문자열
# []


''' pickle /    1. pickle.dump '''
# >>> import pickle
# >>> f=open("text.txt", "wb")
# >>> data={1:'python', 2:'you need'}
# >>> pickle.dump(data,f)
# >>> f.close()

''' pickle /    2. pickle.load '''
# >>> import pickle
# >>> f=open("text.txt", "rb")
# >>> data=pickle.load(f)
# >>> print(data)
# {1: 'python', 2: 'you need'}
# >>> f.close()


# >>> import pickle
# >>> with open("text.txt", "rb") as f:
# ...     data=pickle.load(f)
# ...     print(data)
# ... 
# {1: 'python', 2: 'you need'}


''' OS / os.environ : 현재 시스템의 환경 변수값을 리턴 '''
# >>> import os
# >>> os.environ
# environ({'SHELL': '/bin/bash', 'COLORTERM': 'truecolor', 'VSCODE_DEBUGPY_ADAPTER_ENDPOINTS': '/home/annea4646/.vscode-server/extensions/ms-python.debugpy-2025.18.0-linux-x64/.noConfigDebugAdapterEndpoints/endpoint-dd874e56b5e22000.txt', 'WSL2_GUI_APPS_ENABLED': '1', 'TERM_PROGRAM_VERSION': '1.108.1', 'WSL_DISTRO_NAME': 'Ubuntu-22.04', 'PYDEVD_DISABLE_FILE_VALIDATION': '1', 'NAME': 'DESKTOP-HBGCDB3', 'PWD': '/home/annea4646', 'LOGNAME': 'annea4646', 'BUNDLED_DEBUGPY_PATH': '/home/annea4646/.vscode-server/extensions/ms-python.debugpy-2025.18.0-linux-x64/bundled/libs/debugpy', 'VSCODE_GIT_ASKPASS_NODE': '/home/annea4646/.vscode-server/bin/585eba7c0c34fd6b30faac7c62a42050bfbc0086/node', 'HOME': '/home/annea4646', 'LANG': 'C.UTF-8', 'WSL_INTEROP': '/run/WSL/365_interop', 'LS_COLORS': 'rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:', 'PYTHONSTARTUP': '/home/annea4646/.vscode-server/data/User/workspaceStorage/1ac0bd946d84f1217aed6dea9bcee2c5/ms-python.python/pythonrc.py', 'WAYLAND_DISPLAY': 'wayland-0', 'GIT_ASKPASS': '/home/annea4646/.vscode-server/bin/585eba7c0c34fd6b30faac7c62a42050bfbc0086/extensions/git/dist/askpass.sh', 'VSCODE_GIT_ASKPASS_EXTRA_ARGS': '', 'VSCODE_PYTHON_AUTOACTIVATE_GUARD': '1', 'LESSCLOSE': '/usr/bin/lesspipe %s %s', 'TERM': 'xterm-256color', 'PYTHON_BASIC_REPL': '1', 'LESSOPEN': '| /usr/bin/lesspipe %s', 'USER': 'annea4646', 'VSCODE_GIT_IPC_HANDLE': '/run/user/1000/vscode-git-7dc9ffc5bc.sock', 'DISPLAY': ':0', 'SHLVL': '1', 'XDG_RUNTIME_DIR': '/run/user/1000/', 'WSLENV': 'VSCODE_WSL_EXT_LOCATION/up', 'VSCODE_GIT_ASKPASS_MAIN': '/home/annea4646/.vscode-server/bin/585eba7c0c34fd6b30faac7c62a42050bfbc0086/extensions/git/dist/askpass-main.js', 'XDG_DATA_DIRS': '/usr/local/share:/usr/share:/var/lib/snapd/desktop', 'PATH': '/home/annea4646/.vscode-server/bin/585eba7c0c34fd6b30faac7c62a42050bfbc0086/bin/remote-cli:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/lib/wsl/lib:/mnt/c/Program Files (x86)/VMware/VMware Workstation/bin/:/mnt/c/WINDOWS/system32:/mnt/c/WINDOWS:/mnt/c/WINDOWS/System32/Wbem:/mnt/c/WINDOWS/System32/WindowsPowerShell/v1.0/:/mnt/c/WINDOWS/System32/OpenSSH/:/mnt/c/Program Files/Git/cmd:/mnt/c/Users/403_28/AppData/Local/Programs/Python/Python311/Scripts/:/mnt/c/Users/403_28/AppData/Local/Programs/Python/Python311/:/mnt/c/Users/403_28/AppData/Local/Microsoft/WindowsApps:/mnt/c/Users/403_28/AppData/Local/Programs/Microsoft VS Code/bin:/snap/bin:/home/annea4646/.vscode-server/extensions/ms-python.debugpy-2025.18.0-linux-x64/bundled/scripts/noConfigScripts', 'DBUS_SESSION_BUS_ADDRESS': 'unix:path=/run/user/1000/bus', 'HOSTTYPE': 'x86_64', 'PULSE_SERVER': 'unix:/mnt/wslg/PulseServer', 'TERM_PROGRAM': 'vscode', 'VSCODE_IPC_HOOK_CLI': '/run/user/1000/vscode-ipc-8b5e3ec7-27a8-452c-9f89-310722af06f2.sock', '_': '/usr/bin/python3'})
# >>> os.environ['PATH']
# '/home/annea4646/.vscode-server/bin/585eba7c0c34fd6b30faac7c62a42050bfbc0086/bin/remote-cli:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/lib/wsl/lib:/mnt/c/Program Files (x86)/VMware/VMware Workstation/bin/:/mnt/c/WINDOWS/system32:/mnt/c/WINDOWS:/mnt/c/WINDOWS/System32/Wbem:/mnt/c/WINDOWS/System32/WindowsPowerShell/v1.0/:/mnt/c/WINDOWS/System32/OpenSSH/:/mnt/c/Program Files/Git/cmd:/mnt/c/Users/403_28/AppData/Local/Programs/Python/Python311/Scripts/:/mnt/c/Users/403_28/AppData/Local/Programs/Python/Python311/:/mnt/c/Users/403_28/AppData/Local/Microsoft/WindowsApps:/mnt/c/Users/403_28/AppData/Local/Programs/Microsoft VS Code/bin:/snap/bin:/home/annea4646/.vscode-server/extensions/ms-python.debugpy-2025.18.0-linux-x64/bundled/scripts/noConfigScripts'

''' os.chdir : 현재 디렉터리 위치 변경 '''
# >>> import os
# >>> os.chdir("/mnt/d/doit")
''' os.getcwd : 현재 자신의 디렉터리 위치를 리턴 '''
# >>> os.getcwd()
# '/mnt/d/doit'
''' os.system : 시스템 자체 프로그램이나 기타 명령어 호출 '''
# >>> os.system("dir")
# __pycache__  app.py  class  doing  game  mod1.py  mod2.py  modtest.py  mymod  practice  text.txt
# 0
''' 기타 유용한 os 관련 함수'''
# >>> import os
# >>> os.mkdir("new_folder")                        # 디렉터리 생성
# >>> os.rmdir("new_folder")                        # 디렉터리 삭제
# >>> os.remove("test/test.py")                     # 파일 삭제
# >>> os.system("touch test/test.txt")              # 파일 생성
# >>> os.rename("test/test.txt","test/test1.txt")   # test.txt를 test1.txt로 파일명 변경

''' zipfile : 여러개의 파일을 zip 형식으로 합치거나 해제(extractall)할 때 사용하는 모듈 '''
# import zipfile
# import os

# if not os.path.exists('zip'):  
#     os.mkdir('zip')                                         # zip 폴더 생성

# for name in ['zip/a.txt','zip/b.txt','zip/c.txt']:          # a,b,c.txt 파일 생성
#     with open(name, 'w') as f:
#         f.write(f"This is {name} content")

# with zipfile.ZipFile('zip/mytext.zip','w') as myzip:         # mytext.zip에 파일을 복사해서 압축
#     myzip.write('zip/a.txt', arcname='a.txt')
#     myzip.write('zip/b.txt', arcname='b.txt')
#     myzip.write('zip/c.txt', arcname='c.txt')

# with zipfile.ZipFile('zip/mytext.zip') as myzip:
#     myzip.extractall('zip/output_folder')                   # mytext.zip 안의 파일을 output_folder폴더에 풀기

''' zipfile : 합친 파일에서 특정파일만 해제(extract) '''
# import zipfile

# with zipfile.ZipFile('zip/mytext.zip') as myzip:
#     myzip.extract('a.txt', path='zip')                        # a.txt 파일을 zip 폴더에 풀기기




''' Threading   1. 쓰레드 사용하지 않을 때 '''
# import time

# def long_task():
#     for i in range(5):
#         time.sleep(1)
#         print("working:%s\n" % i)
# print("Start")
# start = time.time()                         # 시작 시간 기록

# for i in range(5):
#     long_task()

# end = time.time()                           # 종료 시간 기록
# print("End")
# print("걸린 시간: %.2f초" %(end - start))               # 결과값: 걸린 시간: 23.12초


''' Threading   2. 쓰레드 사용할 때 '''
# import time
# import threading

# def long_task():                                    # 여기서 long_task => Python 바이트코드
#     for i in range(5):
#         time.sleep(1)
#         print("working:%s\n" % i)
# print("Start")
# start = time.time()                                 # 시작 시간 기록

# threads = []
# for i in range(5):
#     t = threading.Thread(target=long_task)          # 쓰레드 (일꾼) 5개 생성
#     threads.append(t)                               # threads라는 명단에 담아두기

# for t in threads:
#     t.start()                                       # 쓰레드 실행, 거의 동시에 일꾼 다섯이 1초씩 쉬면서 working:i 출력

# for t in threads:
#     t.join()                                        # 쓰레드 종료 대기, 일꾼 다섯이 모두 long_task를 마칠때까지 대기

# end = time.time()
# print("End")                                        # 종료 시간 기록
# print("걸린 시간: %.2f초" % (end - start))              # 결과값: 걸린 시간: 5.08초



''' Multi-process
     - CPU는 하나(혹은 그 이상이)지만, 그 안의 여러 코어들이 여러 프로세스를 동시에 실행 
     - 멀티프로세싱이 멀티스레딩보다 강력한 이유는 
       각 프로세스가 개별적인 파이썬 인터프리터와 바이트코드 실행 환경을 통째로 갖기 때문
        => long_task 5개를 동시에 실행해도 서로 방해받지 않고 끝날 수 있음
'''

# import time
# import multiprocessing

# def long_task():                                    # long_task => 직렬화되어 자식 프로세스로 전달되는 실행 단위(함수 객체)
#     for i in range(5):                              
#         time.sleep(1)
#         print("working:%s\n" % i)

# if __name__ == "__main__":

#     print("Start")
#     start = time.time()                                 # 시작 시간 기록

#     processes = []

#     for i in range(5):
#         p = multiprocessing.Process(target=long_task)     # 프로세서 생성      
#         processes.append(p)                               

#     for t in processes:
#         t.start()                                         # 프로세스 시작 : 각 프로세스는 독립된 GIL을 가지고 전달받은 Bytecode를 각자의 CPU 코어에서 실행                     

#     for t in processes:
#         t.join()                                          # 프로세스 종료 대기                               

#     end = time.time()
#     print("End")                                        # 종료 시간 기록
#     print("걸린 시간: %.2f초" % (end - start))              # 결과값: 걸린 시간: 5.09초


''' tempfile : 파일을 임시로 만들어서 사용할 때 유용 '''
''' tempfile.mkstemp : 중복되지 않는 임시 파일 이름을 무작위로 만들어 리턴 '''
# >>> import tempfile
# >>> filename=tempfile.mkstemp()
# >>> filename
# (3, '/tmp/tmpwsps02mq')
# >>> filename=tempfile.mkstemp()
# >>> filename
# (4, '/tmp/tmp1lxn9p9m')
# >>> filename=tempfile.mkstemp()
# >>> filename
# (5, '/tmp/tmp941s6suq')

''' traceback : 프로그램 실행 중 발생한 오류 추적 '''
# import traceback

# def a():
#     return 1 / 0

# def b():
#     a()

# def main():
#     try:
#         b()
#     except:
#         print("오류가 발생했습니다.")
#         print(traceback.format_exc())
# main()                                  # 결과값: 오류가 발생했습니다.
                                                # Traceback (most recent call last):
                                                #   File "/home/annea4646/doit/practice/260120_practice.py", line 195, in main
                                                #     b()
                                                #   File "/home/annea4646/doit/practice/260120_practice.py", line 191, in b
                                                #     a()
                                                #   File "/home/annea4646/doit/practice/260120_practice.py", line 188, in a
                                                #     return 1 / 0
                                                # ZeroDivisionError: division by zero


''' JSON    json.load() : JSON 형태의 데이터로 만든 파일을 읽어 (딕셔너리로) 변환'''
# import json

# with open('practice/myinfo.json', encoding='utf-8') as f:
#     raw_text = f.read()                        # 파일의 raw data를 읽음
#     print(f"json 파일 타입: {type(raw_text)}")       # json 파일 타입: <class 'str'>
#     f.seek(0)

#     data=json.load(f)
#     print(data)
#     print(f"json.load 후 타입: {type(data)}")   # json.load 후 타입: <class 'dict'>

# if isinstance(data, dict):
#     for key in data.keys():
#         print(f"키: {key}, 값의 타입: {type(data[key])}")

''' JSON    json.dumps() : 파이썬 자료형을 json 문자열로 만들기 '''
import json

d = {'name': "홍길자", 'birth': '1112', 'age': 30}
json_data = json.dumps(d)
print(json_data)                  # {"name": "\ud64d\uae38\uc790", "birth": "1112", "age": 30} => 비영어권 문자를 유니코드로 변환

''' JSON    json.loads() : json 문자열을 딕셔너리로 변환 '''
print(json.loads(json_data))      # {'name': '홍길자', 'birth': '1112', 'age': 30}





''' 외부 라이브러리 '''
''' pip : 파이썬 모듈이나 패키지를 쉽게 설치할 수 있도록 도와주는 도구 '''
# pip install SomePackage           : SomePackage 설치
# pip uninstall SomePackage         : 설치한 패키지 삭제
# pip install SomePackage==1.0.4    : 특정 버전 설치
# pip install SomePackage           : 버전 생략 시 최신 버전 설치

# pip install --upgrade SomePackage : 최신버전으로 업그레이드
# pip list                          : 설치된 패키지 확인

# pip show pip                      : pip라는 패키지의 버전 정보 확인

        # 리눅스에서는 pip3 명령어 입력
            # annea4646@DESKTOP-HBGCDB3:~/doit$ pip3 show pip
            # Name: pip
            # Version: 22.0.2
            # ...
 

# >>> import requests
# >>> response = requests.get("https://www.google.com")
# >>> print(f"응답 코드: {response.status_code}")
# 응답 코드: 200                    # 성공적으로 연결됨