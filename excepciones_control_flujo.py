
def busca_paises(paises, pais):

    try:
        return paises[pais]
    except KeyError:
        return None


paises = {"CO": "Colombia", "US": "United Stated"}

print(busca_paises(paises, "AR"))
