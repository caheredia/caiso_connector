from sql_app.crud import get_lmps, get_row_count


def test_lmps(get_db):
    """
    Test lmp crud function
    """
    lmps = get_lmps(db=get_db)
    assert isinstance(lmps, list)


def test_row_count(get_db):
    """
    Test row count
    """
    rows = get_row_count(db=get_db)
    assert isinstance(rows, int)
    assert rows < 100
