import time
import argparse

from src import chase_the_pair, EXAMPLE_SET


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--set_size', type=int)
    return parser.parse_args()


def _main():
    if not args.set_size:
        print('Not size specified. Getting default sets...')
        set_a = [1, 23, 45, 66, 84, 113, 145, 178, 205, 210, 221, 250, 264, 300]
        set_b = [5, 31, 40, 52, 73, 103, 126, 162, 195, 214, 225, 241, 256, 267]
        to_chase = 231
        expected_result = (221, 225)
    else:
        if args.set_size not in EXAMPLE_SET:
            print(f'set_size has not be one of the followings: {list(EXAMPLE_SET.keys())}')
            return
        print(f'Correct set size specified. Processing with size {args.set_size}...')
        set_a = EXAMPLE_SET[args.set_size]['set_a']
        set_b = EXAMPLE_SET[args.set_size]['set_b']
        to_chase = EXAMPLE_SET[args.set_size]['to_chase']
        expected_result = EXAMPLE_SET[args.set_size]['expected_result']

    start_time = time.time()
    result = chase_the_pair.solve(set_a, set_b, to_chase)
    end_time = time.time()
    assert result == expected_result
    print(f'Yay! The result is {result} in {end_time - start_time:0.10f}s')


if __name__ == '__main__':
    args = _parse_args()
    _main()
