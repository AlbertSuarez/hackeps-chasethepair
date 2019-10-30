import time

from src import chase_the_pair


if __name__ == '__main__':
    set_a = [1, 23, 45, 66, 84, 113, 145, 178, 205, 210, 221, 250, 264, 300]
    set_b = [5, 31, 40, 52, 73, 103, 126, 162, 195, 214, 225, 241, 256, 267]
    to_chase = 231
    start_time = time.time()
    result = chase_the_pair.solve(set_a, set_b, to_chase)
    end_time = time.time()
    expected_result = 221, 225
    assert result == expected_result
    print(f'Yay! The result is {result} in {end_time - start_time:0.10f}s')
