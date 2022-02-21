def try_me(*args):
    import random
    
    if 4 in args:
        return "Goodbye!" 

    pfc_dict={1: "Pierre", 2: "Feuille", 3: "Ciseau"}
    comp_count = 0
    user_count = 0
    print("Bienvenue à une fabuleuse partie de Pierre, Feuille, Ciseau!\nLe premier à 3 points a gagné.")

    while comp_count < 3 and user_count < 3:
        my_val = int(input("Entrez un chiffre entre 1 et 3, pour :\n1: pierre, \n2: feuille ou \n3: ciseau : "))
        computer_play = random.randint(1, 3)

        print(f"Tu joues {pfc_dict.get(my_val)}, je joue {pfc_dict.get(computer_play)}...\n")
        if int(my_val) == 1:
            if computer_play == 1:
                print("Egalité!")
            elif computer_play == 2: 
                print("La feuille EXPLOOOSE la pierre. 1 point pour bibi !")
                comp_count += 1
            elif computer_play == 3:
                print("La pierre gagne maladroitement contre le ciseau, 1 point pour toi...")
                user_count += 1
        elif int(my_val) == 2:
            if computer_play == 1:
                print("La feuille gagnerait contre la pierre... 1 point pour toi, ça me fait mal.")
                user_count += 1
            elif computer_play == 2: 
                print("Egalité!")
            elif computer_play == 3:
                print("LE CISEAU DECOUPE LA FEUILLE !! 1 point pour MOI !!")
                comp_count += 1
        elif int(my_val) == 3:
            if computer_play == 1:
                print("La pierre brise le pauvre ciseau, qui tombe lamentablement en morceaux au sol... DOMMAGE!! Point pour moii !!!")
                comp_count += 1
            elif computer_play == 2: 
                print("Whaat ? Tu joues ciseau, tout ça pour découper ma feuille... Point pour toi, petit tricheur...")
                user_count += 1
            elif computer_play == 3:
                print("Egalité!")
        elif my_val == 4:
            return "Goodbye!"
        else:
            print("j'ai dit de choisir un nombre entre 1 et 3 :)")
        print(f"Score : {user_count} à {comp_count}\n")
    if comp_count > user_count:
        return "Victoire du cerveau quantique contre le biologique !"
    else:
        return "... c'était écrit, tu es plus fort que moi. Ca me fait mal."

if __name__ == '__main__':
    pass