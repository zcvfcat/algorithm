import heapq
from collections import defaultdict


def huffman_encoding(data):
    # Step 1: Calculate frequency of each character
    freq = defaultdict(int)
    for c in data:
        freq[c] += 1

    # Step 2: Build Huffman tree
    heap = [[f, [c, ""]] for c, f in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # Step 3: Build encoding dictionary
    encoding = dict(heapq.heappop(heap)[1:])

    # Step 4: Encode the input data
    encoded_data = ""
    for c in data:
        encoded_data += encoding[c]

    return encoded_data, encoding


def huffman_decoding(encoded_data, encoding):
    # Step 1: Build decoding dictionary
    decoding = {v: k for k, v in encoding.items()}

    # Step 2: Decode the input data
    decoded_data = ""
    code = ""
    for bit in encoded_data:
        code += bit
        if code in decoding:
            decoded_data += decoding[code]
            code = ""

    return decoded_data


data = "ABBCBACBACDBCBADCCB"
encoded_data, encoding = huffman_encoding(data)
decoded_data = huffman_decoding(encoded_data, encoding)

print(f"Original data: {data}")
print(f"Encoded data: {encoded_data}")
print(f"Decoded data: {decoded_data}")
