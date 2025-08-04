import random

caracteres = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

longitud = int(input('ingrese la longitud de la contraseña: '))

contrasena = ''

for i in range(longitud):
    contrasena += random.choice(caracteres)

print(contrasena)
