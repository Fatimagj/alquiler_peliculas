import csv, os
ruta_alquiler = "datos/alquileres.csv"
ruta_catalogo = "datos/catalogo.csv"


class Dao:
    def __init__(self, ruta_alquiler, ruta_catalogo):
        self.alquiler = ruta_alquiler
        self.catalogo = ruta_catalogo
        self.leer_alquiler()
        self.agrupar_por_titulos()
        self.crear_catalogo()


    def leer_alquiler(self):
        with open(self.alquiler, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f, delimiter=";", quotechar='"')#para leer linea por linea, cada linea se convierte en un diccionario donde las claves sos los nomnbres de las columnas.
            return list(reader) #para convertir lo que estamos leyendo en una lista de diccionarios, cada diccionario es una fila

    def agrupar_por_titulos(self):
        catalogo_titulos = {} #se crea un diccionario vacio
        for r in self.leer_alquiler(): #iteramos sobre cada filar del archivo alquileres qu elo leemos llamando a la función anterior. la variable r representa cada fila del archivo.
            titulo = r["titulo"] #srepresenta el titulo de la película
            if titulo in catalogo_titulos: #si el titulo ya está en el diccionario
                catalogo_titulos[titulo]["copia"] += 1 #se incrementa el numero de copias en uno
            else:
                sinopsis = r["sinopsis"]
                director = r["Director"]
                año = r["año"]
                catalogo_titulos[titulo] = {"titulo": titulo, "sinopsis": sinopsis, "Director": director, "año": año, "copia": 1} #agregamoss una nueva entrada al diccionario
        return catalogo_titulos
    
    def crear_catalogo(self):
            
            #if not os.path.exists(self.catalogo): #, os es una función de la biblioteca que verifica si un archivo existe o no
            with open(self.catalogo, "w", newline="") as f: #si no existe, abre un documento en modo escritura.
                cabecera = ["titulo", "sinopsis", "Director", "año", "copia"]
                writer = csv.DictWriter(f, fieldnames=cabecera, delimiter=";", quotechar='"')#para escribir datos en el archivo csv en forma de diccionario
                writer.writeheader() #escribe las filas de datos en el archivo nuevoo, es una lista de diccionarios.
                catalogo = self.agrupar_por_titulos()
                for titulo, info_pelicula in catalogo.items(): #se tiene que añadir a este elemento de python () para que pueda ser iterable
                    writer.writerow(info_pelicula)




dao = Dao(ruta_alquiler, ruta_catalogo)
#print(dao)


