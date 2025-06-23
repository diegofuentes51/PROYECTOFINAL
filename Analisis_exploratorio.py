import pandas as pd
import matplotlib.pyplot as plt

# Primero se carga los archivos de excel con la fila 4 
data = pd.read_excel('C:/Users/diego/Desktop/PROYECTO_MINERIA/PROYECTOFINAL/PERU_SINIESTROS.xlsx', header=3)

# Aqui lo que se hacees que se limpia los nombres de las columnas  
data.columns = data.columns.str.strip()

# Aqui vemos los primeros 10 registros para verificar la carga de los datos
# Luego mostramos las primeras 10 filas para tener una idea general de cómo se cargaron los datos
print("Primeras filas del archivo:")
print(data.head(10))

# Verificamos los nombres de las columnas
# Este paso permite verificar que los nombres de las columnas están correctamente cargados  para que no tengamos errores en los sigguiente analisis
print("\nNombres de las columnas:")
print(data.columns)

# Aqui vamos a ver la distribucion de los accidentes de transito
# aqui vamos analisar cuantos accidentes de transito ocurrieron por cada categoria
gravedad_counts = data['GRAVEDAD'].value_counts()
print("Distribución de la gravedad de los accidentes:")
print(gravedad_counts)

# Aqui vamos a ver la la distribución de la gravedad de los accidentes
# Aquí se genera un gráfico de barras para visualizar cuántos accidentes ocurrieron en cada categoría de gravedad
gravedad_counts.plot(kind='bar', title='Distribución de la gravedad de los accidentes')
plt.xlabel('Gravedad')
plt.ylabel('Número de accidentes')
plt.xticks(rotation=45)
plt.show()

# Accidentes por departamento
# Aqui vamos a ver cuántos accidentes ocurrieron en cada departamento
dept_counts = data['DEPARTAMENTO'].value_counts()
print("\nAccidentes por departamento:")
print(dept_counts)

# Visualizar los accidentes por departamento
# Aqui vamos a vercuántos accidentes ocurrieron en cada departamento en  un grafico de barras
dept_counts.plot(kind='bar', title='Accidentes por departamento')
plt.xlabel('Departamento')
plt.ylabel('Número de accidentes')
plt.xticks(rotation=45)
plt.show()

# Accidentes por mes
# En este paso, se analiza la cantidad de accidentes ocurridos en cada mes
mes_counts = data['MES'].value_counts()
print("\nAccidentes por mes:")
print(mes_counts)

# Visualizar los accidentes por mes
# Este gráfico de barras muestra cuántos accidentes ocurrieron en cada mes
mes_counts.plot(kind='bar', title='Accidentes por mes')
plt.xlabel('Mes')
plt.ylabel('Número de accidentes')
plt.xticks(rotation=45)
plt.show()

# Verificar los nombres de las columnas nuevamente para asegurarnos de que todo esté correcto
# Al final, se verifica que los nombres de las columnas sean correctos
print("\nNombres finales de las columnas:")
print(data.columns)

