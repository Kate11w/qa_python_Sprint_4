import pytest

from main import BooksCollector

@pytest.fixture
def book():
    book = 'Дюна'

    return book
