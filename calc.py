#-*- coding: utf-8 -*-
from os import system
import time
from random import randint
import Tkinter

###CLASS 정의
class CALC(object):

    def __init__(self):
        self.gui = Tkinter.Tk()
        self.gui.title('수학 문제 연습')
        self.up_frame = Tkinter.Frame(self.gui)
        self.up_frame.pack(side='top')
        self.bottom_frame = Tkinter.Frame(self.gui)
        self.bottom_frame.pack(side='bottom')

        #문제 부분
        self.level = 0
        self.textvar = Tkinter.StringVar().set('생성중')
        self.text = Tkinter.Label(self.up_frame, textvariable=self.textvar)
        self.text.pack()

        #정답부분
        self.answer=Tkinter.Entry(self.bottom_frame)
        self.answer.pack(side='left')
        self.ans_button=Tkinter.Button(self.bottom_frame,text='정답!',command=self.chk)
        self.ans_button.pack(side='left')

    def chk(self):
        level=int(self.answer.get())
        print '레벨:',level
        self.make_Q(level)

    def make_Q(self,level):
        para1 = randint(10 ** level, 10 ** (level + 1))
        para2 = randint(10 ** level, 10 ** (level + 1))
        question = str(para1) + ' + ' + str(para2) +' = ?'
        textvar=question

###함수선언파트
def plus():
    clear()
    process=CALC()

def minus(level):
    clear()
    level = set_level()
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
    level = set_level()
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
    level = set_level()
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

def set_level():
    gui = Tkinter.Tk()
    gui.title('난이도')
    up_frame = Tkinter.Frame(gui)
    up_frame.pack(side='top')
    bottom_frame = Tkinter.Frame(gui)
    bottom_frame.pack(side='bottom')

    lev = int(raw_input("난이도를 숫자로 입력해주세요.(예를들어 1)"))
    return lev