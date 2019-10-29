def solve(set_a, set_b, to_chase):
    # Merge two sets
    list_merged = set_a + set_b
    # Append new item and sort
    list_merged.append(to_chase)
    list_merged.sort()
    # Get the lowest index of `to_chase`
    to_chase_index = list_merged.index(to_chase)
    # Count amount of `to_chase`
    to_chase_count = list_merged.count(to_chase)
    # Get neighbours
    if to_chase_count >= 3:
        return to_chase, to_chase
    elif to_chase_count == 2:
        if to_chase_index == 0:
            return to_chase, list_merged[to_chase_index + 2]
        else:
            return list_merged[to_chase_index - 1], to_chase
    else:
        if to_chase_index == 0:
            return list_merged[to_chase_index + 1], list_merged[to_chase_index + 2]
        elif to_chase_index == len(list_merged) - 1:
            return list_merged[to_chase_index - 2], list_merged[to_chase_index - 1]
        else:
            return list_merged[to_chase_index - 1], list_merged[to_chase_index + 1]
