import numpy as np
import pandas as pd
from tabulate import tabulate
# import matplotlib.pyplot as plt


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


# Function testing
def result():
    print("1. The total infected is: ")
    print(total_infected())
    print("----------------------------------------------")
    print("2. The numbers of the affected municipalities is: ")
    print(num_affected_municipalities())
    print("----------------------------------------------")
    print("3. The affected municipalities are: ")
    print(list_affected_municipalities())
    print("----------------------------------------------")
    print("4. Those cared for at home are: ")
    print(atention_in_home())
    print("----------------------------------------------")
    print("5. Number of people recovered is: ")
    print(num_people_recovered())
    print("----------------------------------------------")
    print("6. Number of dead people is: ")
    print(num_people_killed())
    print("----------------------------------------------")
    print("7. The types of cases from highest to lowest are: ")
    print(order_type_of_case())
    print("----------------------------------------------")
    print("8. The numbers of the affected departments is: ")
    print(num_affected_department())
    print("----------------------------------------------")
    print("9. The affected depertments are: ")
    print(list_affected_department())
    print("----------------------------------------------")
    print("10. The types of care from highest to lowest are: ")
    print(order_type_of_atention())
    print("----------------------------------------------")
    print("11. The 10 most infected departments are: ")
    print(order_ten_departments_infected())
    print("----------------------------------------------")
    print("12. The 10 departments with the most deaths are: ")
    print(order_ten_departments_dead())
    print("----------------------------------------------")
    print("13. The 10 departments with the most recovered are: ")
    print(order_ten_departments_recovered())
    print("----------------------------------------------")
    print("14. The 10 most infected municipalities are: ")
    print(order_ten_municipalities_infected())
    print("----------------------------------------------")
    print("15. The 10 municipalities with the most deaths are: ")
    print(order_ten_municipalities_dead())
    print("----------------------------------------------")
    print("16. The 10 municipalities with the most recovered are: ")
    print(order_ten_municipalities_recovered())
    print("----------------------------------------------")
    print("17. The most infected cities by departments are: ")
    print(order_city_for_department())
    print("----------------------------------------------")
    print("18. Number of women and men per city are: ",)
    print(men_and_women_for_department())
    print("----------------------------------------------")
    print("----------------------------------------------")
    print("20. The most infected countries of origin are: ")
    print(order_infected_country_of_origin())
    print("----------------------------------------------")
    print("21. The number of infected by dates is: ")
    print(order_infected_date())
    print("----------------------------------------------")
    print("22. The Colombia mortality and recovery is: ")
    print(recovery_and_mortality_colombia())
    print("----------------------------------------------")
    print("23. The mortality and recovery for department is: ")
    print(recovery_and_mortality_colombia_department())
    print("----------------------------------------------")
    print("24. The mortality and recovery for city is: ")
    print(recovery_and_mortality_colombia_municipalities())
    print("----------------------------------------------")
    print("25. ")
    print("----------------------------------------------")


result()
