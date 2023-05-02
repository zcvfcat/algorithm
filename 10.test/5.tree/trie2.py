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

def in_trie(trie, word):
    cur_dict = trie
    
    for letter in word:
        if letter not in cur_dict:
            return False
        cur_dict = cur_dict[letter]
    
    return '*' in cur_dict
