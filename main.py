from singable import *
from scale import scale_a_minor

chord = Enumerate()([
    MultiKey(length=2, notes=[Note(0, 0), Note(2, 0), Note(4, 0)]),
    MultiKey(length=2, notes=[Note(6, 0), Note(8, 0), Note(10, 0)]),
    MultiKey(length=4, notes=[Note(0, 0), Note(2, 0), Note(4, 0)]),

    MultiKey(length=2, notes=[Note(5, 0), Note(7, 0), Note(9, 0)]),
    MultiKey(length=2, notes=[Note(0, 0), Note(2, 0), Note(4, 0)]),
    MultiKey(length=2, notes=[Note(2, 0), Note(4, 0), Note(6, 0)]),
    MultiKey(length=2, notes=[Note(6, 0), Note(8, 0), Note(10, 0)]),
])

melody = Enumerate()([
    Key(length=4/2, note=Note(2, 0)),
    Key(length=4/2, note=Note(6, 0)),
    Key(length=8/2, note=Note(4, 0)),

    Key(length=6/2, note=Note(5, 0)),
    Key(length=2/2, note=Note(4, 0)),
    Key(length=4/2, note=Note(4, 0)),
    Key(length=4/2, note=Note(3, 0)),
])


bass_reef = Enumerate()([
    Key(length=1/4, note=Note(0, 0)),
    Key(length=1/4, note=Note(0, 0)),
    Key(length=1/4, note=Note(2, 0)),
    Key(length=1/4, note=Note(0, 0)),
    Key(length=1/4, note=Note(0, 0)),
    Key(length=1/4, note=Note(2, 0)),
    Key(length=1/4, note=Note(0, 0)),
    Key(length=1/4, note=Note(0, 0)),
])


from keys.drum import *

drum_reef = Enumerate()([
    MultiKey(length=1/4, notes=[Note(bass_drum_1), Note(closed_hi_hat)]),
    MultiKey(length=1/4, notes=[Note(bass_drum_1), Note(closed_hi_hat)]),
    MultiKey(length=1/4, notes=[Note(snare_drum_1)]),
    MultiKey(length=1/4, notes=[Note(bass_drum_2)]),
    MultiKey(length=1/4, notes=[Note(bass_drum_1), Note(closed_hi_hat)]),
    MultiKey(length=1/4, notes=[Note(bass_drum_2), Note(closed_hi_hat)]),
    MultiKey(length=1/4, notes=[Note(snare_drum_1)]),
    MultiKey(length=1/4, notes=[Note(bass_drum_2), Note(closed_hi_hat)]),
])

drum = Repeat(8)(drum_reef)


bass_arp = Arpeggio()((
    Transpose(-7)(chord), 
    Repeat(8)(bass_reef)
))


chord_progression = BoundOffset(0, 1, 2)(chord)


song = Sequence()([
    AtChannel(0)(melody),
    AtChannel(1)(Amplify(0.75)(chord_progression)),
    AtChannel(2)(bass_arp),
    AtChannel(9)(drum)
])


from instruments.ensemble import string_ensemble_1
from instruments.piano import acoustic_grand_piano
from instruments.bass import synth_bass_1
from instruments.drum_kits import standard_drum_kit

mid = to_midi(song, scale_a_minor, instruments={ 
    0: acoustic_grand_piano,
    1: string_ensemble_1,
    2: synth_bass_1,
    9: standard_drum_kit
})
mid.save('new_song.mid')

import os

os.system('timidity new_song.mid')

