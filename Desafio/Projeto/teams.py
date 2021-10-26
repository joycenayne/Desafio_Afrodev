import funcs_system as funcs
import pandas as pd
import menus
import main

def total_teams_by_sports_country(data):
    countries = list(data["NOC"].unique())
    list_teams_countries = []
    
    for country in countries:
        dict_teams_country = {
            "País": country,
            "Times": []
        }

        data_teams_country = data[data.NOC == country].groupby(by="Discipline").count()['Event']
        sports =  list(data_teams_country.index)
        count_times = list(data_teams_country.values)

        for index in range(0, data_teams_country.shape[0]):
            dict_teams = {}
            dict_teams["Esporte"] = sports[index]
            dict_teams["Quantidade"] = count_times[index]
            dict_teams_country["Times"].append(dict_teams)
        list_teams_countries.append(dict_teams_country)
    print(f"A seguir, quantidade de times por esporte em cada país: {list_teams_countries}")


def start_menu(teams):
    flag = True
    while flag:
        topic = teams.upper()
        dictionary = menus.m_teams
        data_teams = pd.read_excel("../Arquivos/Teams.xlsx")
        print(f"\nMenu {topic}")
        
        key = funcs.input_topics(dictionary)

        if key == 1:
            total_teams_by_sports_country(data_teams)
        else:
            flag = False
            main.menu_principal()