from singable import *


x1 = Enumerate(1/2)([
    Key(length=1/2, note=Note(2)),
    Key(length=1/2, note=Note(1)),
    Key(length=1/2, note=Note(0)),
    Key(length=1/2, note=Note(1)),
])

x2 = Enumerate(1/2)([
    Key(length=1/2, note=Note(2)),
    Key(length=1/2, note=Note(2)),
    Key(length=2/2, note=Note(2)),
])

x3 = Enumerate(1/2)([
    Key(length=1/2, note=Note(1)),
    Key(length=1/2, note=Note(1)),
    Key(length=2/2, note=Note(1)),
])

x6 = Enumerate(1/2)([
    Key(length=1/2, note=Note(1)),
    Key(length=1/2, note=Note(1)),
    Key(length=1/2, note=Note(2)),
    Key(length=1/2, note=Note(1)),
    Key(length=4/2, note=Note(0)),
])

chord1 = Enumerate()([
    MultiKey(length=4, notes=[Note(0, 0), Note(2, 0), Note(4, 0)]),
    MultiKey(length=4, notes=[Note(4, 0), Note(6, 0), Note(8, 0)]),
    MultiKey(length=4, notes=[Note(3, 0), Note(5, 0), Note(7, 0)]),
    MultiKey(length=2, notes=[Note(5, 0), Note(7, 0), Note(9, 0)]),
    MultiKey(length=2, notes=[Note(6, 0), Note(8, 0), Note(10, 0)]),
])

chord2 = Enumerate()([
    MultiKey(length=4, notes=[Note(3, 0), Note(5, 0), Note(7, 0)]),
    MultiKey(length=4, notes=[Note(4, 0), Note(6, 0), Note(8, 0)]),
    MultiKey(length=4, notes=[Note(5, 0), Note(7, 0), Note(9, 0)]),
    MultiKey(length=4, notes=[Note(4, 0), Note(6, 0), Note(8, 0)]),
])

x = Enumerate()([
    Key(length=1, note=Note(0)),
    Key(length=1, note=Note(0)),
    Key(length=1, note=Note(0)),
    Key(length=1, note=Note(1)),
    Key(length=1, note=Note(0)),
    Key(length=1, note=Note(0)),
    Key(length=2, note=Note(0)),

    Key(length=1, note=Note(0)),
    Key(length=1/2, note=Note(-1)), Key(length=1/2, note=Note(-1)),
    Key(length=1, note=Note(0)),
    Key(length=1/2, note=Note(-1)), Key(length=1/2, note=Note(-1)),
    Key(length=1, note=Note(0)),
    Key(length=1/2, note=Note(0)), Key(length=1/2, note=Note(-1)),
    Key(length=2, note=Note(-3)),
    
])

x = Harmonize(7)(x)

x = Enumerate()([
    (AtChannel(1)(chord1), AtChannel(0)(x)),
    (AtChannel(1)(chord2), AtChannel(0)(x)),
    (AtChannel(1)(Harmonize(-7)(chord1)), AtChannel(0)(x)),
    (AtChannel(1)(Harmonize(-7)(chord2)), AtChannel(0)(x)),
])

mid = to_midi(x, ScaleCMinor, instruments={ 1: 48 })
mid.save('new_song.mid')

import os

os.system('timidity new_song.mid')

