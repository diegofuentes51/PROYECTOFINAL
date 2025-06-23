import pandas as pd

# Cargar los datos
data = pd.read_excel('C:/Users/diego/Desktop/PROYECTO_MINERIA/PROYECTOFINAL/PERU_SINIESTROS.xlsx', header=3)

# Limpiar los nombres de las columnas
data.columns = data.columns.str.strip()

# Eliminar columnas con alto porcentaje de valores nulos
columnas_a_eliminar = ['RESULTADO DEL DOSAJE ETÍLICO CUALITATIVO', 'POSEE LICENCIA']
data = data.drop(columns=columnas_a_eliminar)

# Imputar valores nulos en las columnas de dosaje
columnas_dosaje_a_imputar = ['¿SE SOMETIÓ A DOSAJE ETÍLICO CUALITATIVO?', '¿SE SOMETIÓ A DOSAJE ETÍLICO CUANTITATIVO?']
for col in columnas_dosaje_a_imputar:
    if col in data.columns:
        data[col].fillna('Desconocido', inplace=True)

# Asegurarse de que 'EDAD' sea numérica y los no numéricos sean NaN
data['EDAD'] = pd.to_numeric(data['EDAD'], errors='coerce')

# Calcular la mediana de la columna 'EDAD'
mediana_edad = data['EDAD'].median()

# Imputar los valores nulos con la mediana
data['EDAD'].fillna(mediana_edad, inplace=True)

# Verificar si hay valores nulos restantes
print(data.isnull().sum())
