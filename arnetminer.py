from sklearn.feature_extraction.text import CountVectorizer
import numpy
import xmltodict


#visit https://www.journaldev.com/19392/python-xml-to-json-dict - to see how to manipulate the dictionary
#Nota: algunas variables estan inicializadas en 1234 pero esto es incorrecto. Hallar el valor correcto y corregir.
#Nota2: ver algoritmo x-means

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
#print array_for_clustering

def title_bag_of_words(an_array):
	title_array = []
	for i in an_array:
		title_array.append(i['title'])
	vectorizer = CountVectorizer()
	return vectorizer.fit_transform(title_array).todense()


def venue_to_value(an_array):
	venue_array = []
	venue_dictionary = {}
	for i in an_array:
		venue_array.append(i['jconf'])
	unique_venue_array = list(set(venue_array))
	for index, item in enumerate(unique_venue_array):
	 	venue_dictionary[index] = item
	return venue_dictionary



def author_existence(an_array):
	author_array = []
	author_matrix = numpy.matrix
	for i in an_array:
		author_array.append(i['authors'])
	for index,item in enumerate(author_array):
		author_matrix[index] = item.split(",")
	#splitted = author_array.split(",")
	#unique_author_array = list(set(author_array))
	return author_matrix

def join_features_in_matrix(an_array):
	initial_matrix = title_bag_of_words(an_array)
	#usar un array de array
	#append journal or conference values
	for index, item in enumerate(an_array):
		f
	return initial_matrix


print title_bag_of_words(array_for_clustering)
print venue_to_value(array_for_clustering)
print join_features_in_matrix(array_for_clustering)
#print author_existence(array_for_clustering)

#una vez conseguido el array de publicaciones, es necesaria una funcion que transforme los elementos de cada publicacion en un valor numerico, generandose asi 
#la matriz sobre la cual aplicaremos clustering



# corpus = [
# 'All my cats in a row',
# 'When my cat sits down, she looks like a Furby toy!',
# 'The cat from outer space',
# 'Sunshine loves to sit like this for some reason.'
# ]

# vectorizer = CountVectorizer()
# print( vectorizer.fit_transform(corpus).todense() )
# print( vectorizer.vocabulary_ )


#funcion para estimar el k, es decir el numero posible de autores dado un conjunto de publicaciones a nombre de alquien
# def estimacion_de_k(array_publicaciones):
# 	#inicializando valores
# 	i = 0
# 	k = 1
# 	un_cluster = array_publicaciones #dado que al inicio k=1, el cluster se inicializa con la cantidad total de publicaciones
# 	while(existe_posibilidad_split):
# 		for cluster in conjunto_de_clusters: #ver en que estructura colocamos esto
# 			hallar submodelos
# 			if(calculo_bic(m2)>calculo_bic(m1))
# 				dividir_cluster(cluster) #crear funcion dividir_cluster
# 			nuevo_modelo = 1234
# 			calculo_bic(nuevo_modelo)
# 	#elegir modelo con BIC mas alto como output?

#funcion que determina si es posible particionar un cluster, si el cluster esta compuesto por un solo dato, no es posible hacer mas particiones. Si tiene mas de un dato, se puede particionar
def existe_posibilidad_split(un_cluster):
	if len(cluster) == 1:
		return False
	else:
		return True

# #funcion que calcula el criterio de informacion bayesiano y retorna el resultado
# def calculo_bic(modelo):
# 	un_lambda = 1234
# 	numero = 1234
# 	return math.log(probabilidad_modelo(modelo)) - ((un_lambda/2) * math.log(numero))
