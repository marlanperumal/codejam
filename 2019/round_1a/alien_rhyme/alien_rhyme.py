from collections import defaultdict

def alien_rhyme(words):
    suffixes = defaultdict(set)
    for word in words:
        for i in range(len(word)):
            suffixes[word[-i:]].add(word)
    couplets = []
    sorted_suffixes = sorted(suffixes, key=lambda x: len(x), reverse=True)
    for suffix in sorted_suffixes:
        rhyming_set = suffixes[suffix]
        if len(rhyming_set) < 2:
            del suffixes[suffix]
            continue
        c1 = rhyming_set.pop()
        c2 = rhyming_set.pop()
        couplets.append([c1, c2])
        for i in range(1, len(suffix)):
            suffixes[suffix[-i:]].remove(c1)
            suffixes[suffix[-i:]].remove(c2)
        del suffixes[suffix]

    return len(couplets) * 2

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        words = [input() for i in range(N)]
        result = alien_rhyme(words)
        print("Case #{}: {}".format(t, result))