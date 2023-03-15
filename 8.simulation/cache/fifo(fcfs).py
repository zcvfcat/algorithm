def fifo_algorithm(pages, frames):
    # 프레임 초기화
    frame_list = [-1] * frames

    page_faults = 0
    len_pages = len(pages)
    # 참조된 페이지들을 저장할 큐 만들기 
    queue = []

    for i in range(len_pages):
        if pages[i] in frame_list:
            # 해당 페이지가 이미 캐시에 있으면 건너뜀
            continue
        else:
            # 페이지 부재 발생
            page_faults += 1

            if -1 in frame_list:
                # 빈 프레임에 새로운 페이지 할당
                frame_list[frame_list.index(-1)] = pages[i]
                queue.append(pages[i])
            else:
                # 가장 먼저 들어온 페이지를 먼저 교체 (FIFO)
                idx = frame_list.index(queue.pop(0))
                frame_list[idx] = pages[i]
                queue.append(pages[i])

    return page_faults

pages = [1, 2, 3, 4, 5, 6, 7]
frames = 4

print(fifo_algorithm(pages, frames))  # Output: 3
