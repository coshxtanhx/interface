from pico2d import *
from collections import defaultdict

SE_COMPLETED = 'sound/zrescue.wav'
SE_GAZE_CHECK = ['sound/piano_%d.wav' % i for i in range(1, 5)]

class SoundEffect:
    se_dict = defaultdict(str)
    volume = 64
    se = None
    def __init__(self):
        pass
    def play(self, snd):
        if not SoundEffect.se_dict[snd]:
            SoundEffect.se_dict[snd] = load_wav(snd)
        SoundEffect.se = SoundEffect.se_dict[snd]
        SoundEffect.se.set_volume(SoundEffect.volume)
        SoundEffect.se.play()

sound_effect = SoundEffect()