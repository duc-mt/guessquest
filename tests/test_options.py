import pytest
from unittest.mock import patch
import options

@patch('options.game')
def test_easy(mock_game, capsys):
    options.easy()
    mock_game.assert_called_once_with(10, 6)
    captured = capsys.readouterr()
    assert "guess a number between 1 and 10" in captured.out

@patch('options.game')
def test_medium(mock_game, capsys):
    options.medium()
    mock_game.assert_called_once_with(20, 4)
    captured = capsys.readouterr()
    assert "guess a number between 1 and 20" in captured.out

@patch('options.game')
def test_hard(mock_game, capsys):
    options.hard()
    mock_game.assert_called_once_with(50, 3)
    captured = capsys.readouterr()
    assert "guess a number between 1 and 50" in captured.out

@patch('builtins.input', side_effect=['y'])
@patch('welcome.start_game')
def test_try_again_yes(mock_start_game, mock_input):
    options.try_again()
    mock_start_game.assert_called_once()

@patch('builtins.input', side_effect=['n'])
@patch('builtins.print')
def test_try_again_no(mock_print, mock_input):
    options.try_again()
    mock_print.assert_any_call('Thanks for playing the game!')

@patch('builtins.input', side_effect=['invalid', 'n'])
@patch('builtins.print')
def test_try_again_invalid_then_no(mock_print, mock_input):
    options.try_again()
    mock_print.assert_any_call('INVALID VALUE!')
    mock_print.assert_any_call('Thanks for playing the game!')
