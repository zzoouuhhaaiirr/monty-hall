import numpy as np
from enum import Enum
 
class Strategie(Enum):
    GARDER = 0
    CHANGER = 1
 
def play(nbtous):
    """Simulation du jeu de Monty Hall"""
 
    results = np.array([])
 
    # Portes disponibles au début du jeu
    doors = np.array([1, 2, 3])
 
    # Porte où se cache la voiture
    car = np.random.randint(1,4,1)
 
    # Porte choisie par le candidat
    choice = np.random.randint(1,4,1)
 
    # Portes que le présentateur peut ouvrir
    open_doors = np.setdiff1d(doors,[car, choice])
 
    # Porte ouverte par le présentateur
    open_door = np.random.choice(open_doors, 1)
 
    # Porte qui reste fermée après l'ouverture du présentateur
    other_closed_door = np.setdiff1d(doors, [choice, open_door])
 
    if other_closed_door == car:
        results = np.append(results, 1)
    else:
        results = np.append(results, 0)
 
    return results
 
