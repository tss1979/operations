from src.get_date import get_date


def test_get_date():
    assert get_date('') == ''
    assert get_date([]) == ''
    assert get_date({}) == ''
    assert get_date([1, 2, 3]) == ''
    assert get_date() == ''
    assert get_date('sshsggs') == ''
    assert get_date("2019-08-26T10:50:58.29404") == '26.08.2019'
    assert get_date("2019-08-2629404") == ''
    assert get_date("2019-1-26T10:50:58.29404") == '26.01.2019'
