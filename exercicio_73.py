num=float(input("\nEntre com um número com parte fracionária: "))
numi=round((num-0.5))
numfrac=num-numi
numa=round(num+0.00001)
print(f"\nParte inteira: {numi}\nParte fracionária: {numfrac:.3f}\nNúmero arredondado: {numa}\n")