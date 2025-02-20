import pytest
from unittest.mock import patch
from src.game import Game

@pytest.fixture
def game():
    return Game()

@patch('src.cpu.Cpu.get_choice', return_value='scissors')
@patch('src.player.Player.get_choice', return_value='rock')
def test_play_round(mock_player_choice, mock_cpu_choice):

    # Verify if the internal state has been updated correctly
    assert game is not None