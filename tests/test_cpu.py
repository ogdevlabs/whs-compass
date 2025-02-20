import pytest

from src.cpu import Cpu


@pytest.fixture()
def cpu():
    return Cpu()

def test_get_choice_valid(cpu):
    assert cpu.get_choice() in ["rock","paper","scissors"]