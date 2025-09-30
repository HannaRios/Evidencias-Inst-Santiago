import pandas as pd

df= pd.read_csv("clase_3/usuarios.csv")
print("Total de usuarios:", len(df))

#Crear segmentacion
def categoria_clicks(c):
    if c >= 200:
        return "Muy activo"
    elif c >= 100:
        return "Activo"
    elif c >= 50:
        return "Medio" 
    else:
        return "Bajo"

df["segmento_clicks"] = df["clicks"].apply(categoria_clicks)

def categoria_compras(c):
    if c >= 3:
        return "Comprador Frecuente"
    elif c >= 1:
        return "Comprador Ocasional"
    else:
        return "No comprador"

df["segmento_compras"] = df["compras"].apply(categoria_compras)

resumen = df.groupby(["suscripcion", "segmento_clicks","segmento_compras"]).size().reset_index(name="usuarios")

print(resumen)

df.to_csv("usuarios_segmentados_clase3.csv", index=False, encoding="utf-8")