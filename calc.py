#-*- coding: utf-8 -*-
from os import system
import time
from random import randint
import Tkinter

###CLASS 정의
class CALC(object):

    def __init__(self):
        self.initial_set(textlabel='난이도를 입력해주세요. (1~)', answertext='난이도: ',para=1)

    def start(self):
        print self.level
        self.initial_set(answertext='정답 :')
        q=self.make_Q(self.level)
        self.set(q)


    def initial_set(self,title='수학문제연습',textlabel='생성중...',answertext='',buttontext='확인',para=0):
        self.gui = Tkinter.Tk()
        self.gui.title(title)
        self.up_frame = Tkinter.Frame(self.gui)
        self.up_frame.pack(side='top')
        self.bottom_frame = Tkinter.Frame(self.gui)
        self.bottom_frame.pack(side='bottom')

        #문제 부분
        self.level = 0
        self.textlabel = Tkinter.StringVar()
        self.textlabel.set(textlabel)
        self.text = Tkinter.Label(self.up_frame, textvariable=self.textlabel)
        self.text.pack()

        #정답부분
        self.input=0
        self.answertext=Tkinter.StringVar()
        self.answertext.set(answertext)
        self.buttontext=Tkinter.StringVar()
        self.buttontext.set(buttontext)

        self.answerlabel=Tkinter.Label(self.bottom_frame,textvariable=self.answertext)
        self.answerlabel.pack(side='left')
        self.answer=Tkinter.Entry(self.bottom_frame)
        self.answer.pack(side='left')
        if para==1:
            self.ans_button = Tkinter.Button(self.bottom_frame, textvariable=self.buttontext, command=self.set_lev)
        else:
            self.ans_button=Tkinter.Button(self.bottom_frame,textvariable=self.buttontext,command=self.get)
        self.ans_button.pack(side='left')

        self.gui.mainloop()

    def set_lev(self):
        self.level=self.get()
        self.gui.destroy()

    def get(self):
        self.input=int(self.answer.get())

    def make_Q(self,level):
        print 'make_Q 실행!'
        para1 = randint(10 ** level, 10 ** (level + 1))
        para2 = randint(10 ** level, 10 ** (level + 1))
        question = str(para1) + ' + ' + str(para2) +' = ?'
        return question

    def set(self,para):
        self.textlabel.set('test')

    def return_para(self,level=0):
        if level==1:
            return self.level

###함수선언파트
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

