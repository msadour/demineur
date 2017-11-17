def check_line_col_action(line, col, nb_line, nb_col, combination_already_play, type_action, mine_played):
    try:
        line=int(line)
        col=int(col)
    except Exception:
        return "La ligne et la colonne doivent etre des entiers !"

    combination = str(line)+"-"+str(col)
    if line > nb_line:
        return "La ligne saisie ne doit pas depasser " + str(nb_line) + " !!"
    elif col > nb_col:
        return "La colonne saisie ne doit pas depasser " + str(nb_col) + " !!"
    elif combination in combination_already_play and type_action == "creuser" and mine_played.have_flag == True:
        return "Vous avez deja jouer cette combinaison ligne/colonne !!"
    elif type_action == "drapeau" and mine_played.is_display == True:
        return "Impossible de deposer un drapeau sur une mine deja creusé"
    elif type_action not in ["creuser","drapeau","retirer drapeau"]:
        return "Veuillez saisir une action proposé par la liste !!"
    else:
        return "OK"


def check_is_all_finish(current_board, nb_total_mine):
    # Ici on va checker si toute les mines ont été devoilé ou non
    nb_mine_display = 0

    for one_line in current_board.board.values():
        for one_mine_dict in one_line:
            for one_mine in one_mine_dict.values():
                if one_mine.is_display == True and one_mine.have_flag == False:
                    nb_mine_display += 1

    if nb_mine_display == nb_total_mine:
        return True