import random

class Game():
    def __init__(self, user):
        self.user = user
        self.is_finish = False

class User():
    def __init__(self, name, game=None):
        self.name = name
        self.game = game

class Mine():
    def __init__(self, is_display):
        self.value = random.randint(0,1)
        self.is_display = is_display
        self.have_flag = False

class Board():
    def __init__(self, nb_line, nb_col):
        self.nb_col = nb_col
        self.nb_line = nb_line
        self.board = {}
        for l in range(1,nb_line+1):
            self.board[l] = [{c : Mine(False)} for c in range(1,nb_col+1)]

    def get_mine_by_line_col(self, line, col):
        """
        This function get a mine by a line and column
        :param line:
        :param col:
        :return:
        """
        for a_mine in self.board[int(line)][int(col) - 1].values():
            return a_mine

    def display(self, line, col):
        """
        This function make a mine display on the board
        :param line:
        :param col:
        :return: None
        """
        for a_mine in self.board[int(line)][int(col)-1].values():
            a_mine.is_display = True

    def put_a_glag(self, line, col):
        """
        This function add a flag one a mine
        :param line:
        :param col:
        :return:
        """
        for a_mine in self.board[int(line)][int(col) - 1].values():
            a_mine.have_flag = True
            a_mine.is_display = False

    def remove_a_flag(self, line, col):
        """
        This function delete the flag on a mine
        :param line:
        :param col:
        :return:
        """
        for a_mine in self.board[int(line)][int(col) - 1].values():
            a_mine.have_flag = False
            a_mine.is_display = False

    def play(self, line, col, type_action):
        line = int(line)
        col = int(col)
       #if I dig
        if type_action == "creuser":
            for a_mine in self.board[line][col-1].values():
                self.display(line, col)
                if a_mine.value == 1:
                    #display the mine on the upper line
                    if line > 1 and a_mine.have_flag == False:
                        self.display(line-1, col)
                    #display the mine on the lower line
                    if line < self.nb_line and a_mine.have_flag == False:
                        self.display(line + 1, col)
                    #display the mine on the line at right
                    if col < self.nb_col and a_mine.have_flag == False:
                        self.display(line, col+1)
                    #display the mine on the line at left
                    if col > 1 and a_mine.have_flag == False:
                        self.display(line, col-1)
                    #display the mine on the top and left
                    if line > 1 and col > 1 and a_mine.have_flag == False:
                        self.display(line-1, col - 1)
                    #display the mine on the top and fight
                    if line > 1 and col < self.nb_col and a_mine.have_flag == False:
                        self.display(line - 1, col + 1)
                    #display the mine on the down and left
                    if line < self.nb_line and col > 1 and a_mine.have_flag == False:
                        self.display(line + 1, col - 1)
                    #display the mine on the down and right
                    if line < self.nb_line and col < self.nb_col and a_mine.have_flag == False:
                        self.display(line + 1, col + 1)
                    return True
                else:
                    return False
        #if i put a flag
        elif type_action == "drapeau":
            self.put_a_glag( line, col)
            return True
        #if I remove
        elif type_action == "retirer drapeau" :
            self.remove_a_flag( line, col)
            return True

    def __repr__(self):
        good_display = ""

        for line, col in self.board.items():
            pos_obj = 1
            for elm in self.board[line]:
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