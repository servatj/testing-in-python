from two_sum import two_sum_linear, two_sum_quadratic

import pytest

def test_two_sum_linear():
    assert two_sum_linear([2, 1, 5, 3], 4) == [1, 3]

def test_two_sum_quadratic():
    assert two_sum_quadratic([2, 1, 5, 3], 4) == [1, 3]
