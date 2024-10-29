from collections import defaultdict


class Block:
    i = 0
    def __init__(self, word, blocks):
        self.id = str(Block.i)
        Block.i += 1
        self.word = word
        self.lefts = {}
        self.rights = {}
        for id, block in blocks.items():
            if self.word[0] == block.word[-1]:
                self.lefts[id] = block
                block.rights[self.id] = self
            if self.word[-1] == block.word[0]:
                self.rights[id] = block
                block.lefts[self.id] = self
        self.valid = True
        self.letters = set()
        last_letter = ""
        for c in word:
            if c == last_letter:
                continue
            if c in self.letters:
                self.valid = False
                break
            last_letter = c
            self.letters.add(c)

        blocks[self.id] = self

        self.uniform = len(self.letters) == 1

    def num_lefts(self):
        return 9999 if len(self.lefts) == 0 else len(self.lefts)

    def num_rights(self):
        return 9999 if len(self.rights) == 0 else len(self.rights)

    def order_value(self):
        return (min(self.num_lefts(), self.num_rights()), 1 if self.uniform else 0)

    def left_order_value(self):
        return (self.num_rights(), 1 if self.uniform else 0)

    def right_order_value(self):
        return (self.num_lefts(), 1 if self.uniform else 0)

    def __repr__(self):
        return f"{self.id} <{self.word}> [{''.join(self.letters)}] l[{','.join(self.lefts)}] r[{','.join(self.rights)}] {self.valid}"


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    S = [s for s in input().split()]
    blocks = dict()
    result = None
    for s in S:
        block = Block(s, blocks)
        if not block.valid:
            result = "IMPOSSIBLE"
            break
    while len(blocks) > 1:
        block = min(blocks.values(), key=lambda x: x.order_value())
        if block.num_lefts() == 9999 and block.num_rights() == 9999:
            del blocks[block.id]
            left = list(blocks.values())[0]
            del blocks[left.id]
            new_block = Block(f"{left.word}{block.word}", blocks)
        elif block.num_lefts() < block.num_rights():
            left = max(block.lefts.values(), key=lambda x: x.left_order_value())
            del blocks[block.id]
            del blocks[left.id]
            for l1 in block.lefts():
                del l1.rights[block.id] 
            new_block = Block(f"{left.word}{block.word}", blocks)
        else:
            right = max(block.rights.values(), key=lambda x: x.right_order_value())
            del blocks[block.id]
            del blocks[right.id]
            new_block = Block(f"{block.word}{right.word}", blocks)
        print(new_block)
        if not new_block.valid:
            result = "IMPOSSIBLE"
            break

    if result != "IMPOSSIBLE":
        block = list(blocks.values())[0]
        result = block.word
    # while result != "IMPOSSIBLE"
    print(f"Case #{t}: {result}")

