import math

def fft(signal):
    n = len(signal)
    
    if n == 1:
        return signal

    # divide
    even_signal = fft(signal[0::2])
    odd_signal = fft(signal[1::2])

    w_factor = math.exp(-2j * math.pi / n)
    w = 1
    result = [0] * n

    # conquer
    for i in range(n//2):
        result[i] = even_signal[i] + w * odd_signal[i]
        result[i + n//2] = even_signal[i] - w * odd_signal[i]
        w *= w_factor

    return result