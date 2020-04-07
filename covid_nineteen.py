# import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

"""
Variables
    ID de caso
    Fecha de diagnóstico
    Ciudad de ubicación
    Departamento o Distrito
    Atención**
    Edad
    Sexo
    Tipo*
    País de procedencia
"""

# Variables globales
ID = 'ID de caso'
DATE_DIAGNOSTIC = 'Fecha de diagnóstico'
CITY = 'Ciudad de ubicación'
DEPARTMENT = 'Departamento o Distrito'
ATENTION = 'Atención**'
AGE = 'Edad'
GENDER = 'Sexo'
TYPE = 'Tipo*'
CONTRY = 'País de procedencia'
URL = 'casos.csv'
DATA = pd.read_csv(URL)

# 1. Número de casos de Contagiados en el País.
def total_infected():
    return(len(DATA[ID]))

def result():
    print("The total infected is: ", total_infected())

result()
