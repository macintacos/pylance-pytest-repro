import app


def test_pylance_with_fixtures(some_fixture):
    # Note that this is NOT "some data", and passes, but Pylance claims "some_fixture" is not accessed
    expected = ["fixture data"]
    actual = app.return_data()
    assert expected == actual
