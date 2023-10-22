from main import prime_numbers
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(1, 17, [2, 3, 5, 7, 11, 13, 17]),
                                                   (66, 84, [67, 71, 73, 79, 83]),
                                                   (10, 5, []),
                                                   (24, 26, []),
                                                   ('1', 17, []),
                                                   (24, '38', []),
                                                   ('3', '67', []),
                                                   (-10, 3, []),
                                                   (3, -20, []),
                                                   (-100, -23, [])])
def test_prime_numbers(a, b, expected_result):
    assert prime_numbers(a, b) == expected_result
