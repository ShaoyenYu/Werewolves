import numpy as np


class Board:
    def __init__(self, player_num: int):
        self.__player_num = player_num
        self.__role_allocation_template = {
            12: ["Werewolf"] * 4 + ["Villager"] * 5 + ["Seer", "Hunter", "Witch"]
        }
        self.__role_allocation = self.role_allocation_template[player_num]
        self.__player_role = dict(zip(range(self.__player_num), self.__role_allocation))
        self.__player_alive = self.__player_role.copy()

    @property
    def player_num(self):
        return self.__player_num

    @property
    def role_allocation_template(self):
        return self.__role_allocation_template

    @property
    def role_allocation(self):
        return self.__role_allocation

    @property
    def player_role(self):
        return self.__player_role

    @property
    def player_alive(self):
        return self.__player_alive

    def shuffle(self):
        np.random.shuffle(self.__player_role)


class Player:
    def __init__(self):
        self.__status


class Role:
    def __init__(self, player: Player):
        pass


class Action:
    pass


class Event:
    pass
