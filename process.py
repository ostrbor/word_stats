'''Process words

Usage:
    process.py <filepath>

Options:
    -h --help     Show this screen.
'''
from typing import List, Dict
from collections import Counter, OrderedDict
import pprint

import docopt


def sort_statistics(stats: Dict[str, int]) -> Dict[str, int]:
    # send (value, key) to key parameter of sorted
    # to sort dict items first by value (desc), then by key (asc)
    key, value = 0, 1
    return OrderedDict(sorted(stats.items(), key=lambda t: (-t[value], t[key])))


def count_words(filepath: str) -> Dict[str, int]:
    counter = Counter()
    with open(filepath) as fd:
        for line in fd:
            c = Counter(line.split())
            counter.update(c)
    return counter


if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    filepath = args.get('<filepath>')
    stats = count_words(filepath)
    sorted_stats = sort_statistics(stats)
    pprint.pprint(sorted_stats)
