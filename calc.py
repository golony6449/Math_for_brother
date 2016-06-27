#-*- coding: utf-8 -*-
from os import system
import time
from random import randint

###함수선언파트
def plus(level):
    clear()
    para1,para2=make_Q(level)
    print para1, ' + ',para2,' = ?'
    answer=int(raw_input('정답: '))

    if answer==para1+para2:
        print '정답입니다.'
        time.sleep(5)
    else:
        print '오답입니다.'
        time.sleep(5)

def minus(level):
    clear()
    para1,para2=make_Q(level)
    print para1, ' - ',para2,' = ?'
    answer=int(raw_input('정답: '))

    if answer==para1-para2:
        print '정답입니다.'
        time.sleep(5)
    else:
        print '오답입니다.'
        time.sleep(5)

def multi(level):
    clear()
    para1,para2=make_Q(level)
    print para1, ' X ',para2,' = ?'
    answer=int(raw_input('정답: '))

    if answer==para1*para2:
        print '정답입니다.'
        time.sleep(5)
    else:
        print '오답입니다.'
        time.sleep(5)

def divine(level):
    clear()
    para1,para2=make_Q(level)
    print para1, ' / ',para2,' = ?'
    answer=int(raw_input('정답: '))

    if answer==para1/para2:
        print '정답입니다.'
        time.sleep(5)
    else:
        print '오답입니다.'
        time.sleep(5)

def make_Q(level=-1):
    if level==-1:
        print "올바른 난이도를 입력해주세요."
        return 0

    para1=randint(10**level,10**(level+1))
    para2=randint(10**level,10**(level+1))

    return para1,para2
def clear():
    system('CLS')