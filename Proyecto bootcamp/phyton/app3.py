import matplotlib.pyplot as plt


labels = [
    "Renovables (Total)",
    "Eólica",
    "Solar",
    "Hidroeléctrica"
]
participacion = [
    60,
    20,
    15,
    25
]

plt.figure(figsize=(6,6))
plt.pie(participacion, labels=labels, autopct='%1.1f%%', startangle=140, colors=['mediumseagreen', 'skyblue', 'gold', 'deepskyblue'])
plt.title("Participación de Energías Renovables en el Consumo Eléctrico")
plt.axis('equal')
plt.tight_layout()
plt.show()