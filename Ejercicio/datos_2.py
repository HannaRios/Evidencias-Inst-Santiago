import pandas as pd 

#cargar datos
df = pd.read_csv("Ejercicio/usuarios_app_limpieza.csv")

#ver las primeras filas
print(df.head(2))

#informacion general
print(df.info())

#estadisticas basicas
print(df.describe())   

#limpieza de datos
df = df.drop_duplicates(subset=['nombre','edad','país','tiempo sesión','estado'])

#rellenar datos nulos en "edad" con el promedio
df['edad'] = df['edad'].fillna(df['edad'].mean())

#filtrar usuarios activos
usuarios_activos = df[df['estado'] == 'activo']

print(usuarios_activos)