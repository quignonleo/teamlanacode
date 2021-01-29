from character2 import * 
from random import choice


dico_monstres = {
    "Vermeer Bonhomme" : monster(15, 5, 55, 10),
    "Jérémy Pervitesse" : monster(15, 5, 20, 1000),
    "Morgane Piko" : monster(30, 5, 10, 20),
    "Victor Pachy" : monster(50, 0, 20, 2),
    "Boval" : monster(10, 10, 10, 20)
    "Tibaldo Arrato Primo de la Manana de la Muerte de la Tolosa": monster(5, 50, 90, 5)
    }

inventaire = [potion(10,10,10),equipment("épée",20,0,0)]

dico_marchand = {
    "Elyes Kaak" : pnj(inventaire,100)
}




liste_endroits_possibles = []
liste_endroits_possibles_monstres = []
for i in range (1001):
    for j in range (701):
        if screen[i,j] == ".":
            liste_endroits_possibles.append((i,j))
        if screen[i, j] == "#"
            liste_endroits_possibles_monstres.append((i,j))
pos = choice(liste_endroits_possibles)
dico_map[pos] = choice(dico_equip.keys())
screen[pos] = "o"
pos = choice(liste_endroits_possibles)
dico_map[pos] = choice(dico_equip.keys())
screen[pos] = "o"
pos = choice(liste_endroits_possibles_monstres)
dico_map[pos] = choice(dico_monstres.keys())
screen[pos] = "M"