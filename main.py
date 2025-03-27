from collections import defaultdict
from ds import BestN, Matcher
import time


def solve(puzzle: list[str], wordlist: list[str]):
    best = BestN(20)
    matcher = Matcher(puzzle)

    word_set = set()  # set of all words
    # start_end_map = defaultdict(list[str])  # a(start_letter, end_letter) -> [words which start & end with them]
    start_map = defaultdict(list[str])  # a(start_letter) -> [words which start them]
    word_matched_letters = dict()
    # char_frequency = defaultdict(int)

    for w in wordlist:
        w = w.upper()
        if len(w) <= 3:
            continue
        overlap = matcher.spellable(w)
        if overlap is None:
            continue

        word_matched_letters[w] = overlap
        word_set.add(w)
        start_map[(w[0])].append(w)
        # trie.insert(w)
        # start_end_map[(w[0], w[-1])].append(w)
        # for c in w:
        #     char_frequency[c] += 1

    for w, matches in word_matched_letters.items():
        if len(matches) == 12:
            best.add((-1, -sum([len(_) for _ in [w]]), [w]))
    if not best.full():
        for w1 in word_set:
            for w2 in start_map[w1[-1]]:
                if 12 == len(word_matched_letters[w1] | word_matched_letters[w2]):
                    best.add((-2, -sum([len(_) for _ in [w1, w2]]), [w1, w2]))
    if not best.full():
        for w1 in word_set:
            for w2 in start_map[w1[-1]]:
                for w3 in start_map[w2[-1]]:
                    if 12 == len(word_matched_letters[w1] | word_matched_letters[w2] | word_matched_letters[w3]):
                        best.add((-3, -sum([len(_) for _ in [w1, w2, w3]]), [w1, w2, w3]))
    if not best.full():
        for w1 in word_set:
            for w2 in start_map[w1[-1]]:
                for w3 in start_map[w2[-1]]:
                    for w4 in start_map[w3[-1]]:
                        if 12 == len(word_matched_letters[w1] | word_matched_letters[w2] | word_matched_letters[w3]
                                     | word_matched_letters[w4]):
                            best.add((-4, -sum([len(_) for _ in [w1, w2, w3, w4]]), [w1, w2, w3, w4]))

    print(best)


def run():
    with open('wordlist.txt', 'r') as f:
        words = [e.strip().replace('"', "") for e in f.readlines()]
    # solve(['BTI', 'ERK', 'SPC', 'LYO'], words)
    solve(['WFI', 'NCY', 'GTA', 'HEM'], words)


if __name__ == '__main__':
    _start = time.perf_counter()
    run()
    _end = time.perf_counter()
    print(f'Time taken: {(_end - _start):.6f} seconds')
