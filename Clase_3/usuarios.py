import random  
import pandas as pd

nombres=["Ana", "Juan", "Sofía", "Carlos", "María", "Luis", "Camila", "Andrés", 
        "Valentina", "Pedro", "Lucía", "Mateo", "Isabella", "Daniel", "Gabriela", "Julián", 
        "Paula", "Sebastián", "Laura", "Tomás","Manuela", "Felipe", "Natalia", "Diego",
          "Carolina", "Santiago", "Mónica", "Esteban", "Andrea"
]

paises=["Colombia","Mexico","Chile","Peru","Argentina","Ecuador"]
suscripciones=["free","premium"]
estados=["activo","inactivo"]
data=[]

for i in range(1,201):
    nombre = random.choice(nombres)
    edad = random.randint(18,60)
    pais = random.choice(paises)
    tiempo = random.randint(5,200)
    estado = random.choice(estados)
    suscripcion = random.choice(suscripciones)
    clicks = random.randint(10,300)
    compras = random.randint(0,5)

    data.append([i,nombre,edad,pais,tiempo,estado,suscripcion,clicks,compras])

df = pd.DataFrame(data, columns=["usuario_id", "nombre", "edad", "pais", "tiempo_sesion_min", "estado", "suscripcion", "clicks", "compras"])
df.to_excel("usuarios.xlsx", index=False)
df.to_csv("usuarios.csv", index=False,encoding="utf-8")