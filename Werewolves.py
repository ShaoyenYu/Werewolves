import Games
from Utils import Dialogue
from Dev import Gameutils as gu

num_players = 12
g = gu.Game(12)
b = g.board
a = b.players_alive
v = a[4]
w = a[11]
s = a[9]
h = a[10]

# Cupid, Thief
# roles = ["Werewolf", "Villager", "Seer", "Hunter", "Witch"]


g.shuffle()

role_allocation = g.role_allocation
players_role = g.player_role


players_alive = players_role.copy()
potion = {-1, 1}
player_poisoned = set()
player_healed = set()
players_dead = set()
time = "n"

while True:
    print("\n\nCurrent board:", players_alive)
    # Werewolves move
    player_wounded = {int(input("\nWerewolves. eat someone ^_^:"))}

    # Witch move
    if "Witch" in players_alive.values():
        if -1 in potion and 1 in potion:
            operation_type = int(input(
                "\nWitch, {0} is dying, would you like to\n    1: save him/her,\n    -1:poison someone and let them die together ❤\n    0:just sleep zZZ:".format(
                    player_wounded)))

            if operation_type == 1:
                player_healed = player_wounded
                potion -= {operation_type}
            elif operation_type == -1:
                player_poisoned = {int(input("Well, choose a lucky guy (I strongly recommend RJ to you)"))}
                potion -= {operation_type}
            elif operation_type == 0:
                print("zZZ")
                pass

        elif -1 not in potion and 1 in potion:
            operation_type = int(input(
                "\nWitch, {0} is dying, would you like to\n    1:save him/her\n    0:just sleep zZZ:".format(
                    player_wounded)))
            if operation_type == 1:
                player_healed = player_wounded
                potion -= {operation_type}
            elif operation_type == 0:
                print("zZZ")
                pass

        elif -1 in potion and 1 not in potion:
            operation_type = int(input("\nWitch,\n    -1:poison someone\n    0:just sleep zZZ:".format(player_wounded)))
            if operation_type == -1:
                player_poisoned = {int(input("Well, choose a lucky guy (I strongly recommend RJ to you)"))}
                potion -= {operation_type}
            elif operation_type == 0:
                print("zZZ")
                pass
        else:
            print("zZZ")
            pass

    # Seer move
    if "Seer" in players_alive.values():
        player_foreseen = int(input("\nSeer, choose one to identify his/her role:"))
        print("He/She is a >>>{0}<<<".format(players_role[player_foreseen]))

    players_dead = player_wounded.union(player_poisoned) - player_healed
    player_healed.clear()
    player_poisoned.clear()

    if players_dead:
        for player_dead in players_dead:
            del players_alive[player_dead]
        Dialogue.Printer.print_dead(players_dead)
        players_dead.clear()

    # Check whether game is over
    villagers_alive = list(players_alive.values()).count("Villager")
    werewolves_alive = list(players_alive.values()).count("Werewolf")
    specialroles_alive = len(players_alive) - villagers_alive - werewolves_alive

    if villagers_alive == 0 or specialroles_alive == 0 or werewolves_alive >= len(players_alive) / 2:
        print("Werewolves win the game!")
        break
    elif werewolves_alive == 0:
        print("Villagers win this game!")
        break
