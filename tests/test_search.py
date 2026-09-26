def test_search_import():
    from app.search import search

    assert callable(search)