import matplotlib.pyplot as plt


fuentes = [
    "Eólica",
    "Solar",
    "Hidroeléctrica",
    "Biocombustible",
    "Geotérmica"
]
produccion = [
    120,
    95,
    180,
    60,
    30
]

plt.figure(figsize=(8,5))
plt.bar(fuentes, produccion, color=['skyblue', 'gold', 'deepskyblue', 'green', 'tomato'])
plt.title("Producción de Energía Renovable por Fuente")
plt.xlabel("Fuente")
plt.ylabel("Producción (GWh)")
plt.tight_layout()
plt.show()