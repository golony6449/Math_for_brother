#-*- coding: utf-8 -*-
#encode by cp949

from os import system
import time
from random import randint

def plus(level):
    clear()
    para1,para2=make_Q(level)
    print para1, ' + ',para2,' = ?'
    answer=int(raw_input('����: '))

    if answer==para1+para2:
        print '�����Դϴ�.'
        time.sleep(5)
    else:
        print 'Ʋ�Ƚ��ϴ�..'
        time.sleep(5)

def minus(level):
    clear()
    para1,para2=make_Q(level)
    print para1, ' - ',para2,' = ?'
    answer=int(raw_input('����: '))

    if answer==para1-para2:
        print '�����Դϴ�.'
        time.sleep(5)
    else:
        print 'Ʋ�Ƚ��ϴ�..'
        time.sleep(5)

def multi(level):
    clear()
    para1,para2=make_Q(level)
    print para1, ' X ',para2,' = ?'
    answer=int(raw_input('����: '))

    if answer==para1*para2:
        print '�����Դϴ�.'
        time.sleep(5)
    else:
        print 'Ʋ�Ƚ��ϴ�..'
        time.sleep(5)

def divine(level):
    clear()
    para1,para2=make_Q(level)
    print para1, ' / ',para2,' = ?'
    answer=int(raw_input('����: '))

    if answer==para1/para2:
        print '�����Դϴ�.'
        time.sleep(5)
    else:
        print 'Ʋ�Ƚ��ϴ�.'
        time.sleep(5)

def make_Q(level=-1):
    if level==-1:
        print "�ùٸ��� ���� ���̵��Դϴ�."
        return 0

    para1=randint(10**level,10**(level+1))
    para2=randint(10**level,10**(level+1))

    return para1,para2
def clear():
    system('CLS')
