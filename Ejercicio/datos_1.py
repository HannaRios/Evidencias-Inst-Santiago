import pandas as pd

#cargar los datos
df = pd.read_csv("Ejercicio/usuarios_app.csv")

#ver las primeras filas
print(df.head(2))

#informacion general
print(df.info())

#estadisticas basicas
print(df.describe())   