import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. cargar la base de datos
df = pd.read_csv("usuarios_app_limpio.csv", encoding = "utf-8")

# 2. KPI rapidos: total de usuarios
total_usuarios = len(df)
print("Total de usuarios limpios", total_usuarios)

# 3. promedio, mediana y cantidad de sesiones por pais y estado
stats = (
    df.groupby(["pais","estado",])["tiempo_sesion_min"] #agrupamos los datos por pais y estado
    .agg(["mean","median","count"]) #calculamos promedio media y cantidad
    .rename(columns={"mean":"promedio", "median":"mediana","count":"cantidad"})
    .reset_index()
)
print("\n Estadisticas  por pais y estado:")
print(stats)

# 4. correlacion entre edad y numero de clicks
# la  correlacion mide que tan relacionadas estan dos valores numericos
correlacion = df["edad"].corr(df["clicks"])
print("\nCorrelacion entre edad y clicks",correlacion)
#A medida que la edad aumenta los clicks disminuyen

# 5. visualizacion  1: usuarios por pais grafico de barras
plt.figure(figsize=(10,5))
usuarios_por_pais = df.groupby("pais")["usuario_id"].count().reset_index()
sns.barplot(data=usuarios_por_pais,x="pais", y="usuario_id", hue="pais", palette="viridis")

plt.title('Usuarios por Pais')
plt.xlabel('pais')
plt.ylabel('Cantidad de usuarios')
plt.show()

# 6. visualizacion 3: mapa de calor de correlaciones
plt.figure(figsize=(8,4))
sns.heatmap(df.select_dtypes(include=["number"]).corr(), annot=True, cmap="coolwarm",)
plt.title("Mapa de calor de correlaciones")
plt.tight_layout()
plt.show()