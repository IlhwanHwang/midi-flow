from singable import *

x1 = Enumerate()([
    Key(length=1/2, note=Note(0)),
    Key(length=1/2, note=Note(1)),
    Key(length=6/2, note=Note(2)),
])

x = Enumerate()([
])


from instruments.ensemble import string_ensemble_1
from instruments.piano import acoustic_grand_piano

mid = to_midi(x, ScaleCMinor, instruments={ 
    0: acoustic_grand_piano,
    1: string_ensemble_1
})
mid.save('new_song.mid')

import os

os.system('timidity new_song.mid')

