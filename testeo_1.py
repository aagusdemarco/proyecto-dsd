import funciones as func


# Casos de prueba para contar_valor:

lista1 = [1, 2, 3, 4, 2, 2, 5, 2, 6]
numero1 = 2

lista2 = []
numero2 = 7

lista3 = [3]
numero3 = 3

print(func.contar_valor(lista1, numero1))
print(func.contar_valor(lista2, numero2)) # Devuelve 0 cuando no encuentra un repetido
print(func.contar_valor(lista3, numero3)) # Devuelve 1 cuando solo hay un elemento del que se busca


# Casos de prueba para contar_cadena:

lista4 = ["manzana", "pera", "manzana", "uva", "manzana"]
cadena1 = "manzana"

lista5 = ["hola", "mundo", "python", "openai"]
cadena2 = "java"

lista6 = ["gato"]
cadena3 = "gato"

print(func.contar_cadena(lista4, cadena1))
print(func.contar_cadena(lista5, cadena2)) # Devuelve 0 cuando no encuentra el elemento
print(func.contar_cadena(lista6, cadena3)) # Devuelve 1 cuando solo hay un elemento del que se busca
