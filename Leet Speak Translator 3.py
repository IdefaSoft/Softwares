from sys import exit
SUBSTITUTIONS1 = [['_/', 'j'], ['|-|', 'H'], ['|_|', 'U'], ['_|', 'J'], ['|<', 'k'], ['><', 'x'], [')(', 'X'], ['|1/|', 'm'], [')-(', 'h'], ['|°', 'P'], ['4', 'a'], ['3', 'e'], ['1/', 'v'], ['1', 'l'], ['°', 'o'], ['†', 't'], ['/\\/\\', 'M'],['\\/\\/', 'W'], ['/\\', 'A'], ['€', 'E'], ['£', 'L'], ['0', 'O'], ['7', 'T'], ['8', 'B'], ['|:', 'b'], ['<', 'c'], ['(_,)', 'Q'], ['(_+', 'G'], ['(_)', 'u'], ['()_', 'q'], ['(', 'C'], ['[)', 'D'], ['|o', 'd'], ['/=', 'F'], ['ƒ', 'f'], ['6', 'g'], ['|\\|', 'n'], ['|*', 'p'], ['|{', 'K'], ['|\\/', 'N'], ['|', 'I'], ['!', 'i'], ['2', 'R'], ['®', 'r'], ['$', 's'], ['5', 'S'], ['\\/', 'V'], ['vv', 'w'], ['`/', 'Y'], ["'/", 'y'], ['-\\_', 'Z'], ['≥', 'z']]
SUBSTITUTIONS0= [['a', '4'], ['e', '3'], ['l', '1'], ['o', '°'], ['t', '†'], ['A', '/\\'], ['E', '€'], ['L', '£'], ['O', '0'], ['T', '7'], ['B', '8'], ['b', '|:'], ['c', '<'], ['C', '('], ['D', '[)'], ['d', '|o'], ['F', '/='], ['f', 'ƒ'], ['G', '(_+'], ['g', '6'], ['H', '|-|'], ['h', ')-('], ['I', '|'], ['i', '!'], ['J', '_|'], ['j', '_/'], ['k', '|<'], ['K', '|{'], ['M', '/\\/\\'], ['m', '|1/|'], ['n', '|\\|'], ['N', '|\\/'], ['P', '|°'], ['p', '|*'], ['q', '()_'], ['Q', '(_,)'], ['R', '2'], ['r', '®'], ['s', '$'], ['S', '5'], ['U', '|_|'], ['u', '(_)'], ['V', '\\/'], ['v', '1/'], ['w', 'vv'], ['W', '\\/\\/'], ['X', ')('], ['x', '><'], ['Y', '`/'], ['y', "'/"], ['Z', '-\\_'], ['z', '≥']]

MENU="""
 _              _     ____                   _      _____                    _       _               _____ 
| |    ___  ___| |_  / ___| _ __   ___  __ _| | __ |_   _| __ __ _ _ __  ___| | __ _| |_ ___  _ __  |___ / 
| |   / _ \/ _ \ __| \___ \| '_ \ / _ \/ _` | |/ /   | || '__/ _` | '_ \/ __| |/ _` | __/ _ \| '__|   |_ \ 
| |___  __/  __/ |_   ___) | |_) |  __/ (_| |   <    | || | | (_| | | | \__ \ | (_| | |_ (_) | |     ___) |
|_____\___|\___|\__| |____/| .__/ \___|\__,_|_|\_\   |_||_|  \__,_|_| |_|___/_|\__,_|\__\___/|_|    |____/ 
                            |_|                                                                             
                                        Créé par IdefaSoft, tous droits réservés.
Appuyez sur 'q' pour quitter, 'p' pour revenir au menu précédent.
"""
######################### Section des fonctions ##############################
def coder_message(message, substitutions):
    """Traite une chaine transmise et applique des substitutions de lettres d'après une liste d'éléments. Chaque élément est une liste de longueur 2(ancien, nouveau) """
    for s in substitutions:
        vcar = s[0]
        ncar = s[1]
        message = message.replace(vcar, ncar)
    return message

######################### Section Main ############################
print(MENU)
while True:
    message0 = input("Voulez-vous :\n1.Crypter\n2.Décrypter\nNombre :")
    if message0=='1':
        while True:
            message = input("Message à crypter :\n")
            if message == 'p':
                break
            elif message =='q':
                exit(0)
            txt_converti = coder_message(message, SUBSTITUTIONS0)
            print("Voici le message en Leet Speak :\n" + txt_converti+"\n")

    elif message0=='2':
        while True:
            message = input("Message à décrypter :\n")
            if message == 'p':
                break
            elif message =='q':
                exit(0)
            txt_converti = coder_message(message, SUBSTITUTIONS1)
            print("Voici le message traduit :\n" + txt_converti+"\n")
    elif message0=='q':
        exit(0)
    elif message0=='p':
        print(MENU)
        continue
