print('Bienvenido a la calculadora V2')
print('Para salir de la calculadora escriba "Salir"')
print('Las operaciones son suma, resta, multi y div')

resultado = ""
while True:
    if not resultado:
        resultado = input("ingrese el primer numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input('ingrese la operacion: ')
    if op.lower() == "salir":
        break
    n2 = input('ingrese el segundo numero: ')
    if n2.lower() == 'salir':
        break
    n2 = int(n2)

    if op.lower() == ('suma'):
        resultado += n2
    elif op.lower() == ('resta'):
        resultado -= n2
    elif op.lower() == ('multi'):
        resultado *= n2
    elif op.lower() == ('div'):
        resultado /= n2
    else:
        print('Operacion no valida')
        break
    print(f'El resultado es {resultado}')

# Si ingresa un str a el input de numeros falla la app
