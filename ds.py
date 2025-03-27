import heapq


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


class BestN:
    def __init__(self, n):
        self.n = n
        self.data = list()
        heapq.heapify(self.data)

    def add(self, val):
        heapq.heappush(self.data, val)
        if len(self.data) > self.n:
            heapq.heappop(self.data)

    def __repr__(self):
        return "\n".join([str(_) for _ in sorted(self.data, reverse=True)])
    
    def full(self):
        return len(self.data) == self.n


class Matcher:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.all_letters = set()
        for side in self.puzzle:
            self.all_letters.update(list(side))
        print(self.all_letters)

    def spellable(self, w) -> set | None:
        walks = [(idx, 0) for (idx, side) in enumerate(self.puzzle) if w[0] in side]
        while walks:
            (node_idx, char_idx) = walks.pop(0)
            if char_idx + 1 == len(w):
                return set(w) & self.all_letters
            for next_node in range(4):
                if next_node == node_idx: 
                    continue
                if w[1 + char_idx] in self.puzzle[next_node]:
                    walks.append((next_node, 1 + char_idx))
        return None


if __name__ == '__main__':
    matcher = Matcher(['WFI', 'NCY', 'GTA', 'HEM'])
    matcher.spellable('HIGHWAYC')
