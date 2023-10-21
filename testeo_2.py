import funciones as func
import pandas as pd

# Promedio de Data Frames

data_promedio = {
    'Nombre': ['Ana', 'Juan', 'María', 'Carlos'],
    'Edad': [25, 30, 28, 22],
    'Puntaje': [85, 92, 78, 65]
}
df_promedio = pd.DataFrame(data_promedio)

print(func.promedio_df(df_promedio, 'Puntaje')) 

data_promedio_vacio = {
    'Nombre': [],
    'Edad': [],
    'Puntaje': []
}
df_promedio_vacio = pd.DataFrame(data_promedio_vacio)

print(func.promedio_df(df_promedio_vacio, 'Puntaje')) # Cuando es vacío devuelve NaN


# Repeticiones en Data Frames

data_contar = {
    'Nombre': ['Ana', 'Juan', 'Ana', 'María'],
    'Edad': [25, 30, 25, 28],
    'Puntaje': [85, 92, 85, 78]
}
df_contar = pd.DataFrame(data_contar)

print(func.contar_df(df_contar))

data_contar_distinto = {
    'Ciudad': ['Nueva York', 'Los Angeles', 'Chicago', 'Miami'],
    'País': ['EE. UU.', 'EE. UU.', 'EE. UU.', 'EE. UU.'],
    'Población': [8398748, 3990456, 2705994, 470914]
}
df_contar_distinto = pd.DataFrame(data_contar_distinto)

print(func.contar_df(df_contar_distinto))


# Data Frames en minusculas

data_cadenas_minus = {
    'Nombre': ['Ana', 'Juan', 'María', 'Carlos'],
    'Ciudad': ['New York', 'Los Angeles', 'Chicago', 'Miami']
}
df_cadenas_minus = pd.DataFrame(data_cadenas_minus)

print(func.cadenas_minus_df(df_cadenas_minus))

data_cadenas_minus_numeros = {
    'Nombre': [123, 'Juan', 'MARÍA', 456],
    'Ciudad': ['New York', 'Los Angeles', 789, 'Miami']
}
df_cadenas_minus_numeros = pd.DataFrame(data_cadenas_minus_numeros)

print(func.cadenas_minus_df(df_cadenas_minus_numeros)) # Es necesario añadir a la funcion el metodo apply(str) para que los number no sean transformados a NaN
