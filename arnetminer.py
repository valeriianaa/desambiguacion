import xmltodict


#visit https://www.journaldev.com/19392/python-xml-to-json-dict - to see how to manipulate the dictionary

#funcion que abre el archivo xml, parsea a diccionario de python y retorna el array con las publicaciones del autor, que son los datos para el clustering
def preparar_archivo(ruta, nombre_archivo):
	with open(ruta + nombre_archivo) as archivo:
		diccionario = xmltodict.parse(archivo.read())
	unarray = diccionario['person']['publication']
	return unarray

#probando...
unaruta = '/media/ana/90BA2B70BA2B5250/Users/Ana/Documents/MEGA/Tesis 2017/datasets/aminer/simple/data/raw-data/'
unarchivo = 'Thomas D. Taylor.xml'

array_for_clustering = preparar_archivo(unaruta,unarchivo)

#funcion para estimar el k, es decir el número posible de autores dado un conjunto de publicaciones a nombre de alquien
def estimacion_de_k(array_publicaciones):
	#inicializando valores
	i = 0
	k = 1
	un_cluster = array_publicaciones #dado que al inicio k=1, el cluster se inicializa con la cantidad total de publicaciones
	while(existe_posibilidad_split):
		for cluster in conjunto_de_clusters: #ver en que estructura colocamos esto
			hallar submodelos
			if(calculo_bic(m2)>calculo_bic(m1))
				dividir_cluster(cluster) #crear funcion dividir_cluster
			calculo_bic(nuevo_modelo)
	#elegir modelo con BIC mas alto como output?

#funcion que calcula el criterio de información bayesiano y retorna el resultado
def calculo_bic(modelo):
	un_lambda = 1
	numero = 1
	return math.log(probabilidad_modelo) - ((un_lambda/2) * math.log(numero))

#función que luego formará parte del calculo_bic 
def probabilidad_modelo(modelo):
	nro_eventos = modelo
	nro_resultados = 1
	return nro_eventos / nro_resultados