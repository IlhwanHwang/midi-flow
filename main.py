from singable import *
from scale import Scale, scale_c_minor
from random import choice

melody1_1 = Enumerate()([
    Key(length=2/2, note=Note(1)),
    Key(length=2/2, note=Note(2)),
    Key(length=2/2, note=Note(3)),
    Key(length=2/2, note=Note(4)),
    Key(length=4/2, note=Note(2)),
    Key(length=4/2, note=Note(0)),
    Key(length=2/2, note=Note(3)),
    Key(length=2/2, note=Note(2)),
    Key(length=1/2, note=Note(3)),
    Key(length=1/2, note=Note(1)),
    Key(length=2/2, note=Note(3)),
    Key(length=2/2, note=Note(1)),
    Key(length=2/2, note=Note(6)),
    Key(length=4/2, note=Note(4)),
])

melody1_2 = Enumerate()([
    Key(length=2/2, note=Note(1)),
    Key(length=2/2, note=Note(2)),
    Key(length=2/2, note=Note(3)),
    Key(length=2/2, note=Note(4)),
    Key(length=4/2, note=Note(2)),
    Key(length=4/2, note=Note(0)),
    Key(length=2/2, note=Note(-1)),
    Key(length=2/2, note=Note(2)),
    Key(length=2/2, note=Note(1)),
    Key(length=2/2, note=Note(-1)),
    Key(length=8/2, note=Note(0)),
])

melody2_1 = Enumerate()([
    Key(length=4/2, note=Note(3)),
    Key(length=4/2, note=Note(1)),
    Key(length=6/2, note=Note(0)),
    Key(length=1/2, note=Note(2)),
    Key(length=1/2, note=Note(4)),
    Key(length=4/2, note=Note(3)),
    Key(length=4/2, note=Note(6)),
    Key(length=6/2, note=Note(4)),
    Key(length=1/2, note=Note(2)),
    Key(length=1/2, note=Note(4)),
    Key(length=4/2, note=Note(3)),
    Key(length=4/2, note=Note(1)),
    Key(length=6/2, note=Note(0)),
    Key(length=1/2, note=Note(0)),
    Key(length=1/2, note=Note(1)),
    Key(length=2/2, note=Note(2)),
    Key(length=2/2, note=Note(4)),
    Key(length=2/2, note=Note(3)),
    Key(length=2/2, note=Note(1)),
    Key(length=8/2, note=Note(0)),
])

melody3_1 = Enumerate()([
    Key(length=1/2, note=Note(0)),
    Key(length=1/2, note=Note(1)),
    Key(length=1/2, note=Note(2)),
    Key(length=1/2, note=Note(0)),
    Key(length=1/2, note=Note(1)),
    Key(length=1/2, note=Note(2)),
    Key(length=1/2, note=Note(0)),
    Key(length=1/2, note=Note(1)),
    Key(length=1/2, note=Note(2)),
    Key(length=1/2, note=Note(0)),
    Key(length=1/2, note=Note(2)),
    Key(length=1/2, note=Note(4)),
    Key(length=1/2, note=Note(3)),
    Key(length=1/2, note=Note(2)),
    Key(length=1/2, note=Note(1)),
    Key(length=1/2, note=Note(2)),
])

melody3_2 = Enumerate()([
    Key(length=1/2, note=Note(0)),
    Key(length=1/2, note=Note(1)),
    Key(length=1/2, note=Note(2)),
    Key(length=1/2, note=Note(0)),
    Key(length=1/2, note=Note(1)),
    Key(length=1/2, note=Note(2)),
    Key(length=1/2, note=Note(0)),
    Key(length=1/2, note=Note(1)),
    Key(length=1/2, note=Note(2)),
    Key(length=1/2, note=Note(0)),
    Key(length=1/2, note=Note(2)),
    Key(length=1/2, note=Note(4)),
    Key(length=4/2, note=Note(1)),
])

melody3_3 = Enumerate()([
    Key(length=1/2, note=Note(0)),
    Key(length=1/2, note=Note(1)),
    Key(length=1/2, note=Note(2)),
    Key(length=1/2, note=Note(0)),
    Key(length=1/2, note=Note(1)),
    Key(length=1/2, note=Note(2)),
    Key(length=1/2, note=Note(1)),
    Key(length=1/2, note=Note(4)),
    Key(length=8/2, note=Note(0)),
])

chord1_1 = Enumerate()([
    MultiKey(length=8/2, notes=[Note(1), Note(3), Note(5)]),
    MultiKey(length=8/2, notes=[Note(2), Note(4), Note(6)]),
    MultiKey(length=8/2, notes=[Note(1), Note(3), Note(5)]),
    MultiKey(length=8/2, notes=[Note(4), Note(6), Note(8)]),
])

chord1_2 = Enumerate()([
    MultiKey(length=8/2, notes=[Note(1), Note(3), Note(5)]),
    MultiKey(length=8/2, notes=[Note(2), Note(4), Note(6)]),
    MultiKey(length=8/2, notes=[Note(4), Note(6), Note(8)]),
    MultiKey(length=4/2, notes=[Note(0), Note(3), Note(4)]),
    MultiKey(length=4/2, notes=[Note(0), Note(2), Note(4)]),
])

chord3_1 = Enumerate()([
    MultiKey(length=16/2, notes=[Note(0), Note(2), Note(4)]),
    MultiKey(length=12/2, notes=[Note(0), Note(2), Note(4)]),
    MultiKey(length=4/2, notes=[Note(-1), Note(1), Note(3)]),
])

chord3_2 = Enumerate()([
    MultiKey(length=16/2, notes=[Note(0), Note(2), Note(4)]),
    MultiKey(length=16/2, notes=[Note(0), Note(2), Note(4)]),
])

bassarp_1 = Repeat(1)(
    Enumerate()([
        Key(length=3/4, note=Note(0)),
        Key(length=3/4, note=Note(1)),
        Key(length=2/4, note=Note(0)),
        Key(length=3/4, note=Note(1)),
        Key(length=3/4, note=Note(0)),
        Key(length=2/4, note=Note(1))
    ])
)

bassarp_2 = Repeat(1)(
    Enumerate()([
        Key(length=1/4, note=Note(0)),
        Key(length=1/4, note=Note(0)),
        Key(length=1/4, note=Note(1)),
        Key(length=1/4, note=Note(1)),
        Key(length=1/4, note=Note(0)),
        Key(length=1/4, note=Note(0)),
        Key(length=1/4, note=Note(1)),
        Key(length=1/4, note=Note(1)),
        Key(length=1/4, note=Note(0)),
        Key(length=1/4, note=Note(0)),
        Key(length=1/4, note=Note(1)),
        Key(length=1/4, note=Note(1)),
        Key(length=1/4, note=Note(0)),
        Key(length=1/4, note=Note(0)),
        Key(length=1/4, note=Note(1)),
        Key(length=1/4, note=Note(1)),
        Key(length=1/4, note=Note(0)),
        Key(length=1/4, note=Note(0)),
        Key(length=1/4, note=Note(1)),
        Key(length=1/4, note=Note(1)),
        Key(length=1/4, note=Note(0)),
        Key(length=1/4, note=Note(0)),
        Key(length=1/4, note=Note(1)),
        Key(length=1/4, note=Note(1)),
        Key(length=1/4, note=Note(0)),
        Key(length=1/4, note=Note(2)),
        Key(length=1/4, note=Note(1)),
        Key(length=1/4, note=Note(2)),
        Key(length=1/4, note=Note(0)),
        Key(length=1/4, note=Note(2)),
        Key(length=1/4, note=Note(1)),
        Key(length=1/4, note=Note(2)),
    ])
)

bassarp_3 = Repeat(1)(
    Enumerate()([
        Key(length=8/4, note=Note(0)),
        Key(length=3/4, note=Note(0)),
        Key(length=3/4, note=Note(0)),
        Key(length=2/4, note=Note(0)),
        Key(length=3/4, note=Note(0)),
        Key(length=3/4, note=Note(0)),
        Key(length=2/4, note=Note(0)),
        Key(length=3/4, note=Note(0)),
        Key(length=3/4, note=Note(0)),
        Key(length=2/4, note=Note(0)),
    ])
)

from keys.drum import *

drum_bass_1 = Enumerate()([
    Key(length=1, note=Note(bass_drum_2)),
    Key(length=1, note=Note(snare_drum_1)),
    Key(length=1, note=Note(bass_drum_2)),
    Key(length=1, note=Note(snare_drum_1))
])

drum_hat_1 = Enumerate()([
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=2/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=2/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=2/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=2/4, note=Note(closed_hi_hat)),
])

drum_bass_2 = Enumerate()([
    Key(length=1, note=Note(bass_drum_2)),
    Key(length=1, note=Note(snare_drum_1)),
    Key(length=1, note=Note(bass_drum_2)),
    Key(length=1, note=Note(snare_drum_1))
])

drum_hat_2 = Enumerate()([
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
    Key(length=1/4, note=Note(closed_hi_hat)),
])

song = Sequence()([
    AtChannel(0)(
        Articulate4(0.25)(
            Transpose(7)(
                Enumerate()([
                    melody1_1,
                    melody1_2,
                    melody1_1,
                    melody1_2,
                    melody1_1,
                    melody1_2,
                    melody1_1,
                    melody1_2,
                    melody3_1,
                    melody3_2,
                    melody3_1,
                    melody3_3,
                    Harmonize(-7)(melody3_1),
                    Harmonize(-7)(melody3_2),
                    Harmonize(-7)(melody3_1),
                    Harmonize(-7)(melody3_3),
                ])
            )
        )
    ),
    AtChannel(3)(
        ShiftTime(64)(
            Harmonize(7)(
                Enumerate()([
                    melody2_1,
                    melody2_1,
                ])
            )
        )
    ),
    AtChannel(1)(
        ShiftTime(64)(
            Transpose(-7)(
                Enumerate()([
                    chord1_1,
                    chord1_2,
                    chord1_1,
                    chord1_2
                ])
            )
        )
    ),
    AtChannel(2)(
        Amplify(2.0)(
            Transpose(-7)(
                Articulate4(0.33)(
                    Enumerate()([
                        Arpeggio()((
                            Enumerate()([
                                chord1_1,
                                chord1_2,
                                chord1_1,
                                chord1_2,
                            ]),
                            Repeat(16)(bassarp_1)
                        )),
                        Arpeggio()((
                            Enumerate()([
                                chord1_1,
                                chord1_2,
                                chord1_1,
                                chord1_2,
                            ]),
                            Repeat(8)(bassarp_2)
                        )),
                        Arpeggio()((
                            Enumerate()([
                                chord3_1,
                                chord3_2,
                                chord3_1,
                                chord3_2,
                            ]),
                            Repeat(8)(bassarp_3)
                        ))
                    ])
                )
            )
        )
    ),
    AtChannel(9)(
        Enumerate()([
            Repeat(16)(
                Sequence()([
                    Articulate4(0.5)(drum_bass_1),
                    Articulate4(0.5)(drum_hat_1)
                ])
            ),
            Repeat(16)(
                Sequence()([
                    Articulate4(0.5)(drum_bass_2),
                    Articulate4(0.5)(drum_hat_2)
                ])
            )
        ])
    )
])

# song = ShiftTime(-64)(song)

from instruments.ensemble import string_ensemble_1
from instruments.synth_lead import lead_1_square
from instruments.bass import synth_bass_1
from instruments.piano import acoustic_grand_piano
from instruments.drum_kits import standard_drum_kit

mid = to_midi(song, scale_c_minor, instruments={ 
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
