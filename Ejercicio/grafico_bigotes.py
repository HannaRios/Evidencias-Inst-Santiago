import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Ejercicio/usuarios_app_limpieza.csv")

# Limpiar los datos - eliminar filas donde la edad está vacía
df_clean = df.dropna(subset=['edad'])

# Configurar el estilo de seaborn para que se vea similar a la imagen
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

# Crear el boxplot con colores pastel específicos para cada país
colors = ['#4A90E2', '#8B7355', '#7CB342', '#D32F2F']  # Azul, marrón, verde, rojo
country_order = ['Colombia', 'México', 'Chile', 'Perú']

# Crear el boxplot
ax = sns.boxplot(data=df_clean, 
                x='país', 
                y='edad',
                order=country_order,
                palette=colors,
                linewidth=1.5)

# Personalizar el gráfico para que se vea exactamente como la imagen
plt.title('Distribución de Edad por País', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('País', fontsize=12, fontweight='bold')
plt.ylabel('Edad', fontsize=12, fontweight='bold')

# Configurar los límites del eje Y para que coincidan con la imagen
plt.ylim(17.5, 37.5)

# Configurar los ticks del eje Y
plt.yticks([20, 22.5, 25, 27.5, 30, 32.5, 35])

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()

# Opcional: Guardar el gráfico
# plt.savefig('distribucion_edad_por_pais.png', dpi=300, bbox_inches='tight')

# Verificar los datos limpios
print("Datos originales:", len(df))
print("Datos después de limpiar:", len(df_clean))
print("\nRegistros por país después de limpieza:")
print(df_clean['país'].value_counts())

print("\nEstadísticas descriptivas por país:")
print(df_clean.groupby('país')['edad'].describe())