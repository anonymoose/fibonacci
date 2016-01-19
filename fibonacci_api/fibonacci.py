import copy

"""
constant: PRE_GEN_FIB_SEQUENCE

notes:    Fibonacci numbers we know about.

TODO:     KB: [2016-01-18]: We could pregenerate a very large list of these if we wanted, or if performance became a problem.
"""
PRE_GEN_FIB_SEQUENCE = [0, 1]

"""
constant: PRE_GEN_FIB_SEQUENCE_SIZE

notes:    Length of the pre generated Fibonacci numbers.  Don't want to count it every time, so count it once.
"""
PRE_GEN_FIB_SEQUENCE_SIZE = len(PRE_GEN_FIB_SEQUENCE)



def fibonacci_calc(count):
    """
    function:  fibonacci_calc

    params:    count - number of elements in the return value.  Assumed to be a long.

    pre-conditions:  count is assumed to be a positive int or long.

    returns:   list of integers, of length == count, containing valid Fibonacci numbers.

    notes:
    This algorithm is an iterative solution to calculating Fibonacci numbers.  Start with known numbers 0 & 1.  Add them up
    and store in an array until you reach "count" iterations.

    This solution is preferable to a recursive solution in that, while we are collecting results as we go, the size of the
    stack frames we would collect as we processed the algorithm should be less than simply storing an array of integers.
    This will pay off for very large values of 'count'.

    Another alternative not implemented here is to use a generator to yield the results to an array.   While that is arguably
    a more idiomatic use of the python language, the performance should be the same (non-recursive), and this solution has the
    advantage of being immediately understandable in by only one function.
    """
    assert isinstance(count, (int, long))
    assert count >= 0

    sequence = copy.copy(PRE_GEN_FIB_SEQUENCE)
    if count > PRE_GEN_FIB_SEQUENCE_SIZE:
        for f in range(2, count):
            parent = sequence[-1]
            grandparent = sequence[-2]
            sequence.append(grandparent + parent)
    return sequence[:count]
