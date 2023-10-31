import pandas as pd
import matplotlib.pyplot as plt
import funciones as func

import pandas as pd

# Datos de ejemplo
data = {
    'Categoria': ['A', 'B', 'C', 'D'],
    'Valor1': [10, 15, 8, 12],
    'Valor2': [5, 10, 7, 9]
}
df = pd.DataFrame(data)

# Caso de prueba para grafico_barras
func.grafico_barras(df, 'grafico_barras', 'Gráfico de Barras', 'Categoria', 'Valor1')

# Caso de prueba para grafico_lineas
func.grafico_lineas(df, 'grafico_lineas', 'Gráfico de Líneas', 'Categoria', 'Valor2')

# Caso de prueba para grafico_puntos
func.grafico_puntos(df, 'grafico_puntos', 'Gráfico de Puntos', 'Valor1', 'Valor2')
