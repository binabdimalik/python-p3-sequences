#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    
    elif length == 1:
        print([0])
        return
    
    seq = [0, 1]

    while len(seq) < length:
        next_val = seq[-1]  + seq[-2]
        seq.append(next_val)

    print(seq)