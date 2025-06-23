# preparacion_datos.py

from cargar_datos import cargar_datos  # Importar la función que carga los datos

# Cargar los datos utilizando la función de cargar_datos
data = cargar_datos()

# Selección de los datos para Lima
data_lima = data[data['DEPARTAMENTO'] == 'LIMA']

# Selección de las variables relevantes
variables_seleccionadas = [
    'TIPO PERSONA', 'GRAVEDAD', 'EDAD', 'SEXO', 'POSEE LICENCIA', 'ESTADO LICENCIA',
    'CLASE_LICENCIA', '¿SE SOMETIÓ A DOSAJE ETÍLICO CUALITATIVO?', 'RESULTADO DEL DOSAJE ETÍLICO CUALITATIVO',
    '¿SE SOMETIÓ A DOSAJE ETÍLICO CUANTITATIVO?', 'VEHÍCULO', 'MES', 'DIA', 'HORA', 'CLASE DE SINIESTRO',
    'CAUSA', 'CAUSA ESPECIFICA', 'TIPO DE VÍA', 'RED VIAL'
]

# Filtrar las columnas seleccionadas
data_lima = data_lima[variables_seleccionadas]

# Verificar los datos después de la selección de variables
print(data_lima.head(10))
