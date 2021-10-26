import menus

import funcs_system as funcs
import news_questions as nq
import athletes as ath
import coaches as coach
import sports as sport
import teams as team
import medals as medal


def menu_principal():
    print("Olá, Bem-vinde!")
    print("\nSistema de Curiosidades sobre as Olímpiadas de Toquio 2021!")
    key = funcs.input_topics(menus.m_major)
    if key in (-1, 7):
        print("\n\nObrigada por utilizar o Sistema de Curiosidades sobre as Olímpiadas de Toquio 2021!\n")
    else:
        path_topics(menus.m_major[key])

def path_topics(choice):
    ans = choice.lower()
    if ans == 'atletas':
        ath.start_menu(choice)
    elif ans == 'treinadores':
        coach.start_menu(choice)
    elif ans == 'esportes':
        sport.start_menu(choice)
    elif ans == 'times':
        team.start_menu(choice)
    elif ans == 'medalhas':
        medal.start_menu(choice)
    elif ans == 'analises':
        nq.start_menu(choice)


if __name__ == '__main__':
    menu_principal()
