# crie um programa que leia quanto dinheiro tem
# na carteira e mostre quantos dolar ele pode comprar(USS 1.00 = R$ 3,27)
money = float(input('Quanto dinheiro voce tem'))
cota = float(3.27)
dolar = float(money/cota)
print("voce tem USS {:.2f}".format(dolar),"Dolar")