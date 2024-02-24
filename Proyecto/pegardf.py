import pandas as pd


# Cargar el DataFrame desde el archivo pickle
df1 = pd.read_pickle('./df_resumen_100.pkl')
df2 = pd.read_pickle('./df_resumen_200.pkl')
df3 = pd.read_pickle('./df_resumen_300.pkl')
df4 = pd.read_pickle('./df_resumen_fin.pkl')


df_1 = df1.head(100)
df_2 = df2.iloc[100:200, :].copy()
df_3 = df3.iloc[200:300, :].copy()
df_4 = df4.iloc[300:424, :].copy()

df_concatenado = pd.concat([df_1, df_2, df_3, df_4], axis=0)


print(len(df_concatenado))

print(df_concatenado.iloc[423,3])

df_concatenado.to_pickle('df_resumenes.pkl')
