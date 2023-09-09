import math as m

angulo=float(input("\nDigite um angulo em graus: "))
rang=m.radians(angulo)
print(f"\nSeno: {m.sin(rang)}\nCoseno: {m.cos(rang)}\nTangente: {m.tan(rang)}\nCosecante: {1/(m.cos(rang))}\nSecante: {1/(m.cos(rang))}\nCotangente: {1/(m.tan(rang))}\n")