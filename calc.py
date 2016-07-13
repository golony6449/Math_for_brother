#-*- coding: utf-8 -*-
from os import system
import time
from random import randint
import Tkinter

###CLASS 정의
###Define Class
class CALC(object):

##코드 재사용을 위해 init 중 상당수를 별도 함수로 분리
#For re-use code in __init__, move code to other fuction(initial_set)
    def __init__(self,cat):
        self.category=cat
        self.initial_set(textlabel='난이도를 입력해주세요. (1~)', answertext='난이도: ',para=1)
        self.gui.mainloop()


    def start(self):
        self.initial_set(answertext='정답 :')
        q=self.make_Q()
        self.gui.mainloop()

##Tk 윈도우 실행
#Generate Tk window with some argument.
#title: window's title, textlabel: text at the middle of window,
#answertext: left side of Entry widget, buttontext: Text on button widget
#para: decide which fuction is executed, initialize or show question
    def initial_set(self,title='수학문제연습',textlabel='생성중...',answertext='',buttontext='확인',para=0):
        self.gui = Tkinter.Tk()
        self.gui.title(title)
        self.up_frame = Tkinter.Frame(self.gui)
        self.up_frame.pack(side='top')
        self.bottom_frame = Tkinter.Frame(self.gui)
        self.bottom_frame.pack(side='bottom')

        #문제 부분
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
            print 'level set'
            self.ans_button = Tkinter.Button(self.bottom_frame, textvariable=self.buttontext, command=self.set_lev)
        else:
            self.ans_button=Tkinter.Button(self.bottom_frame,textvariable=self.buttontext,command=self.chk)
        self.ans_button.pack(side='left')

##확인버튼이 눌러졌을때 Entry위젯의 값을 얻고 정답과 비교하고 정답인 경우 새 문제를 생성한다
# When Button which is on Tk window is pressed,
# execute 'get from Entry widget, Compare with answer and regenerate new quesion when the answer is corrent'
    def chk(self):
        self.get()
        if self.input==self.ans:
            # test code
            print '성공'
            self.make_Q()

##initial_set 함수가 초기설정상태일때(para==1) 실행되어 난이도를 설정함
#Set the level when the fuction 'initial_set' is initialize mode
    def set_lev(self):
        self.level=self.get()
        self.gui.destroy()

#Entry에 있는 값을 정수형으로 반환함
#Return value in Entry widget, by int type
    def get(self):
        self.input=int(self.answer.get())
        return self.input

#일단 + 기준 개발(추후수정요망)
    def make_Q(self):
        indicator=self.category
        #print 'make_Q 실행!'
        print self.level
        para1 = randint(10 ** self.level, 10 ** (self.level + 1))
        para2 = randint(10 ** self.level, 10 ** (self.level + 1))
        if indicator==1:
            question = str(para1) + ' + ' + str(para2) +' = ?'
            self.ans=para1+para2
            self.set(question)
            return question
        elif indicator==2:
            question = str(para1) + ' - ' + str(para2) +' = ?'
            self.ans=para1+para2
            self.set(question)
            return question
        elif indicator==3:
            question = str(para1) + ' X ' + str(para2) +' = ?'
            self.ans=para1+para2
            self.set(question)
            return question
        elif indicator==4:
            question = str(para1) + ' ÷ ' + str(para2) +' = ?'
            self.ans=para1+para2
            self.set(question)
            return question

#GUI 중 내용부분을 매개변수(para)로 변경
#Change question part in GUI with 'para'
    def set(self,para):
        self.textlabel.set(para)