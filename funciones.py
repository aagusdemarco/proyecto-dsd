import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Funciones para encontrar palabras y numeros repetidos

def contar_valor(lista, numero):
    contador = 0
    for dup in lista:
        if dup == numero:
            contador += 1
    return contador

def contar_cadena(lista, cadena):
    contador = 0
    for dup in lista:
        if dup == cadena:
            contador += 1
    return contador


# Funcion para calcular la edad de una persona

def calcular_edad(fecha_nacimiento):
    fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, '%d-%m-%Y')
    edad = datetime.datetime.now().year - fecha_nacimiento.year
    return edad


# Funciones para manejar Data Frames

def promedio_df(data_frame, columna):
    data_frame = pd.DataFrame(data_frame)
    if columna in data_frame.columns:
        promedio = data_frame[columna].mean()
    else: 
        promedio = 0
        print(f'La columna {columna} no fue encontrada')
    return promedio

def contar_df(data_frame):
    data_frame = pd.DataFrame(data_frame)
    repeticiones = {}
    for columna in data_frame:
        for valor in data_frame[columna]:
            if valor in repeticiones:
                repeticiones[valor] += 1
            else: repeticiones[valor] = 1
    return repeticiones

def cadenas_minus_df(data_frame):
    data_frame = pd.DataFrame(data_frame)
    df_minus = data_frame.copy()
    for columna in data_frame.columns:
        if data_frame[columna].dtype == 'object':
            df_minus[columna] = data_frame[columna].apply(str).str.lower()
    return df_minus


# Funciones para manipular y generar gráficos

def grafico_barras(dataframe, nombre, titulo, ejex, ejey):
    dataframe = pd.DataFrame(dataframe)
    plt.figure()
    graph = dataframe.plot.bar(stacked = False)
    graph.set_title(titulo)
    graph.set_xlabel(ejex)
    graph.set_ylabel(ejey)
    plt.savefig(f'{nombre}.jpg')

def grafico_lineas(dataframe, nombre, titulo, ejex, ejey):
    dataframe = pd.DataFrame(dataframe)
    plt.figure()
    graph = dataframe.plot.line()
    graph.set_title(titulo)
    graph.set_xlabel(ejex)
    graph.set_ylabel(ejey)
    plt.savefig(f'{nombre}.jpg')

def grafico_puntos(dataframe, nombre, titulo, ejex, ejey):
    plt.figure()
    graph = dataframe.plot.scatter(x=ejex, y=ejey)
    graph.set_title(titulo)
    graph.set_xlabel(ejex)
    graph.set_ylabel(ejey)
    plt.savefig(f'{nombre}.jpg')