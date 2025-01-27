""" J'ai choisi de coder en Python """

class AwaleBoard:
    def __init__(self):
        self.board = {
            'A': 4, 'B': 4, 'C': 4, 'D': 4, 'E': 4, 'F': 4,
            'G': 4, 'H': 4, 'I': 4, 'J': 4, 'K': 4, 'L': 4
        }
    
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

# Affichage initial
plateau.display()

# Vérification si le plateau est vide
print("Le plateau est-il vide ?", plateau.isEmpty())

# Simulation : vider toutes les cases
for case in plateau.board:
    plateau.board[case] = 0

# Affichage après vidage
plateau.display()
print("Le plateau est-il vide ?", plateau.isEmpty())

# Création des joueurs
player1 = Player("Alice")
player2 = Player("Bob")

# Afficher leurs scores initiaux
print(player1)
print(player2)

# Incrémenter les score
player1.increment_score(4)
player2.increment_score(6)

# Afficher les scores après incrémentation
print(player1)
print(player2)



