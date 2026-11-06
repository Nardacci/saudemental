"""Fundo musical sintetizado (sem direitos autorais). Gera flavia.wav (calmo) e andre.wav (leve)."""
import sys
import numpy as np
import wave

sr = 44100


def note(f, dur):
    t = np.arange(int(sr * dur)) / sr
    s = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * 2 * f * t) + 0.12 * np.sin(2 * np.pi * 3 * f * t)
    return s * (0.85 + 0.15 * np.sin(2 * np.pi * 0.25 * t))


def env(n, a, r):
    e = np.ones(n)
    na, nr = int(a * sr), int(r * sr)
    e[:na] = np.linspace(0, 1, na)
    e[-nr:] = np.linspace(1, 0, nr)
    return e


def render(chords, seg, dur, name):
    n = int(sr * dur)
    out = np.zeros(n)
    for i, ch in enumerate(chords):
        start = int(i * seg * sr)
        for f in ch:
            s = note(f, seg + 1.5)
            s = s * env(len(s), 1.5, 1.5)
            end = min(n, start + len(s))
            out[start:end] += s[:end - start]
    out /= np.max(np.abs(out))
    out *= 0.5
    rev = out.copy()
    for d, g in [(0.23, 0.35), (0.47, 0.25), (0.71, 0.18)]:
        k = int(d * sr)
        rev[k:] += g * out[:-k]
    rev /= np.max(np.abs(rev))
    rev *= 0.6
    fade = int(1.0 * sr)
    rev[:fade] *= np.linspace(0, 1, fade)
    rev[-fade:] *= np.linspace(1, 0, fade)
    w = wave.open(name, 'wb')
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(sr)
    w.writeframes((rev * 32767).astype(np.int16).tobytes())
    w.close()


if __name__ == '__main__':
    out = sys.argv[1]
    A2, C3, E3, F3, G3, B3, D4 = 110.0, 130.81, 164.81, 174.61, 196.0, 246.94, 293.66
    A3, C4, E4, F4, G4, A4 = 220.0, 261.63, 329.63, 349.23, 392.0, 440.0
    render([[A2, A3, C4, E4], [F3, A3, C4, F4], [C3, G3, C4, E4], [G3, B3, D4, G4]], 5.0, 20, out + '/flavia.wav')
    render([[C3, G3, E4, C4 * 2], [G3, D4, G4, B3 * 2], [A2 * 2, E4, A4, C4 * 2], [F3, C4, F4, A4]], 5.0, 20, out + '/andre.wav')
