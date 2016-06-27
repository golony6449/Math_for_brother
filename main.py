#-*- coding: utf-8 -*-

#Math for brother
#Programming By golony
#Practice to SOLVE MATH PROBLEM

from os import system
import time
from random import randint
import calc

#Define fuction
def clear():
    system('CLS')
#END

print "���� ���� ����"
print "������ ����� ������ 10������ Ǯ�� ���ô�, \n"

#�ݺ�Ƚ��
do=10

symbol=raw_input("������ ���� ������ �����ϼ���.(����,����,����,������)")
level=int(raw_input("���̵��� ���ڷ� �Է����ּ���.(�������� 1)"))

if symbol=="����":
    for a in range(do):
        calc.plus(level)
elif symbol=="����":
    for a in range(do):
        calc.minus(level)
elif symbol=="����":
    for a in range(do):
        calc.multi(level)
elif symbol=='������':
    for a in range(do):
        calc.divine(level)
else:
    print "�ùٸ��� ���� �����Դϴ�"
    time.sleep(5)
    exit()
