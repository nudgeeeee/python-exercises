def count_elements(lst):
    counts = {}
    for element in lst:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    return counts