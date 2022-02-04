
# assert <expression boolean>, <mensaje de error>

def primera_letra(lista_palabras):

    primeras_letras = []

    for palabra in lista_palabras:

        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'No se permiten str vacios'

        primeras_letras.append(palabra[0])

    return primeras_letras


lista_palabras = ["mi mama", "lucia la luz", "tania te amo", ""]

print(primera_letra(lista_palabras))