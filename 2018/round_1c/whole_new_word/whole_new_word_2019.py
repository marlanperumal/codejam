def add_to_node(word, node):
    l = word[0]
    if l not in node:
        node[l] = {}
    if len(word) > 1:
        add_to_node(word[1:], node[l])


def parse_tree(node, level, L, letters, current_word, queue):
    for wi in letters[level]:
        if wi not in node:
            word = current_word + wi
            if L > level + 1:
                word += "".join([letter[0] for letter in letters[level + 1:]]) 
            return word
        elif L > level + 1:
            queue.append((node[wi], level + 1, L, letters, current_word + wi, queue))
    return None


def run(N, L, W):
    word_tree = {}
    for w in W:
        add_to_node(w, word_tree)
    letters = [list(set([w[l] for w in W])) for l in range(L)]
    queue = []
    queue.append((word_tree, 0, L, letters, "", queue))
    word = None
    while queue and not word:
        elem = queue.pop()
        word = parse_tree(*elem)
    result = "-" if word is None else word
    return result


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N, L = [int(i) for i in input().split()]
        W = [input() for n in range(N)]
        result = run(N, L, W)
        print("Case #{}: {}".format(t, result))
