"""Verificar si un texto que termina en punto es un palíndromo (capicúa). Un texto es
palíndromo si se lee lo mismo de izquierda a derecha o de derecha a izquierda. Ej: “Amor
a roma”."""
def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.replace('.','')
    palabra = palabra.lower()
    palabraInvertida = palabra[::-1]
    if palabra == palabraInvertida:
        return True
    else:
        return False

#funcion principal puede ser un main dos espacion en cada funcion
def run():
    palabra = input('Escribe una palabra: ')
    esPalindromo = palindromo(palabra)
    if esPalindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')

print(run())
