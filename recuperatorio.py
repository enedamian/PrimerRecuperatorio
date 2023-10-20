# Recuperatorio Primer Parcial - Programación 2 - TUP UTN

nombre=''
fechaNacimiento=''
dni=''
legajo=''

# 1) implementar una funcion hashRecuperatorio(stringNombre, stringFecha) que recibe un nombre y una fecha de nacimiento 
# y devuelve un numero entero que representa el hash de la persona. stringFecha debe tener el formato "dd-mm-aaaa". 
# El hash se calculará de la siguiente forma:
# Se deben sumar los valores ASCII de los caracteres del nombre. (los valores ASCII se obtienen con la funcion "ord(caracter)" de python).
# Luego, si la suma anterior es par se le debe sumar el DNI, sino se le suma el Legajo. 
# Finalmente la función debe retornar el residuo de la división por 3 del resultado anterior. (módulo de la división por 3)
# Recordá validar los datos para que el programa no termine con errores.
# Sólo es necesario programar la función, no el ingreso de los datos.

def hashRecuperatorio(stringNombre, stringFecha):

    return 0


# 2) De acuerdo al hash obtenido en el punto 1 con su nombre y fecha de nacimiento, explique con sus palabras como funciona el algoritmo de ordenamiento que corresponda:
# 0: Ordenamiento por selección
# 1: Ordenamiento por inserción
# 2: Ordenamiento burbuja



# 3) Dada la siguiente lista, crear una función que devuelva una lista nueva con los nombres cuya longitud sea mayor a un numero pasado por parámetro,
# la lista a devolver deberá ordenada alfabéticamente sin distingir entre mayuscula y minusculas.
lista_nombres = ["Juan", "Pedro", "Maria", "Ana", "Florencia", "Hector", "jose", "Jorge", "Harry", "Haydee", "gisela","valeria", "valentina", 
         "Vanesa", "violeta", "Viviana", "ximena", "yanina", "Zoe", "Zulema", "Abril", "Agustin", "ivan", "federico"]

def filtrarLista(lista, longitud):
    
    return []


#4) Se organizo una venta de pizzas en el club para recaudar fondos. Cada pizza se vendio a $1500 y el club consiguió 100 pizzas para vender.
# En la página del club se anotaron los interesados en comprar pizzas, y se cargó en un archivo CSV la siguiente informacion:
# Nombre Comprador, Cantidad de paquetes
# Procese la información y confirme las ventas hasta donde alcance, si un comprador pidió más de lo que queda se le vende hasta donde alcance. 
# Ejemplo: suponiendo que h4ay 10 paquetes. 
# 1° en el archivo compro 5. 
# 2° compro 3. 
# 3° quiso comprar 15 pero solo quedaban 2.
# 4° no pudo comprar porque no habia mas.
# Imprimir por pantalla la información de las ventas realizadas indicando nombre comprador y cantidad de paquetes y quienes se quedaron sin poder comprar.
# ruta archivo para usar F5: PrimerParcial\compradores.csv

def procesarVentas(compradores, cantidadPaquetesDisponibles):
    
    return 0

#5) Implementar una función que reciba un diccionario con las claves como nombres de personas y los valores como edades 
# y devuelva un diccionario con las claves como edades y los valores una LISTA con los nombres de las personas de esa edad.
dicEdades = {"Juan":30,"María":25,"Carlos":35,"Ana":28,"Luis":32,"Laura":29,"Pedro":31,"Sofía":26,"Miguel":27,"Isabel":24,
             "Diego":33,"Valentina":22,"Javier":29,"Carmen":40,"Andrés":38,"Lucía":27,"Ricardo":36,"Victoria":23,"Gabriel":34,
             "Fernanda":31,"Max":29,"Diana":28,"Rodrigo":30,"Camila":25,"Gonzalo":33,"Daniela":27,"Emilio":29,"Marcela":34,
             "José":39,"Valeria":26,"Andrea":30,"Raúl":42,"Sara":24,"Rafael":36,"Elena":25,"Martín":32,"Beatriz":28,"Pablo":37,
             "Lorena":30,"Ángel":29,"Paula":26,"Luisa":35,"Arturo":31,"Mónica":27,"Manuel":28,"Verónica":29,"Carlos":40}
# Resultado esperado
#personas_por_edad = {
#    22: ["Valentina"],
#    23: ["Victoria"],
#    24: ["Isabel", "Sara"],
#    25: ["María", "Laura", "Elena", "Camila"],

def invertirDiccionario(diccionario):

    return 0