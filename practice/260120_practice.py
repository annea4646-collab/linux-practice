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
# >>> os.getcwd()
# '/mnt/d/doit'

# >>> os.system("dir")
# __pycache__  app.py  class  doing  game  mod1.py  mod2.py  modtest.py  mymod  practice  text.txt
# 0

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



''' Multi-process : CPU는 하나(혹은 그 이상이)지만, 그 안의 여러 코어들이 여러 프로세스를 동시에 실행 '''
import time
import multiprocessing

def long_task():                                    # 여기서 long_task => Python 바이트코드
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

if __name__ == "__main__":

    print("Start")
    start = time.time()                                 # 시작 시간 기록

    processes = []

    for i in range(5):
        p = multiprocessing.Process(target=long_task)          
        processes.append(p)                               

    for t in processes:
        t.start()                                       

    for t in processes:
        t.join()                                        

    end = time.time()
    print("End")                                        # 종료 시간 기록
    print("걸린 시간: %.2f초" % (end - start))              # 결과값: 걸린 시간: 5.09초