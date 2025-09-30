#librerias
import pandas as pd   
import seaborn as sns
import matplotlib.pyplot as plt  

df = pd.read_csv("Ejercicio/usuarios_app_limpieza.csv")  # Llamar el archivo CSV

df_clean = df.dropna(subset=['edad'])  # Quitar filas donde la edad esta vacía

country_order = ['Colombia', 'México', 'Chile', 'Perú']  # Ordenar países en el eje X

# Crear un boxplot (gráfico de bigotes)
ax = sns.boxplot(
    data=df_clean,     # Usar los datos limpios
    x='país',          # Poner los países en el eje X
    y='edad',          # Poner la edad en el eje Y
    order=country_order,              # Mantener el orden de los países
    palette=sns.color_palette("pastel"),  # Usar colores de Seaborn
    linewidth=1.5      # Grosor de las líneas de las cajas
)

# Título y nombres de los ejes
plt.title('Distribución de Edad por País', fontsize=16, fontweight='bold', pad=20)  
plt.xlabel('País', fontsize=12, fontweight='bold')  
plt.ylabel('Edad', fontsize=12, fontweight='bold')  

plt.ylim(17.5, 37.5)  # Limitar el rango del eje Y para que se vea mejor
plt.yticks([20, 22.5, 25, 27.5, 30, 32.5, 35])  # Marcar valores específicos en el eje Y


plt.show()  # Mostrar el gráfico 
