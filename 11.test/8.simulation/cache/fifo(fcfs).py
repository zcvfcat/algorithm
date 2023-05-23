def fifo(pages, frames):
    frame_list = [-1] * frames
    page_faults = 0
    len_pages = len(pages)
    
    queue = []

    for i in range(len_pages):
        if pages[i] in frame_list:
            continue
        else:
            page_faults += 1

            if -1 in frame_list:
                frame_list[frame_list.index(-1)] = pages[i]
                queue.append(pages[i])
            else:
                idx = frame_list.index(queue.pop(0))
                frame_list[idx] = pages[i]
                queue.append(pages[i])

    return page_faults

pages = [1, 2, 3, 4, 5, 6, 7]
frames = 4

print(fifo(pages, frames))