from src.make_bill_str import make_bill_str


def test_make_bill_str():
    assert make_bill_str() == ''
    assert make_bill_str({}) == ''
    assert make_bill_str({'aaa'}) == ''
