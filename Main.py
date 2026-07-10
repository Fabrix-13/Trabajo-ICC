import math
from sklearn import datasets
import cv2

"""
Primero al insertar una imagen la computadora debe raconocerla:
    - Hacer que se tranforme en escalas grises
    - Transformar a 8x8
    - Invertir colores
    - Normalizar 0 - 16 (cero es blanco y mientras va aumentando se vuelve un tono más negro)
Hacemos esto debido a que las imagenes en la lista digits se encuentra de escala 16.
"""
matriz_ = cv2.imread("miNumero9_3.png", cv2.IMREAD_GRAYSCALE)
matriz_ =cv2.resize(matriz_, dsize=(8,8))

# Invertir los colores
i = 0
while i < 8:
    j = 0
    while j < 8:
        matriz_[i][j] = 255 - matriz_[i][j]
        j += 1
    i += 1

# Corrigiendo los colores
i = 0
while i < 8:
    j = 0
    while j < 8:
        matriz_[i][j] = matriz_[i][j]/255*16
        j += 1
    i += 1
print(matriz_)
"""
Segundo paso sacar la distancia euclidiana con el dataset digits.
"""

matriz = datasets.load_digits()
matriz_imagines = matriz["images"]

dic = {} # En este diccionario se van a complar todas las imagenes con su target, distancia Euclidiana e indicie. (Aunque este ultimo m¿no estan necesario)

for k in range(len(matriz_imagines)):
    i = 0
    suma = 0
    while i < 8:
        j = 0
        while j < 8:
            resta = matriz_imagines[k][i][j] - matriz_[i][j]
            potencia = resta ** 2
            suma += potencia
            j = j+1
        i = i + 1
    raiz = math.sqrt(suma)
    dic[k] = {}
    dic[k]["Eu"] =  raiz
    dic[k]["target"] = matriz["target"][k]
    dic[k]["indice"] = k

"""
Tercer paso Comparar todas las distancias y ordenar el diccionario, lo hare con bubble_sort, esto debido a que la función sort() no ordena diccionarios.
merge sort tambien seria util para esta situación, pero el volumen de los datos es pequeño por lo que más conveniente es el bubble sort.
"""

def bubble_sort(lista):
    for tope in range(len(lista) - 1, 0, -1):
        for i in range(tope):
            if lista[i]["Eu"] > lista[i + 1]["Eu"]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp


bubble_sort(dic) # Usamos bubble sort.

"""
Ultimo paso comparamos los tres ultimos targets
1. si los tres son iguales, escoger el primero de ellos (en si cualquiera de ellos es igual).
2. si dos de ellos son iguales, escoger uno de esos, existen 3 posibles casos, o los primeros son iguales, los ultimos son iguales o el primero y el ultimo son iguales.
3. si ninguno es igual, escoger al primero de todos, lo hemos elegido así porque al ser el más cercano entonces tendria más relacion con el número a identificar.
"""
if dic[0]["target"] == dic[1]["target"] and dic[1]["target"] == dic[2]["target"]:
    numero = dic[0]["target"]

elif dic[1]["target"] == dic[2]["target"]:
    numero = dic[1]["target"]

elif dic[0]["target"] == dic[1]["target"]:
    numero = dic[1]["target"]

elif dic[2]["target"] == dic[0]["target"]:
    numero = dic[2]["target"]

else:
    numero = dic[0]["target"]

# Imprimir resultados
print("posibles valores: " + str(dic[0]["target"]) + ", " + str(dic[1]["target"]) + ", "+ str(dic[2]["target"]))
print("Soy la inteligencia artificial, y he detectado que el dígito ingresado corresponde al número "+ str(numero))



