deposito=float(input("\nEntre com depósito: "))
taxa=float(input("\nEntre com a taxa de juros: "))
valor=deposito*taxa/100
total=deposito+valor
print(f"\nRendimentos: {total:.2f}\nTotal: {total:.2f}\n")