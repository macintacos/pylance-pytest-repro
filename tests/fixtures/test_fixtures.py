import pytest


@pytest.fixture(name="some_fixture")
def mock_fixture(mocker):
    mocker.patch("app.return_data", return_value=["fixture data"])
