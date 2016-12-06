from importlib import reload
from Dev import Gameutils as gu
reload(gu)

g = gu.Game(12)
b = g.board
a = b.players_alive
v = a[4]
w = a[11]

r = gu.Role("Witch")
