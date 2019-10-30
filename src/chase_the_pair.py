def solve(set_a, set_b, to_chase):
    return min(set_a, key=lambda x: abs(x - to_chase)), min(set_b, key=lambda x: abs(x - to_chase))
