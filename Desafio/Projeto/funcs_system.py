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