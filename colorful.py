import platform
from sys import stdout

if platform.system()=="Linux":
    pass
else: 
    from colorama import init
    init()

# Do you like the elegance of Chinese characters?
def print红(*kw,**kargs):
    print("\033[0;31m",*kw,"\033[0m",**kargs)
def print绿(*kw,**kargs):
    print("\033[0;32m",*kw,"\033[0m",**kargs)
def print黄(*kw,**kargs):
    print("\033[0;33m",*kw,"\033[0m",**kargs)
def print蓝(*kw,**kargs):
    print("\033[0;34m",*kw,"\033[0m",**kargs)
def print紫(*kw,**kargs):
    print("\033[0;35m",*kw,"\033[0m",**kargs)
def print靛(*kw,**kargs):
    print("\033[0;36m",*kw,"\033[0m",**kargs)

def print亮红(*kw,**kargs):
    print("\033[1;31m",*kw,"\033[0m",**kargs)
def print亮绿(*kw,**kargs):
    print("\033[1;32m",*kw,"\033[0m",**kargs)
def print亮黄(*kw,**kargs):
    print("\033[1;33m",*kw,"\033[0m",**kargs)
def print亮蓝(*kw,**kargs):
    print("\033[1;34m",*kw,"\033[0m",**kargs)
def print亮紫(*kw,**kargs):
    print("\033[1;35m",*kw,"\033[0m",**kargs)
def print亮靛(*kw,**kargs):
    print("\033[1;36m",*kw,"\033[0m",**kargs)

<<<<<<< HEAD


def print亮红(*kw,**kargs):
    print("\033[1;31m",*kw,"\033[0m",**kargs)
def print亮绿(*kw,**kargs):
    print("\033[1;32m",*kw,"\033[0m",**kargs)
def print亮黄(*kw,**kargs):
    print("\033[1;33m",*kw,"\033[0m",**kargs)
def print亮蓝(*kw,**kargs):
    print("\033[1;34m",*kw,"\033[0m",**kargs)
def print亮紫(*kw,**kargs):
    print("\033[1;35m",*kw,"\033[0m",**kargs)
def print亮靛(*kw,**kargs):
    print("\033[1;36m",*kw,"\033[0m",**kargs)
    
print_red = print红
print_green = print绿
print_yellow = print黄
print_blue = print蓝
print_purple = print紫
print_indigo = print靛

print_bold_red = print亮红
print_bold_green = print亮绿
print_bold_yellow = print亮黄
print_bold_blue = print亮蓝
print_bold_purple = print亮紫
print_bold_indigo = print亮靛
    
if not stdout.isatty():
    # redirection, avoid a fucked up log file
    print红 = print
    print绿 = print
    print黄 = print
    print蓝 = print
    print紫 = print
    print靛 = print
    print亮红 = print
    print亮绿 = print
    print亮黄 = print
    print亮蓝 = print
    print亮紫 = print
    print亮靛 = print
    print_red = print
    print_green = print
    print_yellow = print
    print_blue = print
    print_purple = print
    print_indigo = print
    print_bold_red = print
    print_bold_green = print
    print_bold_yellow = print
    print_bold_blue = print
    print_bold_purple = print
    print_bold_indigo = print
=======
# Do you like the elegance of Chinese characters?
def sprint红(*kw):
    return "\033[0;31m"+' '.join(kw)+"\033[0m"
def sprint绿(*kw):
    return "\033[0;32m"+' '.join(kw)+"\033[0m"
def sprint黄(*kw):
    return "\033[0;33m"+' '.join(kw)+"\033[0m"
def sprint蓝(*kw):
    return "\033[0;34m"+' '.join(kw)+"\033[0m"
def sprint紫(*kw):
    return "\033[0;35m"+' '.join(kw)+"\033[0m"
def sprint靛(*kw):
    return "\033[0;36m"+' '.join(kw)+"\033[0m"
def sprint亮红(*kw):
    return "\033[1;31m"+' '.join(kw)+"\033[0m"
def sprint亮绿(*kw):
    return "\033[1;32m"+' '.join(kw)+"\033[0m"
def sprint亮黄(*kw):
    return "\033[1;33m"+' '.join(kw)+"\033[0m"
def sprint亮蓝(*kw):
    return "\033[1;34m"+' '.join(kw)+"\033[0m"
def sprint亮紫(*kw):
    return "\033[1;35m"+' '.join(kw)+"\033[0m"
def sprint亮靛(*kw):
    return "\033[1;36m"+' '.join(kw)+"\033[0m"
>>>>>>> upstream/master
