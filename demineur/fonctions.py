def check_line_row_action(line, row, nb_line, nb_row, combinaison_already_play, type_action, mine_saisie):
    try:
        line=int(line)
        row=int(row)
    except Exception:
        return "La ligne et la colonne doivent etre des entiers !"

    combinaison = str(line)+"-"+str(row)
    if line > nb_line:
        return "La ligne saisie ne doit pas depasser " + str(nb_line) + " !!"
    elif row > nb_row:
        return "La colonne saisie ne doit pas depasser " + str(nb_row) + " !!"
    elif combinaison in combinaison_already_play and type_action == "creuser" and mine_saisie.have_flag == True:
        return "Vous avez deja jouer cette combinaison ligne/colonne !!"
    elif type_action == "drapeau" and mine_saisie.is_display == True:
        return "Impossible de deposer un drapeau sur une mine deja creusé"
    elif type_action not in ["creuser","drapeau","retirer drapeau"]:
        return "Veuillez saisir une action proposé par la liste !!"
    else:
        return "OK"


def check_is_all_finish(current_game, nb_total_mine):
    # Ici on va checker si toute les mines ont été devoilé ou non
    nb_mine_display = 0

    for one_line in current_game.jeu.values():
        for one_mine_dict in one_line:
            for one_mine in one_mine_dict.values():
                if one_mine.is_display == True and one_mine.have_flag == False:
                    nb_mine_display += 1

    if nb_mine_display == nb_total_mine:
        return True
