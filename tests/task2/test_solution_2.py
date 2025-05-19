import pytest

from task2.solution import get_beasts_count_by_char


@pytest.fixture
def mock_requests(mocker):
    mock_requests = mocker.patch("task2.solution.requests")
    mock_requests.get.return_value = mocker.MagicMock()
    return mock_requests


@pytest.fixture
def mock_bs4(mocker):
    mock_bs4 = mocker.patch("task2.solution.BeautifulSoup")
    mock_bs4_instance = mocker.MagicMock()
    mock_select = mocker.MagicMock()
    mock_select_2 = mocker.MagicMock()
    mock_select.select.return_value = [mock_select_2]
    mock_select.find.return_value = None
    mock_select_2.select.return_value = [{"title": "Носорог"}, {"title": "Змея"}]
    mock_bs4_instance.return_value = mock_select
    mock_bs4.side_effect = mock_bs4_instance
    return mock_bs4


def test_get_beasts_count_by_char(mock_requests, mock_bs4):
    assert get_beasts_count_by_char("13", "132") == {"Н": 1, "З": 1}
