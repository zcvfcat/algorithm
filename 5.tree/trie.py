def make_trie(words):
    trie = {}
    for word in words:
        curr_dict = trie
        for letter in word:
            if letter not in curr_dict:
                curr_dict[letter] = {}
            curr_dict = curr_dict[letter]
        curr_dict["*"] = True
    return trie


words = ["hi", "hello", "world"]
trie = make_trie(words)
print(trie)

# {'h': {'i': {'*': True}, 'e': {'l': {'l': {'o': {'*': True}}}}, 'w': {'o': {'r': {'l': {'d': {'*': True}}}}}
