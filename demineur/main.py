from demineur.classes import *
from demineur.fonctions import *

nom_user = input("Veuillez saisir votre pseudo : ")
choix_level = input(("Choisissez le niveau de difficulté (facile - normal - difficile) :  "))
if choix_level == "facile":
    NB_LINE, NB_COL = 4,4
elif choix_level == "normal":
    NB_LINE, NB_COL = 10,10
elif choix_level == "difficile":
    NB_LINE, NB_COL = 20,20
else :
    NB_LINE, NB_COL = 10,10


player = User(nom_user)
current_partie = Partie(player)
current_game = Game(NB_LINE, NB_COL)
combinaison_already_play = [] #Pour checker que l'on a pas deja jouer la meme combinaison
print(current_game)
while current_partie.is_finish == False:
    is_ok = False
    while is_ok == False:
        line = input("Veuillez saisir votre ligne : ")
        row = input("Veuillez saisir votre colonne : ")
        type_action = input("Choisissez une action (creuser - drapeau - retirer drapeau) : ")
        mine_saisie = current_game.get_mine_by_line_row(line, row)
        resultat_check = check_line_row_action(line, row, NB_LINE, NB_COL, combinaison_already_play, type_action, mine_saisie)
        combinaison_already_play.append(line + "-" + row)
        if resultat_check == "OK":
            is_ok = True
        else:
            print("\n" + resultat_check + "\n")
    action = current_game.play(line, row, type_action)
    nb_total_mine = NB_LINE * NB_COL
    all_finish = check_is_all_finish(current_game, nb_total_mine)

    if action == 1:
        print(current_game)
        if all_finish:
            print("Gagné !! Felicitiation "+ player.nom)
            current_partie.is_finish = True
    else:
        print(current_game)
        print("Perdu !!")
        current_partie.is_finish = True