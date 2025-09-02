#llamar librerias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv("Ejercicio/usuarios_app_limpieza.csv")


# Convertir a número edad y tiempo sesion, si no son válidos se ponen NaN
df['edad'] = pd.to_numeric(df['edad'], errors='coerce')
df['tiempo sesión'] = pd.to_numeric(df['tiempo sesión'], errors='coerce')

# Eliminar filas con NaN en edad o tiempo_sesion
df_clean = df.dropna(subset=['edad', 'tiempo sesión'])

# filtrar solo usuarios activos si hay una columna "activo"
if 'activo' in df_clean.columns:
    df_clean = df_clean[df_clean['activo'] == 1]


sns.set_style("whitegrid")  # Fondo bonito cuadricula
plt.figure(figsize=(10, 6))  # Tamaño del gráfico

# Crear scatterplot
ax = sns.scatterplot(
    data=df_clean,
    x='edad',              # Eje X
    y='tiempo sesión',     # Eje Y
    hue='país',            # Colorear puntos por país
    palette='pastel',      # Colores suaves
    edgecolor="black",     # Borde negro en los puntos
    s=80                   # Tamaño de los puntos
)

# Personalizar título y ejes
plt.title('Relación entre Edad y Tiempo de Sesión', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Edad', fontsize=12, fontweight='bold')
plt.ylabel('Tiempo de Sesión', fontsize=12, fontweight='bold')

# Ajustar límites 
plt.xlim(17.5, 37.5)  
plt.ylim(0, 50)

# Mostrar
plt.tight_layout()
plt.show()
