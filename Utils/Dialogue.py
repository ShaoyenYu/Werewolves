
class Printer:
    @staticmethod
    def print_dead(players_dead: set):
        dead_num = len(players_dead)

        if dead_num != 0:
            if dead_num == 1:
                print("{0} player died last night, he/she is: {1}".format(dead_num, players_dead))

            elif dead_num >= 2:
                dead_ids = ""
                for player_dead in players_dead:
                    dead_ids += "{0} & ".format(player_dead)
                dead_ids = dead_ids[:-3]
                print("{0} players died last night, they are: {1}".format(dead_num, dead_ids))
        else:
            print("Oops, silent night~")


