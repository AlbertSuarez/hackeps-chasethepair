# Chase The Pair Challenge by HackEPS2019

[![HitCount](http://hits.dwyl.io/AlbertSuarez/hackeps-chasethepair.svg)](http://hits.dwyl.io/AlbertSuarez/hackeps-chasethepair)
[![GitHub stars](https://img.shields.io/github/stars/AlbertSuarez/hackeps-chasethepair.svg)](https://GitHub.com/AlbertSuarez/hackeps-chasethepair/stargazers/)
[![GitHub forks](https://img.shields.io/github/forks/AlbertSuarez/hackeps-chasethepair.svg)](https://GitHub.com/AlbertSuarez/hackeps-chasethepair/network/)
[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/AlbertSuarez/hackeps-chasethepair.svg)](https://github.com/AlbertSuarez/hackeps-chasethepair)
[![GitHub contributors](https://img.shields.io/github/contributors/AlbertSuarez/hackeps-chasethepair.svg)](https://GitHub.com/AlbertSuarez/hackeps-chasethepair/graphs/contributors/)
[![GitHub license](https://img.shields.io/github/license/AlbertSuarez/hackeps-chasethepair.svg)](https://github.com/AlbertSuarez/hackeps-chasethepair/blob/master/LICENSE)

👫 "Chase The Pair" challenge solution from HackEPS

## Problem

Given a number (number A) get the closest pair of numbers (number B and number C) from two sets consisting of random numbers. When there are two numbers from the same set that are at the same distance from the result you can return either.

Given two sets of numerical values (SetA and SetB)

```
SetA: [1,23,45,66,84,113,145,178,205,210,221,250,264,300]
SetB: [5,31,40,52,73,103,126,162,195,214,225,241,256,267]
```

Given a random numerical value (toChase) contained within the two sets (It does not have to exist within these)

```
toChase: 231
WHERE toChase >= min(SetA, SetB) && toChase <= max(SetA, SetB)
```

Find that pair of numerical values closest to toChase

```
Result: [221, 225]
```

- Sets A and B can be considered the same length.
- If two values within the same set are at the same distance from toChase, either is perfectly valid as a result.
- If you find the toChase value within the set, this is a perfectly valid result.
- The set generator that we offer in this same repository should be used: `resources/setsGenerator`
- The reading time of the file can be ignored from the total elapsed.
- Sort algorithms can be used to sort the data and take advantage of them to arrive at a more optimal solution [hint].
- Taking into account the previous points notified, all programming techniques (legal) are allowed if you get a better time with them.

## Description

Use Python Lambdas with each set and get the closest number of `to_chase` number given the set:

```python
return min(set_[a|b], key=lambda x: abs(x - to_chase))
```

## Information

- Group name: Albert Suarez
- Cost: O(n)
- Time expend: 0.0467770100s
- Sets size: 100,000

## Requirements

This project is using Python3.7. No external libraries needed.

## Recommendations

Usage of [virtualenv](https://realpython.com/blog/python/python-virtual-environments-a-primer/) is recommended for package library / runtime isolation.

## Usage

To run this script, please execute the following from the root directory:

1. Setup virtual environment

2. Run the script with the default values

  ```bash
  python3 -m src [--set_size INT]
  ```

## Authors

- [Albert Suàrez](https://github.com/AlbertSuarez)

## License

MIT © Albert Suarez
