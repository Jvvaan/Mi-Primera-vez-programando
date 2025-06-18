n1 = input("Ingrese primer numero: ")
n2 = input("Ingrese segundo numero: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

Mensaje = f""" 
Los resultados de los numeros {n1} y {n2} son:
el resultado de la suma es: {suma}
el resultado de la resta es: {resta}
el resultado de la multiplicacion es: {multi}
el resultado de la division es: {div}
"""

print(Mensaje)
