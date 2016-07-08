#-*- coding: utf-8 -*-

#Math for brother
##Programming By golony
###Practice to SOLVE MATH PROBLEM

from os import system
import time
from random import randint
from calc import *
import Tkinter

def plus():
    gui.destroy()
    process=CALC(1)
    process.start()
def minus():
    gui.destroy()
    process=CALC(2)
    process.start()
def multi():
    gui.destroy()
    process=CALC(3)
    process.start()
def divine():
    gui.destroy()
    process=CALC(4)
    process.start()

gui=Tkinter.Tk()
gui.title('수학 문제 연습')
up_frame=Tkinter.Frame(gui)
up_frame.pack(side='top')
bottom_frame=Tkinter.Frame(gui)
bottom_frame.pack(side='bottom')

text=Tkinter.Label(up_frame,text='수학문제연습')
text.pack()
text=Tkinter.Label(up_frame,text='귀찮고 힘들어도 힘내서 10문제만 풀어 봅시다.')
text.pack()

plus_button=Tkinter.Button(bottom_frame,text='덧셈',command=plus).pack(side='left')
minus_button=Tkinter.Button(bottom_frame,text='뺄셈',command=minus).pack(side='left')
multi_button=Tkinter.Button(bottom_frame,text='곱셈',command=multi).pack(side='left')
divine_button=Tkinter.Button(bottom_frame,text='나눗셈',command=divine).pack(side='left')

gui.mainloop()