import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Ejercicio/usuarios_app.csv")

df['pais'].value_counts().plot(kind ='bar')

plt.title('Usuarios por Pais')
plt.xlabel('pais')
plt.ylabel('Cantidad de usuarios')
plt.show()