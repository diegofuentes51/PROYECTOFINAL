# cargar_datos.py

import pandas as pd

def cargar_datos():
    # Cargar el archivo Excel
    data = pd.read_excel('C:/Users/diego/Desktop/PROYECTO_MINERIA/PROYECTOFINAL/PERU_SINIESTROS.xlsx', header=3)
    
    # Limpiar los nombres de las columnas
    data.columns = data.columns.str.strip()
    
    return data
