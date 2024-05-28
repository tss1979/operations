from src.get_last_five import get_last_five

def test_get_last_five():
    assert get_last_five() == []
    assert len(get_last_five([1, 2, 3, 4, 5, 6])) == 5
    assert len(get_last_five([1, 2, 3])) == 3
    assert get_last_five([]) == []

