# Chunk a list into N-sized batches
def chunk_list(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

# Flatten a nested list up to 1 level deep
def flatten_one_level(nested):
    return [item for sublist in nested for item in (sublist if isinstance(sublist, list) else [sublist])]

# Safe dict get with default callable
def dict_get_with_callable(d, key, default):
    return d.get(key, default() if callable(default) else default)

# Frequency count using Counter
from collections import Counter

def freq_with_counter(lst):
    return Counter(lst)

# Frequency count manually
def freq_manual(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

print(chunk_list([1,2,3,4,5,6],2))
print(flatten_one_level([[1,2],[1],4,[2]]))
print(dict_get_with_callable({'x':1}, 'y', lambda: 42))
print(freq_with_counter(['a','b','a']))
print(freq_manual(['a','b','a']))
