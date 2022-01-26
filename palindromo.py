
# Evalua si una palabra es un palindromo o no
def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()

    palabra_invertida = palabra[::-1]

    return palabra_invertida == palabra

# Programa principal 
def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)

    if es_palindromo == True:
        print('Es palindromo')
    else:
        print("No es palindromo")


# Punto de entrada para el programa de python
if __name__ == "__main__":
    run()

