# CASO 13
from tkinter import E


nombre = input("Ingrese su nombre: ")
c_a = 0
c_e = 0
c_i = 0
c_o = 0
c_u = 0

for letra in nombre:
    if letra == "a":
        c_a += 1
    elif letra == "e":
        c_e += 1
    elif letra == "i":
        c_i += 1
    elif letra == "o":
        c_o += 1
    elif letra == "u":
        c_u += 1

print(f"hay {c_a} vocales a")
print(f"Hay {c_e} vocales e")
print(f"Hay {c_i} vocales i")
print(f"Hay {c_o} vocales o")
print(f"Hay {c_u} vocales u")

