# visualizacion_datos.py

import matplotlib.pyplot as plt
import seaborn as sns
from cargar_datos import cargar_datos  # Importa la función que carga los datos

# Cargar los datos usando la función de cargar_datos
data = cargar_datos()

# Visualización de la distribución de la gravedad de los accidentes
gravedad_counts = data['GRAVEDAD'].value_counts()
gravedad_counts.plot(kind='bar', title='Distribución de la gravedad de los accidentes')
plt.xlabel('Gravedad')
plt.ylabel('Número de accidentes')
plt.xticks(rotation=45)
plt.show()

# Visualizar los accidentes por departamento
dept_counts = data['DEPARTAMENTO'].value_counts()
dept_counts.plot(kind='bar', title='Accidentes por departamento')
plt.xlabel('Departamento')
plt.ylabel('Número de accidentes')
plt.xticks(rotation=45)
plt.show()

# Visualizar los accidentes por mes
mes_counts = data['MES'].value_counts()
mes_counts.plot(kind='bar', title='Accidentes por mes')
plt.xlabel('Mes')
plt.ylabel('Número de accidentes')
plt.xticks(rotation=45)
plt.show()

# Gráfico circular por sexo
sexo_counts = data['SEXO'].value_counts(dropna=False)
plt.figure(figsize=(8, 8))
plt.pie(sexo_counts, labels=sexo_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title('Distribución de Accidentes por Sexo', fontsize=16)
plt.axis('equal')
plt.show()
