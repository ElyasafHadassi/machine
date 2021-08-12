
def main(mushrooms):
    odors = []
    other = []
    i = 0
    for mushroom in mushrooms:
        j = 0
        removed = []
        for c in mushroom:
            if j == 5:
                odors.append(c)
            else:
                removed.append(c)
            j += 1
        other.append(removed)
        i += 1
    return other, odors
