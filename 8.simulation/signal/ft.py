import math

def fourier_transform(signal):
    N = len(signal)
    spectrum = []
    
    for i in range(N):
        re, im = 0.0, 0.0
        for j in range(N):
            angle = 2 * math.pi * i * j / N
            re += signal[j] * math.cos(angle)
            im -= signal[j] * math.sin(angle)
        spectrum.append((re, im))
    
    return spectrum