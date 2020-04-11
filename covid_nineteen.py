import numpy as np
import pandas as pd
from tabulate import tabulate
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

def TO_UPPER_CITY():
    new_city = [i.upper() for i in DATA[CITY]]
    DATA[CITY] = new_city

def TO_UPPER_DEPARTMENT():
    new_department = [i.upper() for i in DATA[DEPARTMENT]]
    DATA[DEPARTMENT] = new_department

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

# 5. Número de personas que se encuentran recuperados
def num_people_recovered():
    return(FILTER(ATENTION, 'Recuperado').size)

# 6. Número de personas que ha fallecido
def num_people_killed():
    return(FILTER(ATENTION, 'Fallecido').size)

# 7. Ordenar de Mayor a menor por tipo de caso (Importado, en estudio, Relacionado)
def order_type_of_case():
    aux = pd.DataFrame({'Type': TYPE_OF_CASE()})
    result = aux.groupby('Type').size().sort_values(ascending=False)
    return(result)

# 8. Número de departamentos afectados
def num_affected_department():
    return(DEPARTMENTS().unique().size)

# 9. Liste los departamentos afectados(sin repetirlos)
def list_affected_department():
    return(DEPARTMENTS().unique())

# 10. Ordene de mayor a menor por tipo de atención
def order_type_of_atention():
    return(DATA.groupby(ATENTION).size().sort_values(ascending=False))

# 11. Liste de mayor a menor los 10 departamentos con mas casos de contagiados
def order_ten_departments_infected():
    return(DATA.groupby(DEPARTMENT).size().sort_values(ascending=False).head(10))

# 12. Liste de mayor a menor los 10 departamentos con mas casos de fallecidos
def order_ten_departments_dead():
    deads = DATA[DATA[ATENTION] == "Fallecido"]
    result = deads.groupby([DEPARTMENT, ATENTION]).size().sort_values(ascending=False).head(10)
    return(result)

# 13. Liste de mayor a menor los 10 departamentos con mas casos de recuperados
def order_ten_departments_recovered():
    recovereds = DATA[DATA[ATENTION] == "Recuperado"]
    result = recovereds.groupby([DEPARTMENT, ATENTION]).size().sort_values(ascending=False).head(10)
    return(result)

# 14. Liste de mayor a menor los 10 municipios con mas casos de contagiados
def order_ten_municipalities_infected():
    TO_UPPER_CITY()
    result = DATA.groupby(CITY).size().sort_values(ascending=False).head(10)
    return(result)

# 15. Liste de mayor a menor los 10 municipios con mas casos de fallecidos
def order_ten_municipalities_dead():
    TO_UPPER_CITY()
    deads = DATA[DATA[ATENTION] == "Fallecido"]
    result = deads.groupby([CITY, ATENTION]).size().sort_values(ascending=False).head(10)
    return(result)

# 16. Liste de mayor a menor los 10 municipios con mas casos de recuperados
def order_ten_municipalities_recovered():
    TO_UPPER_CITY()
    recovereds = DATA[DATA[ATENTION] == "Recuperado"]
    result = recovereds.groupby([CITY, ATENTION]).size().sort_values(ascending=False).head(10)
    return(result)

# 17. Liste agrupado por departamento y en orden de Mayor a menor las
# ciudades con mas casos de contagiados
def order_city_for_department():
    TO_UPPER_CITY()
    TO_UPPER_DEPARTMENT()
    department = DATA.groupby([DEPARTMENT, CITY, ATENTION]).size().sort_values(ascending=False)
    return(department)

# 18. Número de Mujeres y hombres contagiados por ciudad por departamento
def men_and_women_for_department():
    TO_UPPER_CITY()
    TO_UPPER_DEPARTMENT()
    result = DATA.groupby([DEPARTMENT, CITY, GENDER]).size().sort_values(ascending=False)
    return(result)

# def average_age_men_and_women():
#     TO_UPPER_CITY()
#     aux = DATA[DATA[DEPARTMENT] == "Bogotá D.C."]
#     men = aux.groupby([DEPARTMENT, CITY, GENDER, AGE])
#     result = men[AGE].sum().head(20)
#     # aux = pd.DataFrame(men)
#     # print(tabulate(aux, tablefmt='psql'))
#     print(men.size())
#
# average_age_men_and_women()



# Function testing
def result():
    print("1. The total infected is: ", total_infected())
    print("----------------------------------------------")
    print("2. The numbers of the affected municipalities is: ", num_affected_municipalities())
    print("----------------------------------------------")
    print("3. The affected municipalities are: ", list_affected_municipalities())
    print("----------------------------------------------")
    print("4. Those cared for at home are: ", atention_in_home())
    print("----------------------------------------------")
    print("5. Number of people recovered is: ", num_people_recovered())
    print("----------------------------------------------")
    print("6. Number of dead people is: ", num_people_killed())
    print("----------------------------------------------")
    print("7. The types of cases from highest to lowest are: ", order_type_of_case())
    print("----------------------------------------------")
    print("8. The numbers of the affected departments is: ", num_affected_department())
    print("----------------------------------------------")
    print("9. The affected depertments are: ", list_affected_department())
    print("----------------------------------------------")
    print("10. The types of care from highest to lowest are: ", order_type_of_atention())
    print("----------------------------------------------")
    print("11. The 10 most infected departments are: ", order_ten_departments_infected())
    print("----------------------------------------------")
    print("12. The 10 departments with the most deaths are: ", order_ten_departments_dead())
    print("----------------------------------------------")
    print("13. The 10 departments with the most recovered are: ", order_ten_departments_recovered())
    print("----------------------------------------------")
    print("14. The 10 most infected municipalities are: " , order_ten_municipalities_infected())
    print("----------------------------------------------")
    print("15. The 10 municipalities with the most deaths are: ", order_ten_municipalities_dead())
    print("----------------------------------------------")
    print("16. The 10 municipalities with the most recovered are: ", order_ten_municipalities_recovered())
    print("----------------------------------------------")
    print("17. The most infected cities by departments are: ", order_city_for_department())
    print("----------------------------------------------")
    print("18. Number of women and men per city are: ", men_and_women_for_department())
    print("----------------------------------------------")
    print("----------------------------------------------")
    print("----------------------------------------------")
# result()
