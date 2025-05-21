import pandas as pd
import matplotlib.pyplot as plt


datos = {
    "Año": [2018, 2019, 2020, 2021, 2022],
    "Solar": [400, 480, 600, 720, 850],
    "Eólica": [1000, 1100, 1250, 1400, 1600]
}

df = pd.DataFrame(datos)


plt.figure(figsize=(8, 5))
plt.plot(df["Año"], df["Solar"], label="Solar", marker='o')
plt.plot(df["Año"], df["Eólica"], label="Eólica", marker='s')
plt.title("Producción de Energía Renovable (TWh)")
plt.xlabel("Año")
plt.ylabel("Producción (TWh)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("grafica_energia.png")
plt.close()
