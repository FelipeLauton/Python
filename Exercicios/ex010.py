dinheiro = float(input('Quanto você tem na carteira? R$'))
dolar = dinheiro / 5.21
print('Com a quantidade de R${:.2f}, você poderá comprar US${:.2f} '.format(dinheiro, dolar))
