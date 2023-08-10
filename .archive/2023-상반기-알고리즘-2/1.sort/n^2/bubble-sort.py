import random


def bubble(array):
    # 맥스값 밀어넣기
    for max_scope in range(len(array) - 1, -1, -1):
        for current_node in range(max_scope):
            next_node = current_node + 1

            current_value = array[current_node]
            next_value = array[next_node]

            if current_value > next_value:
                array[current_node], array[next_node] = array[next_node], array[current_node]
    return array


array = [random.randint(0, 10) for _ in range(20)]
print(array)
print(bubble(array))
