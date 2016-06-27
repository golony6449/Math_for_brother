#-*- coding: utf-8 -*-

#Math for brother
##Programming By golony
###Practice to SOLVE MATH PROBLEM

from os import system
import time
from random import randint
import calc

print "수학 문제 연습"
print "귀찮고 힘들어도 힘내서 한번 풀어 봅시다. \n"

symbol=raw_input("연습할 문제 유형을 선택하세요.(덧셈,뺄셈,곱셈,나눗셈)")
level=int(raw_input("난이도를 숫자로 입력해주세요.(예를들어 1)"))

if symbol=="덧셈":
    while True:
        calc.plus(level)
elif symbol=="뺄셈":
    while True:
        calc.minus(level)
elif symbol=="곱셈":
    while True:
        calc.multi(level)
elif symbol==(level):
    while True:
        calc.divine(level)
else:
    print "올바르지 않은 유형입니다."
    time.sleep(5)
    exit()

###함수선언파트
def clear():
    system('CLS')