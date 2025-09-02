import pandas as pd

# Leer archivo CSV
df = pd.read_csv("Ejercicio/usuarios_app_limpieza.csv")

# Eliminar duplicados basados en estas columnas
df = df.drop_duplicates(subset=['nombre', 'edad', 'país', 'tiempo sesión', 'estado'])

# Quitar registros sin edad
df = df.dropna(subset=['edad'])

# Convertir edad y tiempo sesión en números válidos
df['edad'] = pd.to_numeric(df['edad'], errors='coerce')
df['tiempo sesión'] = pd.to_numeric(df['tiempo sesión'], errors='coerce')

# Eliminar filas inválidas
df_clean = df.dropna(subset=['edad', 'tiempo sesión'])

# Calcular XP: 1 punto por minuto de sesión
df_clean['xp'] = df_clean['tiempo sesión']

# +10 si el estado es "activo"
df_clean['xp'] += df_clean['estado'].apply(lambda x: 10 if x.lower() == "activo" else 0)

# Nivel
def asignar_nivel(xp):
    if xp < 20:
        return "Novato"
    elif 20 <= xp <= 39:
        return "Intermedio"
    elif 40 <= xp <= 59:
        return "Avanzado"
    else:
        return "Experto"

df_clean['nivel'] = df_clean['xp'].apply(asignar_nivel)

# Mostrar resultado 
print(df_clean[['usuario id', 'nombre', 'edad', 'país', 'tiempo sesión', 'estado', 'xp', 'nivel']])
