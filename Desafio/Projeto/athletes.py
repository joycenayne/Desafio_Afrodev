import funcs_system as funcs
import pandas as pd
import menus
import main


def total_atletas(data):
    athletes_list = list(data["Name"].unique())
    total = len(athletes_list)
    print(f"Participaram, no total, {total} atletas.")

def participants_male(data):
    total_male = list(data["Male"].values)
    print(f"Participaram, no total, {sum(total_male)} atletas homens.")

def participants_female(data):
    total_female = list(data["Female"].values)
    print(f"Participaram, no total, {sum(total_female)} atletas mulheres.")

def start_menu(athletes):
    flag = True
    while flag:
        topic = athletes.upper()
        dictionary = menus.m_athletes
        data_atheletes = pd.read_excel("../Arquivos/Athletes.xlsx")
        data_gender = pd.read_excel("../Arquivos/EntriesGender.xlsx")
        
        print(f"\nMenu {topic}")
        
        key = funcs.input_topics(dictionary)


        if key == 1:
            total_atletas(data_atheletes)
        elif key == 2:
            participants_male(data_gender)
        elif key == 3:
            participants_female(data_gender)
        else:
            flag = False
            main.menu_principal()