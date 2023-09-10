import math as m

altura=float(input("\nDigite a altura da lata: "))
raio=float(input("\nDigite o raio da lata: "))
volume= m.pi*raio**2*altura
print(f"\nO volume da lata é: {volume:.2f}\n")