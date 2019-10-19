#faça um programa que leia um angulo qualquer e mostre
# na tela o valor do seno, cosseno e tangente desse angulo
import math

ang = float(input('digite angulo :'))
se = math.sin(math.radians(ang))
co = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print('Angulo :{: .2f}\nSeno :{: .2f}\nCosseno :{:.2f} \ntangente :{: .2f}'.format(ang, se, co, tang))