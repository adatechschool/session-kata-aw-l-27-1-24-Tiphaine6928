""" J'ai choisi de coder en Python """

class AwaleBoard:
    def __init__(self):
        self.board = {
            'A': 4, 'B': 4, 'C': 4, 'D': 4, 'E': 4, 'F': 4,
            'G': 4, 'H': 4, 'I': 4, 'J': 4, 'K': 4, 'L': 4
        }
        self.cases = list(self.board.keys())
    
    def display(self):
        """
        Affiche le plateau dans la console sous forme d'une rangée du haut et une rangée du bas.
        """
        upper_row = " ".join(f"{key}:{self.board[key]}" for key in "ABCDEF")
        lower_row = " ".join(f"{key}:{self.board[key]}" for key in "GHIJKL")
        print("Rangée 1 (haut) :", upper_row)
        print("Rangée 2 (bas)  :", lower_row)
    
    def isEmpty(self):
        """
        Vérifie si toutes les cases du plateau sont vides (toutes les graines à 0).
        :return: True si toutes les cases sont vides, sinon False.
        """
        return all(value == 0 for value in self.board.values())

    def next_case(self, current_case, reverse=False):
        index = self.cases.index(current_case)
        if reverse:
            return self.cases[(index - 1) % len(self.cases)]
        else:
            return self.cases[(index + 1) % len(self.cases)]
    
    def saw(self, start_case):
        seeds = self.board[start_case]
        if seeds == 0:
            raise ValueError("La case de départ est vide, impossible de semer.")

        self.board[start_case] = 0
        current_case = start_case

        while seeds > 0:
            current_case = self.next_case(current_case)
            self.board[current_case] += 1
            seeds -= 1

    def harvest(self, start_case, Player):
        total_seeds = 0
        current_case = start_case

        while True:
            seeds = self.board[current_case]
            if seeds == 0:
                break
            total_seeds += seeds
            self.board[current_case] = 0
            current_case = self.next_case(current_case, reverse=True)

        Player.increment_score(total_seeds)
        return total_seeds

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def increment_score(self, points):
        if points < 0:
            raise ValueError("Le nombre de points doit être positif.")
        self.score += points
    
    def __str__(self):
        return f"Joueur: {self.name}, Score: {self.score}"

# Initialisation du plateau
plateau = AwaleBoard()
player1 = Player("Alice")
player2 = Player("Bob")

# Affichage initial
print("Etat initial du plateau :")
plateau.display()

# Semer pour le joueur 1
print("Alice sème à partir de la case 'B':")
plateau.saw('B')
plateau.display()

# Récolter pour le joueur 2
print("Bob récolte à partir de la case 'H':")
graines_recoltees = plateau.harvest('H', player2)
print(f"Graines récoltées par Bob : {graines_recoltees}")
plateau.display()

# Affichage des scores des joueurs
print("Scores des joueurs :")
print(player1)
print(player2)



