import funciones as func
import pandas as pd
import numpy as np

# Acceso al archivo de excel

path = 'AP\proyecto_dsd\colores.xlsx'
try:
    colores = pd.read_excel(path)
except FileNotFoundError:
    print(f'no se puede hallar el archivo {path}')
    exit()
print(colores)


# Gráfico analizando el porcentaje de elección de un color u otro

porcentaje_colores = (colores['rojo o azul'].value_counts())/len(colores['rojo o azul'])*100
func.grafico_barras(porcentaje_colores, 'Porcentaje de Colores', 'Porcentaje Rojo/Azul', 'Colores', 'Porcentaje de Eleccíon')

# Grafico mostrando la edad de cada participante

func.grafico_barras(colores[['nombre', 'edad']], 'grafico_edad', 'Edad de Participantes', 'Nombre', 'Edad')

# Gráfico de dispersión para mostrar la relación entre la edad y la elección

func.grafico_puntos(colores, 'grafico_edad_eleccion', 'Relación entre Edad y Elección', 'edad', 'rojo o azul')

# Gráficos analizando las edades de cada uno

promedio_edades = np.mean(colores['edad'])
colores['promedio_edad'] = promedio_edades

promedio_edades_df = pd.DataFrame({'Nombre': colores['nombre'], 'Edad': colores['edad'], 'Promedio': colores['promedio_edad']})
print(promedio_edades_df)

func.grafico_lineas(promedio_edades_df, 'Edades de Participantes', 'Edades de Participantes', 'Participante', 'Edad')


