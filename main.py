from singable import *
from scale import scale_a_melodic_minor as scale_a_minor
from random import choice

# chord = Enumerate()([
#     MultiKey(length=4, notes=[Note(0, 0), Note(2, 0), Note(4, 0)]),
#     MultiKey(length=4, notes=[Note(-2, 0), Note(0, 0), Note(2, 0)]),
#     MultiKey(length=4, notes=[Note(-1, 0), Note(1, 0), Note(3, 0)]),
#     MultiKey(length=4, notes=[Note(2, 0), Note(4, 0), Note(6, 0)]),
# ])

# melody = Enumerate()([
#     Key(length=8/2, note=Note(2, 0)),
#     Key(length=8/2, note=Note(6, 0)),
#     Key(length=16/2, note=Note(4, 0)),

#     Key(length=12/2, note=Note(5, 0)),
#     Key(length=4/2, note=Note(4, 0)),
#     Key(length=8/2, note=Note(4, 0)),
#     Key(length=8/2, note=Note(3, 0)),
# ])



bass_reef = Enumerate()([
    Key(length=1/4, note=Note(0, 0)),
    Key(length=1/4, note=Note(0, 0)),
    Key(length=1/4, note=Note(2, 0)),
    Key(length=1/4, note=Note(0, 0)),
    Key(length=1/4, note=Note(0, 0)),
    Key(length=1/4, note=Note(2, 0)),
    Key(length=1/4, note=Note(0, 0)),
    Key(length=1/4, note=Note(0, 0)),
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
    MultiKey(length=1/4, notes=[Note(bass_drum_1), Note(closed_hi_hat)]),
    MultiKey(length=1/4, notes=[Note(bass_drum_1), Note(closed_hi_hat)]),
    MultiKey(length=1/4, notes=[Note(snare_drum_1)]),
    MultiKey(length=1/4, notes=[Note(bass_drum_2)]),
    MultiKey(length=1/4, notes=[Note(bass_drum_1), Note(closed_hi_hat)]),
    MultiKey(length=1/4, notes=[Note(bass_drum_2), Note(closed_hi_hat)]),
    MultiKey(length=1/4, notes=[Note(snare_drum_1)]),
    MultiKey(length=1/4, notes=[Note(bass_drum_2), Note(closed_hi_hat)]),
])

# drum = Repeat(4)(drum_reef)


# bass_arp = Arpeggio()((
#     Transpose(-7)(chord), 
#     Repeat(4)(bass_reef)
# ))


# chord_progression = BoundOffset(0, 1, 2)(chord)


# song = Sequence()([
#     # AtChannel(0)(melody),
#     AtChannel(1)(Amplify(0.75)(chord_progression)),
#     AtChannel(2)(bass_arp),
#     AtChannel(9)(drum)
# ])


# rhythms = [
#     [1/2, 1/2, 1/2, 1/2],
#     [2/2,      1/2, 1/2],
#     [1/2, 1/2, 2/2     ],
#     [2/2,      2/2     ],
#     [4/2,              ],
#     [3/2,           1/2],
#     [1/2, 3/2          ],
# ]

# flows8_0 = [
#     [0, 1, 2, 3, 4, 3, 2, 1],
#     [0, 0, 0, 1, 2, 3, 2, 1],
#     [0, 1, 2, 3, 2, 1, 0, 0],
# ]

# flows8_2_1 = [
#     [0, 1, 2, 3, 4, 5, 4, 3],
#     [0, 0, 0, 1, 2, 3, 4, 3],
#     [0, 1, 2, 3, 2, 1, 0, 1],
# ]
# flows16 = [
#     [0, 1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1],
# ]

# rhythm = choice(rhythms) + choice(rhythms) + choice(rhythms) + choice(rhythms)
# flow = choice(flows)

# time = 0
# melody_list = []

# for r in rhythm:
#     melody_list.append(Key(length=r, note=Note(flow[int(time * 2)], 0)))
#     time += r

# melody = Enumerate()(melody_list)

# song = melody

rhythms = [
    [2/2,      2/2,      2/2,      2/2     ],
    [1/2, 1/2, 2/2,      2/2,      2/2     ],
    [1/2, 1/2, 1/2, 1/2, 2/2,      2/2     ],
    [3/2,           1/2, 2/2,      2/2     ],
    [3/2,           1/2, 4/2,              ],
    [1/2, 1/2, 2/2,      4/2,              ],
    [4/2,                2/2,      2/2,    ],
    [6/2,                          2/2,    ],
]

rhythms += [list(reversed(rhythm)) for rhythm in rhythms]
# rhythms = [rhythm1 + rhythm2  for rhythm1 in rhythms for rhythm2 in rhythms]


chords = {
    'i': {
        'i':       (Note(0, 0), Note(2, 0), Note(4, 0)),
        'i7':      (Note(0, 0), Note(2, 0), Note(4, 0), Note(6, 0)),
        'i9':      (Note(0, 0), Note(2, 0), Note(4, 0), Note(6, 0), Note(8, 0)),
        # 'Amdelta7': (Note(0, 0), Note(2, 0), Note(4, 0), Note(6, 1)),
        # 'Am6':      (Note(0, 0), Note(2, 0), Note(4, 0), Note(5, 1)),
    },
    'ii': {
        'iidim':  (Note(1, 0), Note(3, 0), Note(5, 0)),
        'ii7b5': (Note(1, 0), Note(3, 0), Note(5, 0), Note(7, 0)),
        'ii6':   (Note(3, 0), Note(5, 0), Note(7, 0), Note(8, 0)),
    },
    'III': {
        'III':     (Note(2, 0), Note(4, 0), Note(6, 0)),
        'IIIM7':   (Note(2, 0), Note(4, 0), Note(6, 0), Note(8, 0)),
        'IIIM7#5': (Note(2, 0), Note(4, 0), Note(6, 1), Note(8, 0)),
        'III6':    (Note(2, 0), Note(4, 0), Note(6, 0), Note(7, 0)),
    },
    'iv': {
        'iv':  (Note(3, 0), Note(5, 0), Note(7, 0)),
        'iv7': (Note(3, 0), Note(5, 0), Note(7, 0), Note(9, 0)),
    },
    'V': {
        'V':   (Note(4, 0), Note(6, 0), Note(8, 0)),
        'V7':  (Note(4, 0), Note(6, 0), Note(8, 0), Note(10, 0)),
        'V9':  (Note(4, 0), Note(6, 1), Note(8, 0), Note(10, 0), Note(12, 1)),
        # 'Bb7': (Note(1, -1), Note(3, 0), Note(5, 0), Note(7, -1)),
    },
    'VI': {
        'bVI':      (Note(5, 0), Note(7, 0), Note(9, 0)),
        'bVIM7':    (Note(5, 0), Note(7, 0), Note(9, 0), Note(11, 0)),
        'bVIM9':    (Note(5, 0), Note(7, 0), Note(9, 0), Note(11, 0), Note(13, 0)),
        'bVIM6':    (Note(5, 0), Note(7, 0), Note(9, 0), Note(10, 0)),
        # 'vidim':  (Note(5, 1), Note(7, 0), Note(9, 0)),
        # 'vi7b5': (Note(5, 1), Note(7, 0), Note(9, 0), Note(11, 0)),
    },
    'VII': {
        'bVII':      (Note(6, 0), Note(8, 0), Note(10, 0)),
        'bVIIM7':    (Note(6, 0), Note(8, 0), Note(10, 0), Note(12, 0)),
        'bVIIM9':    (Note(6, 0), Note(8, 0), Note(10, 0), Note(12, 0), Note(14, 0)),
        'bVIIM6':    (Note(6, 0), Note(8, 0), Note(10, 0), Note(11, 0)),
    },
    'vii': {
        'vii#dim':  (Note(6, 1), Note(8, 0), Note(10, 0)),
        'vii#7b5': (Note(6, 1), Note(8, 0), Note(10, 0), Note(12, 0)),
    }
}

connectivity = {
    'i':   ['ii', 'III', 'iv', 'V', 'VI', 'VII', 'vii'],
    'ii':  ['i', 'V', 'vii'],
    'III': ['ii', 'iv', 'VI'],
    'iv':  ['i', 'ii', 'V', 'vii'],
    'V':   ['i', 'VI', 'vii'],
    'VI':  ['ii', 'iv'],
    'vii': ['i', 'V', 'VI'],
    'VII': ['ii', 'III', 'iv'],
}

from random import choice, uniform

prev_chord = ''

while prev_chord != 'i':

    prev_chord = ''
    current = choice(list(chords.keys()))
    progression = []
    representation = []

    for progress in range(8):
        if progress == 7:
            if current != 'i':
                prev_chord = ''
                break
            else:
                chord_name = 'i'
        else:
            chord_name = choice(list(chords[current].keys()))
        representation.append(chord_name)
        chord = MultiKey(length=4, notes=chords[current][chord_name])
        progression.append(chord)
        prev_chord = current
        current = choice(connectivity[current])

trans_key, base_key = choice(list(enumerate(['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'])))

print(f'{base_key}: {" - ".join(representation)}')

progression = Transpose(trans_key)(
    Enumerate()(progression)
)

def generate_melody(rhythm, return_factor=0.5, turbulence_factor=5, note_start=0):
    current_note = note_start
    melody = []

    for r in rhythm:
        current_note *= (1 - return_factor)
        current_note += uniform(-turbulence_factor, turbulence_factor)
        melody.append(Key(length=r, note=Note(int(current_note))))
    
    return Enumerate()(melody)

rhythm_progressions = [
    ['A', 'B', 'A', 'C', 'A', 'B', 'A', 'C'], 
    ['A', 'B', 'A', 'C', 'A', 'B', 'A', 'D'], 
    ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'], 
    ['A', 'B', 'A', 'B', 'A', 'C', 'A', 'B'], 
    ['A', 'A', 'B', 'A', 'A', 'A', 'B', 'A'], 
    ['A', 'A', 'B', 'A', 'A', 'A', 'C', 'A'], 
    ['A', 'B', 'C', 'A', 'A', 'B', 'C', 'A']
]
rhythm_progression = choice(rhythm_progressions)
rhythm_map = { key: choice(rhythms) for key in set(rhythm_progression) }
melody_map = { key: generate_melody(rhythm_map[key], note_start=choice([-1, 0, 1])) for key in set(rhythm_progression) }

print(f'progression: {" - ".join(rhythm_progression)}')

melody = Enumerate()([melody_map[key] for key in rhythm_progression])

song = Sequence()([
    AtChannel(0)(
        Arpeggio(outliers='octave')((
            Bound(1, 2)(progression),
            melody
        ))
    ),
    AtChannel(3)(
        Arpeggio(outliers='octave')((
            Bound(-1, -0)(
                progression
            ),
            Repeat(8)(Enumerate()([
                Key(length=1/4, note=Note(0)),
                Key(length=1/4, note=Note(1)),
                Key(length=1/4, note=Note(2)),
                Key(length=1/4, note=Note(3)),
                Key(length=1/4, note=Note(4)),
                Key(length=1/4, note=Note(5)),
                Key(length=1/4, note=Note(6)),
                Key(length=1/4, note=Note(7)),
                Key(length=1/4, note=Note(8)),
                Key(length=1/4, note=Note(7)),
                Key(length=1/4, note=Note(6)),
                Key(length=1/4, note=Note(5)),
                Key(length=1/4, note=Note(4)),
                Key(length=1/4, note=Note(3)),
                Key(length=1/4, note=Note(2)),
                Key(length=1/4, note=Note(1)),
            ]))
        ))
    ),
    AtChannel(1)(
        Amplify(0.5)(
            Bound(0, 1)(
                progression
            )
        )
    ),
    AtChannel(2)(
        Amplify(1)(
            Arpeggio()((
                Bound(-1, 0)(
                    Arpeggio()((
                        progression,
                        Repeat(8)(Sequence()([
                            Key(length=4, note=Note(0)),
                            Key(length=4, note=Note(1)),
                        ]))
                    ))
                ),
                Repeat(8)(bass_reef)
            ))
        )
    ),
    AtChannel(9)(
        Amplify(0.5)(
            Repeat(8)(drum_reef)
        )
    )
])

from instruments.ensemble import string_ensemble_1
from instruments.synth_lead import lead_1_square
from instruments.bass import synth_bass_1
from instruments.piano import acoustic_grand_piano
from instruments.drum_kits import standard_drum_kit

mid = to_midi(song, scale_a_minor, instruments={ 
    0: lead_1_square,
    1: string_ensemble_1,
    2: synth_bass_1,
    3: acoustic_grand_piano,
    9: standard_drum_kit
})
mid.save('new_song.mid')

import os
import subprocess
FNULL = open(os.devnull, 'w')
subprocess.call(['timidity', 'new_song.mid'], stdout=FNULL, stderr=subprocess.STDOUT)