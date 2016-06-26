#-*- coding: utf-8 -*-

#Math for brother
##Programming By golony
###Practice to SOLVE MATH PROBLEM

from os import system
import time
from random import randint

print "수학 문제 연습"
print "귀찮고 힘들어도 힘내서 한번 풀어 봅시다. \n"

symbol=raw_input("연습할 문제 유형을 선택하세요.(덧셈,뺄셈,곱셈,나눗셈)")
level=raw_input("난이도를 숫자로 입력해주세요.(예를들어 1)")

if symbol=="덧셈":
    while True:
        plus(level)
elif symbol=="뺄셈":
    while True:
        minus(level)
elif symbol=="곱셈":
    while True:
        multi(level)
elif symbol==(level):
    while True:
        divine(level)
else:
    print "올바르지 않은 유형입니다."
    time.sleep(5)
    exit()


###함수선언파트
def plus(level):
    clear()
    para1,para2=make_Q(level)
    print para1, ' + ',para2,' = ?'
    answer=raw_input('정답: ')

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
    answer=raw_input('정답: ')

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
    answer=raw_input('정답: ')

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
    answer=raw_input('정답: ')

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
