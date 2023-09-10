base=float(input("\nDigite base: "))
altura=float(input("\nDigite altura: "))
perimetro=2*(base+altura)
area=base*altura
diagonal=(base**2 + altura**2)**0.5
print(f"\nPerimetro: {perimetro}\nArea: {area}\nDiagonal: {diagonal:.2f}\n")