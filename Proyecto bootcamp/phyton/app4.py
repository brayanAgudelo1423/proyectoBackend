import matplotlib.pyplot as plt


anios = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]


eolica = [60, 70, 85, 100, 120, 140, 160, 180]      
solar = [20, 30, 45, 60, 80, 100, 130, 160]       
geotermica = [10, 11, 12, 13, 14, 15, 16, 17]    

plt.figure(figsize=(8,5))
plt.plot(anios, eolica, marker='o', label='Eólica')
plt.plot(anios, solar, marker='s', label='Solar')
plt.plot(anios, geotermica, marker='^', label='Geotérmica')

plt.title("Tendencia en la Capacidad Instalada de Energías Renovables")
plt.xlabel("Año")
plt.ylabel("Capacidad Instalada (GW)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()