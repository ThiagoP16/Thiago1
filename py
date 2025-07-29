Diccionario = {
    'CRINGE': 'una respuesta común a algo raro o bizarro',
    'LOL': 'una respuesta a algo bastante gracioso',
    'SHEESH': 'una manera de sorprenderse',
    'CREEPY': 'algo bastante aterrador o espeluznante'
}

palabra = input('Escribe una palabra que no entiendas (Todo en mayúsculas)')

if palabra in Diccionario.keys():
    print(palabra, 'es', Diccionario[palabra])
