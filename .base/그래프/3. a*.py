# G cost = distance from staring node
# H cost = distance from end node  -> heuristic(한국어로 체험)
# F cost = G cost + H cost
# start ---- mid --------- end
# start ---- mid = G
#            mid --------- end = H
# start ------------------ end = F
maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

vertical_weight, horizon_weight, diagonal_weight = 10, 10, 14  # 피타고라스 정리
step = [
    (1, 0, vertical_weight), (-1, 0, vertical_weight),
    (0, 1, horizon_weight), (0, -1, horizon_weight),
    (1, 1, diagonal_weight), (-1, -1, diagonal_weight),
    (1, -1, diagonal_weight), (1, -1, diagonal_weight),
]

start = (0, 0)
end = (7, 6)