import time
convercion = input('Como quiere hacer la converción, de Celsius a Fahrenheit o viceversa?(Escriba Celsius para Celsius a Fahrenheit y viceversa(Todo en mayúsculas)): ')

if convercion == 'CELSIUS':
    cantidadC = int(input('Cuantos grados Celsius quiere convertir a Fahrenheit?: '))
    celsius = cantidadC
    cantidadC *= 1.8
    cantidadC += 32
    print('Haciendo calculo')
    time.sleep(2)
    print(celsius, 'Grados Celsius, son', cantidadC, 'grados Fahrenheit')
elif convercion == 'FAHRENHEIT':
    cantidadF = int(input('Cuantos grados Fahrenheit quiere convertir a Celsius?: '))
    fahrenheit = cantidadF
    cantidadF -= 32
    cantidadF *= 0.5556
    print('Haciendo calculo')
    time.sleep(2)
    print(fahrenheit, 'Grados Fahrenheit, son', cantidadF, 'grados Celsius')
