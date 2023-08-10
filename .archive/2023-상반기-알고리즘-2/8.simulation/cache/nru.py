def nru_algorithm(pages, frames):
    # 프레임 초기화
    frame_list = [-1] * frames
    # 참조 비트 초기화
    ref_bits = [0] * frames

    page_faults = 0
    len_pages = len(pages)
    for i in range(len_pages):
        if pages[i] in frame_list:
            # 해당 페이지가 이미 캐시에 있으면 참조 비트를 1로 변경
            ref_bits[frame_list.index(pages[i])] = 1
        else:
            # 페이지 부재 발생
            page_faults += 1

            for j in range(frames):
                if frame_list[j] == -1 or ref_bits[j] == 0:
                    # 빈 프레임이나 참조되지 않은 프레임에 페이지 삽입
                    frame_list[j] = pages[i]
                    ref_bits[j] = 1
                    break
                else:
                    # 참조된 프레임의 참조 비트를 0으로 재설정
                    ref_bits[j] = 0

    return page_faults

pages = [1, 2, 3, 4, 5, 1, 6, 7, 8, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
frames = 4

print(nru_algorithm(pages, frames))