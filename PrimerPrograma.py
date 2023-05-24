edadPapa = int(input("Indica la edad de tu papá: "))
edadMama = int(input("Indica la edad de tu mamá: "))
edadhermano = int(input("Indica la edad de tu hermano: "))
mayorEdad = max(edadMama, edadPapa, edadhermano)
menorEdad = min(edadMama, edadPapa, edadhermano)
print("el mayor de tu familia tiene", mayorEdad, "años")
print("el menor de tu familia tiene", menorEdad, "años")

print("el mayor de tu familia tiene {} años y el menor de tu familia tiene {} años".format
      (max(edadMama, edadPapa, edadhermano), min(edadMama, edadPapa, edadhermano)))