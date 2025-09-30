import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r"C:\Sena\Santiago\Clase_3\usuarios_segmentados_clase3.csv")
plt.figure(figsize=(12,5))
plt.subplot(2,2,1)
sns.countplot(data=df, x="segmento_clicks",hue="suscripcion",palette="pastel")
plt.title("Usuarios por segmento de clicks")
plt.subplot(2,2,2)
df['suscripcion'].value_counts().plot(kind ='bar')
plt.title("..")
plt.subplot(2,2,3)
sns.boxplot(data=df, x="suscripcion", y="compras", palette="muted")
plt.title("Distribución de compras segun suscripción")
plt.subplot(2,2,4)
sns.heatmap(df.select_dtypes(include=["number"]).corr(), annot=True, cmap="coolwarm",)
plt.title("Mapa de calor")
plt.tight_layout()
plt.show()