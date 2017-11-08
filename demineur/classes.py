import random

class Partie():
    def __init__(self, user):
        self.user = user
        self.is_finish = False

class User():
    def __init__(self, nom, partie=None):
        self.nom = nom
        self.partie = partie

    def play(self, jeu, line, row):
        la_mine_jouer = jeu[line][row]
        if la_mine_jouer.value == 1:
            la_mine_jouer.is_display = True
            return "OK"
        else:
            return "perdu"
            self.partie.is_finish = True


class Mine():
    def __init__(self, is_display):
        self.value = random.randint(0,1)
        self.is_display = is_display
        self.have_flag = False


class Game():

    def __init__(self, nb_ligne, nb_col):
        self.nb_col = nb_col
        self.nb_ligne = nb_ligne
        self.jeu = {}
        for l in range(1,nb_ligne+1):
            self.jeu[l] = [{c : Mine(False)} for c in range(1,nb_col+1)]

    def get_mine_by_line_row(self, line, col):
        for une_mine in self.jeu[int(line)][int(col) - 1].values():
            return une_mine

    def display(self, line, col):
        for une_mine in self.jeu[int(line)][int(col)-1].values():
            une_mine.is_display = True

    def display_with_flag(self, line, col):
        for une_mine in self.jeu[int(line)][int(col) - 1].values():
            # if une_mine.is_display == False:
            une_mine.have_flag = True
            une_mine.is_display = False

    def display_wihout_flag(self, line, col):
        for une_mine in self.jeu[int(line)][int(col) - 1].values():
            # if une_mine.is_display == False:
            une_mine.have_flag = False
            une_mine.is_display = False

    def play(self, line, col, type_action):
        line = int(line)
        col = int(col)
       #Si on creuse
        if type_action == "creuser":
            for une_mine in self.jeu[line][col-1].values():
                self.display(line, col)
                #On affiche celui de la ligne du dessus
                if line > 1 and une_mine.have_flag == False:
                    self.display(line-1, col)
                #On affiche celui de la ligne du dessous
                if line < self.nb_ligne and une_mine.have_flag == False:
                    self.display(line + 1, col)
                #On affiche celui à sa droite
                if col < self.nb_col and une_mine.have_flag == False:
                    self.display(line, col+1)
                #On affiche celui à sa gauche
                if col > 1 and une_mine.have_flag == False:
                    self.display(line, col-1)
                #On affiche celui en haut à gauche
                if line > 1 and col > 1 and une_mine.have_flag == False:
                    self.display(line-1, col - 1)
                #On affiche celui en haut à droite
                if line > 1 and col < self.nb_col and une_mine.have_flag == False:
                    self.display(line - 1, col + 1)
                #On affiche celui en bas à gauche
                if line < self.nb_ligne and col > 1 and une_mine.have_flag == False:
                    self.display(line + 1, col - 1)
                #On affiche celui en bas à droite
                if line < self.nb_ligne and col < self.nb_col and une_mine.have_flag == False:
                    self.display(line + 1, col + 1)

                if une_mine.value == 1:
                    return True
                else:
                    return False
        elif type_action == "drapeau":
            self.display_with_flag( line, col)
            return True
        elif type_action == "retirer drapeau" :
            self.display_wihout_flag( line, col)
            return True

    def __repr__(self):
        good_display = ""

        for line, col in self.jeu.items():
            pos_obj = 1
            for elm in self.jeu[line]:
                if elm[pos_obj].is_display == False:
                    is_display = "."
                else:
                    is_display = elm[pos_obj].value

                if elm[pos_obj].have_flag == True:
                    is_display = "@"

                good_display = good_display + str(is_display) + " "
                pos_obj += 1
            good_display += "\n"
        return good_display