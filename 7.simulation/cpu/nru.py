def init_frame(num_frames):
    frames = [None] * num_frames
    nru_bits = [0] * num_frames

    return frames, nru_bits

def access_page(frames, nru_bits, page):
    if page in frames:
        frame_index = frames.index(page)
        nru_bits[frame_index]
    else:
        replace_page(frames, nru_bits, page)

def replace_page(frames, nru_bits, page):
    for i in range(len(frames)):
        if 0 not in nru_bits:
            nru_bits = [0] * len(frames)

        frame_index = nru_bits.index(0)

        frames[frame_index] = page
        nru_bits[frame_index] = 1
        return

num_frames = 3
pages = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8]

frames, nru_bits = init_frame(num_frames)

for page in pages:
    access_page(frames, nru_bits, page)
    print(frames)