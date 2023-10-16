# Digite um valor e veja quantos dolares voce poderá comprar: R$
real = float(input("digite o valor em R$"))
dolar = float (input("digite a cotação atual do dolar"))
conversao = real / dolar 

print(f" Seu valor em dolar é {conversao:.2f} ")