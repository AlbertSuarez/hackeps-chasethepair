def solve(set_a, set_b, to_chase):
    # Merge two sets
    list_merged = set_a + set_b
    # Get closest number and remove it
    closest_number = min(list_merged, key=lambda x: abs(x - to_chase))
    del list_merged[list_merged.index(closest_number)]
    # Get second closest number
    second_closest_number = min(list_merged, key=lambda x: abs(x - to_chase))
    # Return
    return second_closest_number, closest_number
