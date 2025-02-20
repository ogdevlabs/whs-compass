import pytest
from src.player import Player
from unittest.mock import patch

@pytest.fixture()
def player():
    return Player()

@patch('builtins.input', return_value="rock")
def test_get_choice_valid(mock_input, player):
    assert player.get_choice() == "rock"

@patch('builtins.input', side_effect=["invalid", "scissors"])
def test_get_choice_invalid_then_valid(mock_input, player):
    assert player.get_choice() == "scissors"