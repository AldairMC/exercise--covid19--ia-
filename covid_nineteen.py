import numpy as np
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

# Functions of the suport
def MUNICIPALITIES():
    return(pd.Series([i.upper() for i in DATA[CITY]]))

def DEPARTMENTS():
    return(pd.Series([i.upper() for i in DATA[DEPARTMENT]]))

def TYPE_OF_CASE():
    return(pd.Series([i.upper() for i in DATA[TYPE]]))

def FILTER(key, keyword):
    return(DATA[DATA[key] == keyword][key])


# 1. Número de casos de Contagiados en el País.
def total_infected():
    return(DATA[ID].size)

# 2. Número de Municipios Afectados
def num_affected_municipalities():
    return(MUNICIPALITIES().unique().size)

# 3. Liste los municipios afectados (sin repetirlos)
def list_affected_municipalities():
    return(MUNICIPALITIES().unique())

# 4. Número de personas que se encuentran en atención en casa
def atention_in_home():
    return(FILTER(ATENTION, 'Casa').size)

#5. Número de personas que se encuentran recuperados
def num_people_recovered():
    return(FILTER(ATENTION, 'Recuperado').size)

#6. Número de personas que ha fallecido
def num_people_killed():
    return(FILTER(ATENTION, 'Fallecido').size)

# 7. Ordenar de Mayor a menor por tipo de caso (Importado, en estudio, Relacionado)
def order_type_of_case():
    aux = pd.DataFrame({'Type' : TYPE_OF_CASE()})
    result = aux.groupby('Type').size().sort_values(ascending=False)
    return(result)

#8. Número de departamentos afectados
def num_affected_department():
    return(DEPARTMENTS().unique().size)



# Function testing
def result():
    print("1. The total infected is: ", total_infected())
    print("2. The numbers of the affected municipalities is: ", num_affected_municipalities())
    print("3. The affected municipalities are: ", list_affected_municipalities())
    print("4. Those cared for at home are: ", atention_in_home())
    print("5. Number of people recovered is: ", num_people_recovered())
    print("6. Number of dead people is: ", num_people_killed())
    print("7. The types of cases from highest to lowest are: ", order_type_of_case())
    print("8. The numbers of the affected departments is: ", num_affected_department())
result()
