import matplotlib.pyplot as plt

ciudades = ['Medellín', 'Cali', 'Ibagué', 'Cartagena']
personas = [80912,53454,43455,32121]
plt.bar (ciudades,personas)
plt.title('Ciudades vs Población')
plt.xlabel('Ciudades Colombianas')
plt.ylabel('Población')
plt.savefig('GraficoCiudades.png')
plt.show()
