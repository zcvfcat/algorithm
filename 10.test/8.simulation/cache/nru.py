def nru(pages, frames):
    frame_list = [-1] * frames
    ref_bits = [0] * frames

    page_faults = 0
    len_pages = len(pages)

    for i in range(len_pages):
        if pages[i] in frame_list:
            ref_bits[frame_list.index(pages[i])] = 1
        else:
            page_faults += 1

            for j in range(frames):
                if frame_list[j] == -1 or ref_bits[j] == 0:
                    frame_list[j] = pages[i]
                    ref_bits[j] = 1
                    break
                else:
                    ref_bits[j] = 0

    return page_faults

pages = [1, 2, 3, 4, 5, 1, 6, 7, 8, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
frames = 4

print(nru(pages, frames))