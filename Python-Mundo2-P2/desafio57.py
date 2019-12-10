'''
desafio57
	faça um programa que leia o sexo de uma pessoa,
	mas só aceite os valores M ou F.
	caso esteja errado, peça a digitação novamente até ter um valor correto
'''

sexo = str(input('Digite seu sexo :')).strip().upper()
while  'M'!= sexo !='F' :
    sexo = str(input('Digite Novamente o sexo :')).upper().strip()
else:
    print ('sexo ok')


