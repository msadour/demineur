from demineur.classes import *
from demineur.fonctions import *

user_name = input("Veuillez saisir votre pseudo : ")
level_choice = input(("Choisissez le niveau de difficulté (facile - normal - difficile) :  "))
if level_choice == "facile":
    NB_LINE, NB_COL = 4,4
elif level_choice == "normal":
    NB_LINE, NB_COL = 10,10
elif level_choice == "difficile":
    NB_LINE, NB_COL = 20,20
else :
    NB_LINE, NB_COL = 10,10


player = User(user_name)
current_game = Game(player)
current_board = Board(NB_LINE, NB_COL)
combination_already_play = [] #Pour checker que l'on a pas deja jouer la meme combinaison
print(current_board)
while current_game.is_finish == False:
    is_ok = False
    while is_ok == False:
        line = input("Veuillez saisir votre ligne : ")
        line = line if int(line) <= NB_LINE else str(NB_LINE)
        col = input("Veuillez saisir votre colonne : ")
        col = col if int(col) <= NB_COL else str(NB_COL)
        type_action = input("Choisissez une action (creuser - drapeau - retirer drapeau) : ")

        mine_played = current_board.get_mine_by_line_col(line, col)
        result_check = check_line_col_action(line, col, NB_LINE, NB_COL, combination_already_play, type_action, mine_played)
        combination_already_play.append(line + "-" + col)
        if result_check == "OK":
            is_ok = True
        else:
            print("\n" + result_check + "\n")
    action = current_board.play(line, col, type_action)
    nb_total_mine = NB_LINE * NB_COL
    all_finish = check_is_all_finish(current_board, nb_total_mine)

    if action == 1:
        print(current_board)
        if all_finish:
            print("Gagné !! Felicitiation "+ player.name)
            current_game.is_finish = True
    else:
        print(current_board)
        print("Perdu !!")
        current_game.is_finish = True