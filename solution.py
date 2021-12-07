import numpy as np
from scipy.ndimage.filters import uniform_filter1d

def read_data():
    with open('input.txt', 'r') as f:
        data = f.readlines()
    return(np.array([int(d.strip()) for d in data]))

data = read_data()

def part1():
    return(np.sum((data[1:]-data[:-1])>0))

def part2():
    size = 3
    win_sum = uniform_filter1d(data*size, size = size, cval=0.0, origin=-(size//2), mode='constant')[:-(size-1)]
    return(np.sum((win_sum[1:]-win_sum[:-1])>0))

print(f'Part 1: {part1()}')
print(f'Part 1: {part2()}')