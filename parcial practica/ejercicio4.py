# EJERCICIO 4) Se tiene la siguiente lista de Países:
# Escribir un programa Python que:

paises = ["Afghanistan","Albania","Algeria",
"Andorra","Angola","Anguilla",
"Antigua and Barbuda","Armenia",
"Aruba","Australia","Austria",
"Azerbaijan","Bahamas","Bahrain",
"Bangladesh","Barbados","Belarus",
"Belgium","Belize","Benin","Bermuda",
"Bhutan","Bolivia","Bosnia & Herzegovina",
"Botswana","Brazil","British Virgin Islands",
"Brunei","Bulgaria","Burkina Faso","Burundi",
"Cambodia","Cameroon","Cape Verde",
"Cayman Islands","Chad","Chile","China",
"Colombia","Congo","Cook Islands",
"Costa Rica","Cote D Ivoire","Croatia",
"Cruise Ship","Cuba","Cyprus","Czech Republic",
"Denmark","Djibouti","Dominica",
"Dominican Republic","Ecuador","Egypt",
"El Salvador","Equatorial Guinea", "Estonia","Ethiopia","Falkland Islands",
"Faroe Islands","Fiji","Finland","France",
"French Polynesia","French West Indies","Gabon",
"Gambia","Georgia","Germany","Ghana","Gibraltar",
"Greece","Greenland","Grenada","Guam","Guatemala",
"Guernsey","Guinea","Guinea Bissau","Guyana",
"Haiti","Honduras","Hong Kong","Hungary","Iceland",
"India","Indonesia","Iran","Iraq","Ireland",
"Isle of Man","Israel","Italy","Jamaica","Japan",
"Jersey","Jordan","Kazakhstan","Kenya","Kuwait",
"Kyrgyz Republic","Laos","Latvia","Lebanon",
"Lesotho","Liberia","Libya","Liechtenstein",
"Lithuania","Luxembourg","Macau","Macedonia",
"Madagascar","Malawi","Malaysia","Maldives",
"Mali","Malta","Mauritania","Mauritius","Mexico",
"Moldova","Monaco","Mongolia","Montenegro",
"Montserrat","Morocco","Mozambique","Namibia",
"Nepal","Netherlands","Netherlands Antilles",
"New Caledonia","New Zealand","Nicaragua","Niger",
"Nigeria","Norway","Oman","Pakistan","Palestine",
"Panama","Papua New Guinea","Paraguay","Peru",
"Philippines","Poland","Portugal","Puerto Rico",
"Qatar","Reunion","Romania","Russia","Rwanda",
"Saint Pierre & Miquelon","Samoa","San Marino",
"Satellite","Saudi Arabia","Senegal","Serbia",
"Seychelles","Sierra Leone","Singapore","Slovakia",
"Slovenia","South Africa","South Korea","Spain",
"Sri Lanka","St Kitts & Nevis","St Lucia",
"St Vincent","St. Lucia","Sudan","Suriname","Swaziland",
"Sweden","Switzerland","Syria","Taiwan","Tajikistan",
"Tanzania","Thailand","Timor L'Este","Togo","Tonga", "Trinidad & Tobago","Tunisia","Turkey","Turkmenistan",
"Turks & Caicos","Uganda","Ukraine",
"United Arab Emirates","United Kingdom","Uruguay",
"Uzbekistan","Venezuela","Vietnam",
"Virgin Islands (US)","Yemen","Zambia","Zimbabwe"]

# a. Permita al usuario ingresar un nuevo País para ser incorporado a la lista (‘Argentina’).
# Luego mostrar la lista completa y la cantidad de países incluidos.

nuevo_pais = paises.append(input('ingrese un nuevo pais: '))
paises = sorted(paises)
print(paises)
cantidad = len(paises)
print(f'La cantidad de paises es {cantidad}')
print('-------')

# b. Crear una función Buscar_pais() que reciba como parámetros la lista y un String,
# deberá retornar un valor entero con la posición que se encuentra en la lista.

pais_buscado = input('Ingrese un pais a buscar: ') 

def buscar_pais(lista,string):
    string1 = string[0].upper()
    string2 = string[1:].lower()
    buscada = string1 + string2
    buscado = lista.index(buscada)
    print(f'El pais buscado ocupa la posicion {buscado}')
    
buscar_pais(paises,pais_buscado)
print('-------')

# c. Listar todos los países de la lista que empiecen con la letra ‘M’.

paises_M =[]

def listar_M(): 
    for i in paises:
        if (i[0] == "M"):
            paises_M.append(i)
    print(f'Estos son todos los paises que empiezan con M: {paises_M}')
listar_M()