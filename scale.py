from math import floor 
from singable import Note

def str2key(symbol):
    tone = { 'C': 60, 'D': 62, 'E': 64, 'F': 65, 'G': 67, 'A': 69, 'B': 71 }[symbol[0].upper()]
    semitones = symbol.count('#') - symbol.count('b')
    return tone + semitones


class Scale:
    def __init__(self, base=(60, 62, 64, 65, 67, 69, 71)):
        self.base = base

    def __getitem__(self, index):
        if isinstance(index, str):
            pass

        elif isinstance(index, int):
            octave = floor(index / 7)
            i = int(index - octave * 7)
            return self.base[i] + octave * 12

        else:
            raise ValueError(index)


scale_c_major = Scale()
scale_a_minor = Scale([57, 59, 60, 62, 63, 65, 67])
scale_a_melodic_minor = Scale([57, 59, 60, 62, 64, 66, 67])
scale_a_harmonic_minor = Scale([57, 59, 60, 62, 63, 66, 67])
scale_c_minor = Scale([60, 62, 63, 65, 66, 68, 70])
