import matplotlib.pyplot as plt

anios = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
renovable = [200, 230, 260, 300, 350, 400, 460, 520]
convencional = [800, 790, 780, 770, 760, 750, 740, 730]

plt.figure(figsize=(8,5))
plt.stackplot(anios, renovable, convencional, labels=['Renovable', 'Convencional'], colors=['mediumseagreen', 'lightgray'])
plt.title("Comparación entre Consumo de Energía Renovable y Convencional")
plt.xlabel("Año")
plt.ylabel("Consumo de Energía (TWh)")
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()