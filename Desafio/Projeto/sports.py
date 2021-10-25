import funcs_system as funcs
import menus
import main

def start_menu(sports):
    flag = True
    while flag:
        topic = sports.upper()
        dictionary = menus.m_sports
        print(f"\nMenu {topic}")
        
        key = funcs.input_topics(dictionary)

        if key == 1:
            print(dictionary[key])
            pass
        elif key == 2:
            pass
        elif key == 3:
            pass
        if key == -1:
            flag = False
            main.menu_principal()
