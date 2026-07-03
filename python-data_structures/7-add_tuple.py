#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Pad both tuples with 0s and slice to ensure they have exactly 2 elements
    a = (tuple_a + (0, 0))[:2]
    b = (tuple_b + (0, 0))[:2]
    
    # Return a new tuple with the sum of elements
    return (a[0] + b[0], a[1] + b[1])
