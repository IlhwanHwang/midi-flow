from math import floor 

class Scale:
    def __init__(self, base=(60, 62, 64, 65, 67, 69, 71)):
        self.base = base

    def __getitem__(self, index):
        octave = floor(index / 7)
        i = int(index - octave * 7)
        return self.base[i] + octave * 12


scale_c_major = Scale()
scale_a_minor = Scale([57, 59, 60, 62, 64, 65, 67])
scale_c_minor = Scale([60, 62, 63, 65, 67, 68, 70])
