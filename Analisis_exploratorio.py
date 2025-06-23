import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos con la fila 4 como encabezado
data = pd.read_excel('C:/Users/diego/Desktop/PROYECTO_MINERIA/PROYECTOFINAL/PERU_SINIESTROS.xlsx', header=3)

# Limpiar los nombres de las columnas
data.columns = data.columns.str.strip()

# Mostrar las primeras 10 filas para verificar que los datos se han cargado correctamente
print("Primeras filas del archivo:")
print(data.head(10))

# Descripción de los datos
num_filas, num_columns = data.shape
print(f"Cantidad de Filas: {num_filas}")
print(f"Cantidad de Columnas: {num_columns}")

# Descripción general de las variables, tipos de datos, y valores únicos
print("\nInformación general de la Data:")
data.info()

# Mostrar los tipos de datos de las columnas
print("\nTipos de valores por columna:")
data.dtypes

# Mostrar las columnas de tipo categórico
print("\nColumnas de tipo categóricas:")
data.select_dtypes(include=['object']).columns

# Distribución de la gravedad de los accidentes
columna_letalidad = 'GRAVEDAD'
if columna_letalidad in data.columns:
    print(f"\n--- Distribución de la Gravedad/Letalidad ({columna_letalidad}) ---")
    gravedad_counts = data[columna_letalidad].value_counts(dropna=False)
    print(gravedad_counts)

    # Visualizar la distribución de la gravedad en un gráfico de barras
    plt.figure(figsize=(10, 6))
    sns.barplot(x=gravedad_counts.index, y=gravedad_counts.values, palette='Reds_d')
    plt.title(f'Distribución de la Gravedad de Accidentes ({columna_letalidad})', fontsize=16)
    plt.xlabel('Gravedad/Tipo de Daño', fontsize=14)
    plt.ylabel('Número de Accidentes', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Calcular porcentaje de cada categoría de gravedad
    gravedad_percentage = data[columna_letalidad].value_counts(normalize=True).mul(100).round(2)
    print(f"\nPorcentaje de cada categoría en '{columna_letalidad}':")
    print(gravedad_percentage)
