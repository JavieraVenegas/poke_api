

from get_module import get_info

from get_module import get_info

def procesa_tipos(lista_tipos, caracteristicas):
    tipos_total = []
    for type in lista_tipos:
        url3 = f"https://pokeapi.co/api/v2/type/{type}"

        datos_type = get_info(url3)
        lista_sec = datos_type["damage_relations"][caracteristicas]

        for item in lista_sec:
            tipos_total.append(item["name"])

    
    tipos_total_filtrado = set(tipos_total)
    tipos_total = list(tipos_total_filtrado)
    tipos_total.sort()


    return tipos_total

