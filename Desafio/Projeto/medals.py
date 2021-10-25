from Desafio.Projeto.teams import total_teams_by_sports_country
import funcs_system as funcs
import pandas as pd 
import menus
import main

def total_medals_country(data):
    data["Total_Medals"] = data["Gold"] + data["Silver"] + data["Bronze"]    
    return data

def listing_countries_medals(data):
    list_countries_medal = [(row["Team/NOC"], row["Total_Medals"]) for _, row in data.iterrows()]
    list_count_medal = funcs.format_string(list_countries_medal)
    return list_count_medal

def list_total_medals_country(data):
    data_med = total_medals_country(data)
    data_med = data_med.loc[:, ["Team/NOC", "Total_Medals"]]
    list_country_medals = listing_countries_medals(data_med)
    print(f"A seguir, quantidade de medalhas por cada país: {list_country_medals}")

def country_max_gold(data):
    country = data[data["Gold"] == data["Gold"].max()]["Team/NOC"][0]
    print(f"O país com mais medalhas de ouro é {country}")

def country_max_silver(data):
    country = data[data["Silver"] == data["Silver"].max()]["Team/NOC"][0]
    print(f"O país com mais medalhas de prata é {country}")

def country_max_bronze(data):
    country = data[data["Bronze"] == data["Bronze"].max()]["Team/NOC"][0]
    print(f"O país com mais medalhas de bronze é {country}")

def countries_min_gold(data):
    countries = data[data["Gold"] == data["Gold"].min()]["Team/NOC"]
    countries = funcs.format_string(countries)
    print(f"Os países com menos medalhas de ouro são: {countries}")

def countries_min_silver(data):
    countries = data[data["Silver"] == data["Silver"].min()]["Team/NOC"]
    countries = funcs.format_string(countries)
    print(f"Os países com menos medalhas de prata são: {countries}")

def countries_min_bronze(data):
    countries = data[data["Bronze"] == data["Bronze"].min()]["Team/NOC"]
    countries = funcs.format_string(countries)
    print(f"Os países com menos medalhas de bronze são: {countries}")

def ranking_total_medals(data):
    data_medal = total_medals_country(data)
    data_medal = data_medal.sort_values(by="Total_Medals", ascending=False)
    list_ranking = listing_countries_medals(data_medal)
    print(f"Ranking por total de medalhas: {list_ranking}")


def start_menu(medals):
    flag = True
    while flag:
        topic = medals.upper()
        dictionary = menus.m_medals
        data_medals = pd.read_excel("../Arquivos/Medals.xlsx")
        print(f"\nMenu {topic}")
        
        key = funcs.input_topics(dictionary)

        if key == 1:
            list_total_medals_country(data_medals)
        elif key == 2:
            country_max_gold(data_medals)
        elif key == 3:
            country_max_silver(data_medals)
        elif key == 4:
            country_max_bronze(data_medals)
        elif key == 5:
            countries_min_gold(data_medals)
        elif key == 6:
            countries_min_silver(data_medals)
        elif key == 7:
            countries_min_bronze(data_medals)
        elif key == 8:
            ranking_total_medals(data_medals)
        if key == -1:
            flag = False
            main.menu_principal()