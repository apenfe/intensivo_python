"""Escribir un programa que pregunte al usuario por el número de
 horas trabajadas y el coste por hora. Después debe mostrar por
 pantalla la paga que le corresponde."""

horas = int(input("Ingrese la horas trabajadas: "))
precio = float(input("Ingrese el precio: "))

print(f"Ha ganado {horas*precio:.2f} €")