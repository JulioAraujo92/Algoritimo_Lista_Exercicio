sm=float(input("\nEntre com o salário mínimo: "))
qtd=float(input("\nEntre com a quantidade de Quilowatt: "))
preco=sm/700
vp=preco*qtd
vd=vp*0.9
print(f"\nPreço do quilowatt: {preco:.3}\nValor a ser pago: {vp:.3}\nValor com desconto: {vd:.3}\n")
