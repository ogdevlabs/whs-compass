import pytest

from src.game import Game


@pytest.fixture
def game():
    return Game()

