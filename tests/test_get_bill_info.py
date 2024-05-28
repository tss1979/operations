from src.get_bill_info import get_bill_info


def test_get_bill_info():
    assert get_bill_info('') == ''
    assert get_bill_info() == ''
    assert get_bill_info('Mastercard ') == ''
    assert get_bill_info('Mastercard  293838 399393') == ''
    assert get_bill_info('Mastercard  38399393') == ''
    assert get_bill_info('Mastercard  3839939300000000000') == ''
    assert get_bill_info("Maestro 1596837868705199") == ('Maestro', '1596 83** **** 5199')
    assert get_bill_info("Счет 64686473678894779589") == ('Счет', '****************9589')
    assert get_bill_info("Счет 6468647367889477958") == ''
