# analisis.py

import pandas as pd

# Cargar los datos
data = pd.read_excel('C:/Users/diego/Desktop/PROYECTO_MINERIA/PROYECTOFINAL/PERU_SINIESTROS.xlsx')

# Análisis simple
print(f"Total de accidentes de tránsito: {len(data)}")
