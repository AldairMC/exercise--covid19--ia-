import numpy as np
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import terminalplot as tp

# Variables globales
ID = 'ID de caso'
DATE_DIAGNOSTIC = 'Fecha de diagnóstico'
CITY = 'Ciudad de ubicación'
DEPARTMENT = 'Departamento o Distrito'
ATENTION = 'Atención**'
AGE = 'Edad'
GENDER = 'Sexo'
TYPE = 'Tipo*'
COUNTRY = 'País de procedencia'
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


def TO_UPPER_COUNTRY():
    new_country = [i.upper() for i in DATA[COUNTRY]]
    DATA[COUNTRY] = new_country


def FILTER(key, keyword):
    return(DATA[DATA[key] == keyword][key])


def show():
   return plt.show(block=True)

# 1. Número de casos de Contagiados en el País.
def total_infected():
    return(DATA[ID].max())


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


# 7. Ordenar de Mayor a menor por tipo de caso
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
    result = DATA.groupby(DEPARTMENT).size().sort_values(ascending=False)
    return(result.head(10))


# 12. Liste de mayor a menor los 10 departamentos con mas casos de fallecidos
def order_ten_departments_dead():
    deads = DATA[DATA[ATENTION] == "Fallecido"]
    result = deads.groupby([DEPARTMENT, ATENTION]).size()
    return(result.sort_values(ascending=False).head(10))


# 13. Liste de mayor a menor los 10 departamentos con mas casos de recuperados
def order_ten_departments_recovered():
    recovereds = DATA[DATA[ATENTION] == "Recuperado"]
    result = recovereds.groupby([DEPARTMENT, ATENTION]).size()
    return(result.sort_values(ascending=False).head(10))


# 14. Liste de mayor a menor los 10 municipios con mas casos de contagiados
def order_ten_municipalities_infected():
    TO_UPPER_CITY()
    result = DATA.groupby(CITY).size().sort_values(ascending=False).head(10)
    return(result)


# 15. Liste de mayor a menor los 10 municipios con mas casos de fallecidos
def order_ten_municipalities_dead():
    TO_UPPER_CITY()
    deads = DATA[DATA[ATENTION] == "Fallecido"]
    result = deads.groupby([CITY, ATENTION]).size()
    return(result.sort_values(ascending=False).head(10))


# 16. Liste de mayor a menor los 10 municipios con mas casos de recuperados
def order_ten_municipalities_recovered():
    TO_UPPER_CITY()
    recovereds = DATA[DATA[ATENTION] == "Recuperado"]
    result = recovereds.groupby([CITY, ATENTION]).size()
    return(result.sort_values(ascending=False).head(10))


# 17. Liste agrupado por departamento y en orden de Mayor a menor las
# ciudades con mas casos de contagiados
def order_city_for_department():
    TO_UPPER_CITY()
    TO_UPPER_DEPARTMENT()
    department = DATA.groupby([DEPARTMENT, CITY, ATENTION]).size()
    return(department.sort_values(ascending=False))


# 18. Número de Mujeres y hombres contagiados por ciudad por departamento
def men_and_women_for_department():
    TO_UPPER_CITY()
    TO_UPPER_DEPARTMENT()
    result = DATA.groupby([DEPARTMENT, CITY, GENDER]).size()
    return(result.sort_values(ascending=False))


# 20. Liste de mayor a menor el número de contagiados por país de procedencia
def order_infected_country_of_origin():
    TO_UPPER_COUNTRY()
    result = DATA.groupby(COUNTRY).size().sort_values(ascending=False)
    return(result)


# 21. Liste de mayor a menor las fechas donde se presentaron mas contagios
def order_infected_date():
    result = DATA.groupby(DATE_DIAGNOSTIC).size().sort_values(ascending=False)
    return(result)


# 22. Diga cual es la tasa de mortalidad y recuperación que
# tiene toda Colombmia
def recovery_and_mortality_colombia():
    colombia = len(DATA)
    recovery = (FILTER(ATENTION, "Recuperado").size / colombia) * 100
    mortality = (FILTER(ATENTION, "Fallecido").size / colombia) * 100
    result = pd.Series({'recovery': recovery, 'mortality': mortality})
    return(result)


# 23. Liste la tasa de mortalidad y recuperación que tiene cada departamento
def recovery_and_mortality_colombia_department():
    TO_UPPER_DEPARTMENT()
    atentions = ["Fallecido", "Recuperado"]
    data_department = DATA[ATENTION].unique()
    department = DATA[DATA[ATENTION].isin(data_department)]
    department_group = department.groupby(DEPARTMENT).size()
    result = (DATA[DATA[ATENTION].isin(atentions)].groupby([DEPARTMENT, ATENTION]).size() / department_group)*100
    return(result)


# 24. Liste la tasa de mortalidad y recuperación que tiene cada ciudad
def recovery_and_mortality_colombia_municipalities():
    TO_UPPER_CITY()
    atentions = ["Fallecido", "Recuperado"]
    data_department = DATA[ATENTION].unique()
    cities = DATA[DATA[ATENTION].isin(data_department)].groupby(CITY).size()
    result = (DATA[DATA[ATENTION].isin(atentions)].groupby([CITY, ATENTION]).size() / cities)*100
    return(result)


# 25. Liste por cada ciudad la cantidad de personas por atención
def list_atention_for_municipalities():
    TO_UPPER_CITY()
    result = DATA.groupby([CITY, ATENTION]).size().sort_values(ascending=False)
    return(result)


# 27. Grafique las curvas de contagio, muerte y recuperación de toda
# Colombia acumulados
def grafic_dead_recovery_infected_colombia():
    aux = DATA.groupby(DATE_DIAGNOSTIC).size().cumsum()
    deads = DATA[DATA[ATENTION] == "Fallecido"]
    recovereds = DATA[DATA[ATENTION] == "Recuperado"]
    group_dead = deads.groupby(DATE_DIAGNOSTIC).size().cumsum().sort_values(ascending=True)
    group_recovered = recovereds.groupby(DATE_DIAGNOSTIC).size().cumsum().sort_values()
    plt.subplot(1, 3, 1)
    plt.title("Infected")
    print(plt.plot(aux))
    plt.xticks(rotation=270)
    plt.subplot(1, 3, 2)
    plt.title("Deads")
    print(plt.plot(group_dead))
    plt.xticks(rotation=270)
    plt.subplot(1, 3, 3)
    plt.title("Recovered")
    print(plt.plot(group_recovered))
    plt.xticks(rotation=270)
    show()


# 33. Haga un gráfico de barras por Sexo de toda Colombia
def grafic_men_and_women_colombia():
    men = DATA[DATA[GENDER] == 'M'].groupby(GENDER).size()
    women = DATA[DATA[GENDER] == 'F'].groupby(GENDER).size()
    plt.subplot(1, 2, 1)
    plt.title("Men")
    print(plt.hist(men))
    plt.subplot(1, 2, 2)
    plt.title("Women")
    print(plt.hist(women))
    show()
