from src.make_amount_str import make_amount_str


def test_make_amount_str():
    assert make_amount_str() == ''
    assert make_amount_str({}) == ''
    assert make_amount_str(['ss', 5]) == ''
    assert make_amount_str({'as': 2, 'currency': {}}) == ''
    assert make_amount_str({'amount': 2, 'curre': {}}) == ''
