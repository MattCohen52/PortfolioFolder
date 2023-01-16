# Professional wrestling match for the world heavyweight champion
# Player selects a wrestler
# That wrestler faces off against the designated champion
# A match occurs between the two wrestlers and the winner is the champion

import random

rock = "The Rock"
stone_cold = "Stone Cold Steve Austin"
undertaker = "The Undertaker"
kane = "Kane"
champ = "Triple H"

rock_stamina = 120
stone_cold_stamina = 150
undertaker_stamina = 110
kane_stamina = 100
champ_stamina = 140

rock_power = 60
stone_cold_power = 70
undertaker_power = 95
kane_power = 90
champ_power = 80

rock_finisher = "Rock Bottom"
stone_cold_finisher = "Stunner"
undertaker_finisher = "Tombstone Piledriver"
kane_finsher = "Chokeslam"
champ_finisher = "Pedigree"


while True:
    print("Welcome to Wrestlemania! It is time for the main event.\n")
    print("1) The Rock \n" "2) Stone Cold \n" "3) The Undertaker \n" "4) Kane \n")
    wrestler = input(
        "The World Champion needs an opponent. Choose your wrestler: ")
    wrestler = (wrestler.lower())
# Task 3
    if wrestler == "1" or wrestler == "The Rock":
        wrestler = rock
        wrestler_stamina = rock_stamina
        wrestler_power = rock_power
        wrestler_finisher = rock_finisher
        break
    elif wrestler == "2" or wrestler == "Stone Cold Steve Austin":
        wrestler = stone_cold
        wrestler_stamina = stone_cold_stamina
        wrestler_power = stone_cold_power
        wrestler_finisher = stone_cold_finisher
        break
    elif wrestler == "3" or wrestler == "The Undertaker":
        wrestler = undertaker
        wrestler_stamina = undertaker_stamina
        wrestler_power = undertaker_power
        wrestler_finisher = undertaker_finisher
        break
    elif wrestler == "4" or wrestler == "Kane":
        wrestler = kane
        wrestler_stamina = kane_stamina
        wrestler_power = kane_power
        wrestler_finisher = kane_finsher
        break
    else:
        print("That wrestler is not on the card tonight\n")
print(
    f"\nYou have chosen: {wrestler}. {wrestler}'s stamina is {wrestler_stamina} and is power is {wrestler_power}.")
print(
    f"The World Champion, {champ}, has arrived. His stamina is {champ_stamina} and his power is {champ_power}. \nThe match begins!\n")


while True:
    move_set = ["Suplex", "Body Slam", "Neck Breaker",
                "Drop Kick", "Side Slam", "German Suplex", "Clothesline", "Hip Toss"]
    wrestler_move = random.choice(move_set)
    champ_move = random.choice(move_set)
    champ_stamina = champ_stamina - wrestler_power
    print(f"{wrestler} hits {champ} with a {wrestler_move}!")
    print(f"{champ}'s stamina is now {champ_stamina}.\n")
    pass

    if champ_stamina <= 0:
        print(f"{wrestler} hits the {wrestler_finisher} on {champ}")
        print(f"{wrestler} pins {champ}....1....2....3!\nWe have a new champion!")
        break

    wrestler_stamina = wrestler_stamina - champ_power
    print(f"{champ} hits {wrestler} with a {champ_move}!")
    print(f"{wrestler}'s stamina is now {wrestler_stamina}.\n")

    if wrestler_stamina <= 0:
        print(f"{champ} hits the {champ_finisher} on {wrestler}")
        print(
            f"{champ} pins {wrestler}....1....2....3!\nThe champion has retained his championship!")
        break
