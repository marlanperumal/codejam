def breadth_search(tree, visit, current_word, layer):
    for branch in tree:
        # print(branch)
        success, word = visit(tree[branch], current_word + [branch], layer)
        if success:
            return success, word
    for branch in tree:
        success, word = breadth_search(tree[branch], visit, current_word + [branch], layer+1)
        # print(success, word)
        if success:
            return success, word
    return False, ["-"]

T = int(input())
for t in range(1, T+1):
    N, L = [int(si) for si in input().split()]
    words = []
    for n in range(N):
        words.append(input())
    tiles = [[word[l] for word in words] for l in range(L)]
    tile_tree = {}

    for word in words:
        sub_tree = tile_tree
        for letter in word:
            if letter not in sub_tree:
                sub_tree[letter] = {}
            sub_tree = sub_tree[letter]
    # print(tiles)
    # print(tile_tree)

    def visit(tree, current_word, layer):
        # print(tree, current_word, layer)
        if layer == L-1:
            return False, current_word
        for tile in tiles[layer + 1]:
            if tile not in tree.keys():
                word = current_word + [tile]
                if layer+2 < L:
                    word = word + [tiles[l][0] for l in range(layer+2, L)]
                return True, word
        return False, current_word

    success, word = breadth_search(tile_tree, visit, [], 0)
    ans = "".join(word)
    print("Case #{}: {}".format(t, ans))



    # tiles = {l: {} for l in range(L)}
    # for word in words:
    #     for l in range(L):
    #         if word[l] in tiles[l]:
    #             tiles[l][word[l]] += 1
    #         else:
    #             tiles[l][word[l]] = 1
    # ans = "-"
    # potentials = list(tiles[L-1].keys())
    # for l in reversed(range(L-1)):
    #     new_potentials = []
    #     for tile in tiles[l]:
    #         new_potentials.extend([tile + potential for potential in potentials])
    #     potentials = new_potentials
    # for potential in potentials:
    #     if potential not in words:
    #         ans = potential
    #         break
    # print("Case #{}: {}".format(t, ans))
