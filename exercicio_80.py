quant=float(input("\nDigite a quantidade de fitas: "))
valAluguel=float(input("\nDigite o valor do aluguel: "))
fatAnual=quant/3*valAluguel*12
multas=valAluguel*0.1*(quant/3)/10
quantFinal=(quant-(quant*0.02))+(quant/10)
print(f"\nFaturamento anual: {fatAnual:.2f}\nMultas mensais: {multas:.2f}\nQuantidade de fitas no final do anto: {quantFinal:.0f}\n")