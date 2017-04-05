import numpy as np
app.py
__all__ = ["Game", "Role", "Action"]

_role_template = {
    12: ["Werewolf"] * 4 + ["Villager"] * 5 + ["Seer", "Hunter", "Witch"]
}


class Game:
    def __init__(self, player_num):
        self._player_num = player_num
        self._role_allocation = _role_template[player_num]
        self._player_role = dict(zip(range(self._player_num), self._role_allocation))
        # self.shuffle()
        self._players = dict(
            zip(self._player_role.keys(), [Player(idx, role) for idx, role in self._player_role.items()])
        )
        self._board = Board(self._players)

    def __repr__(self):
        return "A {0.player_num!r}-Player Werewolves Game!".format(self)

    def __str__(self):
        return "Total Players: {0.player_num!s}\nPlayers Roles: {0.player_role!s}".format(self)

    def shuffle(self):
        np.random.shuffle(self._player_role)
        self._players = dict(
            zip(self._player_role.keys(), [Player(idx, role) for idx, role in self._player_role.items()])
        )
        self._board = Board(self._players)

    @property
    def player_num(self):
        return self._player_num

    @property
    def player_role(self):
        return self._player_role

    @property
    def role_allocation(self):
        return self._role_allocation

    @property
    def players(self):
        return self._players

    @property
    def board(self):
        return self._board


class Board:
    def __init__(self, players: dict):
        self._players = players

    @property
    def players_alive(self):
        return [player for player in self._players.values() if player.is_alive is True]

    @property
    def groups(self):
        _roles = set([player.role.role for player in self.players_alive])
        _groups = {role: [] for role in _roles}
        for player in self.players_alive:
            _groups[player.role.role].append(player)
        return _groups


class Player:
    def __init__(self, idx, role):
        self._idx = idx
        self._role = Role(role)
        self._is_alive = True

    def __repr__(self):
        return "Player {0.idx!r}({0.role!r})".format(self)

    @property
    def idx(self):
        return self._idx

    @property
    def role(self):
        return self._role

    @property
    def is_alive(self):
        return self._is_alive

    @is_alive.setter
    def is_alive(self, value):
        self._is_alive = value


class Role:
    def __init__(self, role):
        self._role = role
        self._target = None
        self._act = Action.action.get(role)

        if self.role == "Wolf":
            pass
        elif self._role == "Villager":
            pass
        elif self.role == "Witch":
            self._potion = {-1: True, 1: True}
            self._target = {-1: None, 1: None}
        elif self._role == "Seer":
            self._foreseen = {}
        elif self._role == "Hunter":
            pass
        else:
            pass

    def __repr__(self):
        return "{0.role!r}".format(self)

    @property
    def role(self):
        return self._role

    def act(self, target=None, **kwargs):
        self._act(self, target, **kwargs)


class Action:
    def kill(self, target: Player):
        self._target = target

    def use_potion(self, target: Player, **kwargs):
        if kwargs["potion_type"] == -1 and self._potion[-1]:
            self._potion[-1] = False
            self._target[-1] = target
            target.is_alive = False

    def foresee(self, target: Player):
        self._foreseen[target] = target.role

    def revenge(self, target: Player):
        self._target = target
        target.is_alive = False

    action = {
        "Werewolf": kill,
        "Witch": use_potion,
        "Hunter": revenge,
        "Seer": foresee
    }


class Event:
    pass


g = Game(12)
b = g.board
a = b.players_alive
v = a[4]
w = a[11]
s = a[9]
h = a[10]

r = Role("Witch")


