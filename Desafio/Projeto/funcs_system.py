import matplotlib.pyplot as plt
import numpy as np

def verification_topics(choice, dic):
    if choice in dic.keys():
        return True
    else:
        print("Opção Inválida! \n")



def input_topics(dic):
    dictionary = dic
    print("\nSobre o que você deseja saber? \n")
    for chave, valor in dictionary.items():
        print(f"Digite {chave} para {valor}.")

    flag = True
    while flag:
        choice = input("\nSua opção: ")

        try:
            choice_int = int(choice)
            check = verification_topics(choice_int, dictionary)
            if check == True:
                flag = True
                return choice_int
            else:
                ans_exit = input("Você deseja sair?\n")
                if 'sim' == ans_exit.lower():
                    flag = False
                    return -1
                elif 's' == ans_exit.lower():
                    flag = False
                    return -1
                else:
                    continue                
        except ValueError:
            print("Por favor, digite um número.")

def format_string(list_string):
    text = str(list_string)
    text_formated = text.replace("[", "").replace("]", "").replace("'", "")
    return text_formated


def graphics_plot(x_column, y_column, title, x_label, y_label):
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title(title)

    plt.xticks(rotation=90)
    plt.ylim(0,np.max(y_column)+20)

    bar_graph = plt.bar(x_column, y_column, width=0.3)
    j = 0
    for b in bar_graph:
        width = b.get_width()
        height = b.get_height()
        x, y = b.get_xy()
        plt.text(x+width/2,
                y+height,
                str(round(y_column[j], 2))+'\n',
                ha='center',
                weight='bold')
        j+=1
    plt.show()