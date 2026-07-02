import math
from sklearn import datasets
import cv2

"""
Primero al insertar una imagen la computadora debe raconocerla:
    - Hacer que se tranforme en escalas grises
    - Transformar a 8x8
    - Invertir colores
    - Normalizar 0 - 16
"""
matriz_ = cv2.imread("miNumero5_2.png", cv2.IMREAD_GRAYSCALE)
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

"""
Segundo paso sacar la distancia euclidiana con el dataset digits.
"""

matriz = datasets.load_digits()
matriz_imagines = matriz["images"]

dic = {}

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
Tercer paso Comparar todas las distancias y ordenar el diccionario, lo hare con bubble_sort.
"""

def bubble_sort(list):
    for tope in range(len(list) - 1, 0, -1):
        for i in range(tope):
            if list[i]["Eu"] > list[i + 1]["Eu"]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp


bubble_sort(dic)

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

print("posibles valores: " + str(dic[0]["target"]) + ", " + str(dic[1]["target"]) + ", "+ str(dic[2]["target"]))
print("Soy la inteligencia artificial, y he detectadoque el dígito ingresado corresponde al número "+ str(numero))



