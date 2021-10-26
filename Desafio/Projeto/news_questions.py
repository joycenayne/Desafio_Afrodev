import funcs_system as funcs
import pandas as pd 


import menus
import main

def brazil_vs_top3(data):
    brazil = data[data["Team/NOC"] == "Brazil"]["Team/NOC"].values.tolist()
    brazil_medals = data[data["Team/NOC"] == "Brazil"]["Gold"].values.tolist()

    top3_countries = data.loc[:2, "Team/NOC"].to_list()
    top3_medals = data.loc[:2, "Gold"].to_list()
    
    x_column = brazil + top3_countries
    y_column = brazil_medals + top3_medals

    funcs.graphics_plot(x_column, y_column, "Brasil VS TOP3", "Países", "Medalhas de Ouro")

def sport_max_brazilians(data):
    ath_sports = data[data.NOC == 'Brazil'].groupby(by="Discipline").count()
    sport_br = ath_sports[ath_sports.NOC == ath_sports.NOC.max()].index[0]
    count_ath_br = ath_sports[ath_sports.NOC == ath_sports.NOC.max()].values[0][0]

    ath_sports = data[data.Discipline == sport_br].groupby(by="NOC").count()
    top = ath_sports[ath_sports.Discipline == ath_sports.Discipline.max()].index[0]
    top_count = ath_sports[ath_sports.Discipline == ath_sports.Discipline.max()].values[0][0]

    x_column = ['Brazil', top]
    y_column = [count_ath_br, top_count]
    title = "Comparativo do número de atletas em {}".format(sport_br)

    funcs.graphics_plot(x_column, y_column, title, "Países", "Número de atletas")



def start_menu(news_quest):
    flag = True
    while flag:
        topic = news_quest.upper()
        dictionary = menus.m_news_questions
        data_athletes = pd.read_excel("../Arquivos/Athletes.xlsx")
        data_medals = pd.read_excel("../Arquivos/Medals.xlsx")
        print(f"\nMenu {topic}")
        
        key = funcs.input_topics(dictionary)

        if key == 1:
            brazil_vs_top3(data_medals)
        elif key == 2:
            sport_max_brazilians(data_athletes)
        else:
            flag = False
            main.menu_principal()