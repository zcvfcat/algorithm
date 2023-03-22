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

words = ['hi','hello','world']

trie = make_trie(words)

print(trie)

