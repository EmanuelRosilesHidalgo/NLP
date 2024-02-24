import pandas as pd

# Supongamos que tienes dos DataFrames llamados df1 y df2 con las mismas dimensiones
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['A', 'B', 'C'],
})

df2 = pd.DataFrame({
    'A': [4, 5, 6],
    'B': ['D', 'E', 'F'],
})

print(df2)
# Concatenar los dos DataFrames a lo largo del eje de las filas (axis=0) e ignorar índices originales
df_concatenado = pd.concat([df1, df2], axis=0, ignore_index=True)

# Imprimir el DataFrame resultante
print(df_concatenado)