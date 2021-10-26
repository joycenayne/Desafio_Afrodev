import funcs_system as funcs
import pandas as pd
import menus
import main

def sports_participants(data):
    list_sports = list(data["Discipline"].unique())
    list_sport_format = funcs.format_string(list_sports)
    print(f"\nOs esportes parcipantes das Olímpiadas, foram:\n{list_sport_format}")

def total_participants_by_sports(data):
    data["Total_participants"] = data["Female"] + data["Male"]
    list_part = [(row["Discipline"], row["Total_participants"]) for _, row in data.iterrows()]
    list_par_format = funcs.format_string(list_part)
    print(f"\nA seguir, a quantidade de participantes por esportes:\n{list_par_format}")

def sports_by_gender(data, larger, smaller):
    list_sports = []
    for _, row in data.iterrows():
        if (row[larger] > row[smaller]):
            list_sports.append(row["Discipline"])
    return list_sports

def sports_more_women(data):
    sports_female = sports_by_gender(data, "Female", "Male")
    sports_fem_format = funcs.format_string(sports_female)
    print(f"\nOs esportes com mais mulheres, são:\n{sports_fem_format}")

def sports_more_men(data):
    sports_female = sports_by_gender(data, "Male", "Female")
    sports_fem_format = funcs.format_string(sports_female)
    print(f"\nOs esportes com mais homens, são:\n{sports_fem_format}")

def start_menu(sports):
    flag = True
    while flag:
        topic = sports.upper()
        dictionary = menus.m_sports
        data_gender = pd.read_excel("../Arquivos/EntriesGender.xlsx")
        print(f"\nMenu {topic}")
        
        key = funcs.input_topics(dictionary)

        if key == 1:
            sports_participants(data_gender)
        elif key == 2:
            total_participants_by_sports(data_gender)
        elif key == 3:
            sports_more_men(data_gender)
        elif key == 4:
            sports_more_women(data_gender)
        else:
            flag = False
            main.menu_principal()
