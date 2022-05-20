from get_module import get_info
from poke_validation import validate
from string import Template
from ataque_pokemon import procesa_tipos
from span import genera_span
import random



print('Nota: Si el pokémon tiene espacios reemplace por "-". No coloque ningún tipo de signo de puntuación adicional.')
nombre = input("Introduzca el nombre del Pokemon a procesar: ")

nombre = validate(nombre)
poke_nombre = nombre.capitalize()
print(poke_nombre)

#consultar id
url1 =  f"https://pokeapi.co/api/v2/pokemon/{nombre}"

datos_base = get_info(url1)

poke_id = datos_base["id"]
print(datos_base["id"])

#acá la imagen
poke_img = datos_base["sprites"]["other"]["official-artwork"]["front_default"]

#acá la evolución
url2= f"https://pokeapi.co/api/v2/pokemon-species/{nombre}"
datos_ps = get_info(url2)

if datos_ps["evolves_from_species"] is None:
    evolves_from = ""
    poke_etapa = ""
else:
    evolves_from = datos_ps["evolves_from_species"]["name"]
    poke_etapa = f"Etapa previa: {evolves_from.capitalize()}"

print(poke_etapa)

#hacer un modulo que diga get stats
stats = []
for item in datos_base["stats"]:
    stats.append(item["base_stat"])

print(stats)

poke_hp, poke_at, poke_de, poke_ate, poke_def, poke_ve = stats

print(poke_ve) #deberia ser 90 para pikachu 

#Acá continuo con la parte de TIPO

tipos_lista = datos_base["types"]

tipos = []
for item in tipos_lista:
    tipos.append(item["type"]["name"])

print(tipos)

#parte de la descripcion

descripcion = datos_ps["flavor_text_entries"]

descripcion_es = []

for item in descripcion: 
    if item["language"]["name"] == "es":
        descripcion_es.append(item["flavor_text"].replace("\n"," "))

##print(descripcion_es)

poke_desc = random.choice(descripcion_es)

##print(poke_descripcion)
   
poke_tipos = genera_span(tipos)

print(poke_tipos)

#ACÁ COMIENZA LA PARTE DE LOS ATAQUES
#SUPER EFECTIVO CONTRA
tipos_sec = procesa_tipos(tipos, "double_damage_to")
print(tipos_sec)

poke_sec = genera_span(tipos_sec)

#DEBIL CONTRA
tipos_dc = procesa_tipos(tipos, "double_damage_from")
print(tipos_dc)

poke_dc = genera_span(tipos_dc)

#RESISTENTE CONTRA
tipos_rc = procesa_tipos(tipos, "half_damage_from")
print(tipos_rc)

poke_rc = genera_span(tipos_rc)

#POCO EFICAZ CONTRA
tipos_pec = procesa_tipos(tipos, "half_damage_to")
print(tipos_pec)

poke_pec = genera_span(tipos_pec)

#INMUNE CONTRA
tipos_imc = procesa_tipos(tipos, "no_damage_from")
print(tipos_imc)

poke_imc = genera_span(tipos_imc)

#INEFICAZ CONTRA
tipos_inc = procesa_tipos(tipos, "no_damage_to")
print(tipos_inc)

poke_inc = genera_span(tipos_inc)


#ahora document template
with open('base.html', 'r') as infile:
    entrada = infile.read()

document_template = Template(entrada)

document_template_nuevo = document_template.substitute(
    poke_id=poke_id, poke_nombre=poke_nombre, poke_img=poke_img, 
    poke_etapa=poke_etapa, poke_hp=poke_hp, poke_at=poke_at, poke_de=poke_de,
    poke_ate=poke_ate, poke_def=poke_def, poke_ve=poke_ve, poke_tipos=poke_tipos,
    poke_desc=poke_desc,poke_sec=poke_sec, poke_dc=poke_dc, poke_rc=poke_rc, poke_pec=poke_pec,
    poke_imc=poke_imc, poke_inc=poke_inc)


#crear un modulo para archivo de salida
with open('salida.html', 'w') as outfile:
    outfile.write(document_template_nuevo)

