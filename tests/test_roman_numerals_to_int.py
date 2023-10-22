from main import roman_numerals_to_int

import pytest


@pytest.mark.parametrize("a, expected_result", [('VI', 6),
                                                ('III', 3),
                                                ('XIV', 14),
                                                ('IIII', None),
                                                ('XIIV', None),
                                                ('XXI', 21),
                                                ('XXIIII', None),
                                                ('iv', None),
                                                (5, None)])
def test_prime_numbers(a, expected_result):
    assert roman_numerals_to_int(a) == expected_result