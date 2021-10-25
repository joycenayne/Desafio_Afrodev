import funcs_system as funcs
import pandas as pd
import menus
import main

def listing_coaches(dict):
    list_compr_coaches = [(chave, len(valor)) for chave, valor in dict.items()]
    return list_compr_coaches

def coaches_by_country(data):
    dic_coaches = data.groupby(by='NOC').groups
    list_coaches = listing_coaches(dic_coaches)
    return list_coaches

def total_output(data):
    list_coaches = coaches_by_country(data)
    list_format = funcs.format_string(list_coaches)
    print(f"A seguir, quantidade de treinadores por país: {list_format}")

def country_max_value_coach(data):
    coaches_country = coaches_by_country(data)
    coaches_country = sorted(coaches_country, key=lambda x: x[1], reverse=True)
    country_max_value = coaches_country[0]
    str_country = f"O país {country_max_value[0]} é o que possue o maior número treinadores,"
    str_value = f"tendo o total de {country_max_value[1]} treinadores." 
    print(str_country + str_value)

def coaches_by_sport(data):
    dic_coaches = data.groupby(by='Discipline').groups
    list_coaches = listing_coaches(dic_coaches)
    list_format = funcs.format_string(listing_coaches)
    print(f"A seguir, quantidade de treinadores por esportes: {list_format}")


def start_menu(coaches):
    flag = True
    while flag:
        topic = coaches.upper()
        dictionary = menus.m_coaches
        data_coaches = pd.read_excel("../Arquivos/Coaches.xlsx")
        print(f"\nMenu {topic}")
        
        key = funcs.input_topics(dictionary)

        if key == 1:
            total_output(data_coaches)
        elif key == 2:
            country_max_value_coach(data_coaches)
        elif key == 3:
            coaches_by_sport(data_coaches)
        else:
            flag = False
            main.menu_principal()