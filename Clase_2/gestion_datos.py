import pandas as pd # analisis de datos
import numpy as np # calculos numericos
import re # expresiones regulares
# \D detecta numeros \d+ detecta un par de numeros (\d+) detecta 

# 1. cargar datos
df = pd.read_csv("Clase_2/Usuarios_app_clase2.csv", encoding="utf-8")

# 2. normalizar nombres de columnas
df.columns = (df.columns.str.strip()
              .str.lower()
              .str.replace(" ","_",regex=False))

# 3. unificar paises 
map_pais = {"mexico":"México",
            "méxico":"México",
            "Mexico":"México"}

df['pais']=df['pais'].astype(str).str.strip().replace(map_pais)

def to_number(x):
    if pd.isna(x) or str(x).strip() == "":

        return np.nan
    
    h = str(x).strip().lower()
    palabras ={"quince":15}
    if h in palabras:
        return float(palabras[h])#si la palabra esta en diccionario reemplaza por numero
    s = re.search(r"(\d+)", h) # buscamos solo numeros de todo el texto: \d busca un digito
    
    return float(s.group(1)if s else np.nan)
    
# 4. aplicar conversiones
df ["edad"] = df["edad"].apply(to_number)
df ["tiempo_sesion_min"] = df["tiempo_sesion_min"].apply(to_number)
df ["clicks"] = df["clicks"].apply(to_number)
df ["compras"] = df["compras"].apply(to_number)

# 5. eliminar duplicados (ignorando usuarios_id)
df = df.drop_duplicates(subset=["nombre","edad","pais","tiempo_sesion_min","estado","suscripcion","clicks","compras"])

# 6. quitar filas sin edad o tiempo valido
df= df.dropna(subset=["edad","tiempo_sesion_min"])

# 7. rangos razonables
df= df[df["edad"].between(10,100)]
df = df[df["tiempo_sesion_min"].between(10,100)]

# 8. guardar datos
df.to_csv("usuarios_app_limpio.csv",index=False,encoding="utf-8") 
print("Limpieza finalizada. Filas:", df.shape[0]) # mostramos cantidad de filas