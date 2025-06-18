# for numero in range(5):
#     print(numero, numero * " kepasa")

buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print('encontrado', buscar)
        break
else:
    print('no encontrado')

# iterable string
for char in 'clases python':
    print(char)
