import pytest
from unittest.mock import patch
import welcome

@patch('builtins.input', side_effect=['Alice', '1'])
@patch('options.easy')
@patch('options.try_again')
@patch('time.sleep')
def test_start_game_easy(mock_sleep, mock_try_again, mock_easy, mock_input, capsys):
    welcome.start_game()
    mock_easy.assert_called_once()
    mock_try_again.assert_called_once()
    captured = capsys.readouterr()
    assert "Hello, Welcome to Guessquest!" in captured.out
    assert "Okay, Alice. Let's Begin Guessquest!" in captured.out

@patch('builtins.input', side_effect=['Bob', '2'])
@patch('options.medium')
@patch('options.try_again')
@patch('time.sleep')
def test_start_game_medium(mock_sleep, mock_try_again, mock_medium, mock_input):
    welcome.start_game()
    mock_medium.assert_called_once()
    mock_try_again.assert_called_once()

@patch('builtins.input', side_effect=['Charlie', '3'])
@patch('options.hard')
@patch('options.try_again')
@patch('time.sleep')
def test_start_game_hard(mock_sleep, mock_try_again, mock_hard, mock_input):
    welcome.start_game()
    mock_hard.assert_called_once()
    mock_try_again.assert_called_once()

@patch('builtins.input', side_effect=['Dave', '4', 'Dave', '1'])
@patch('builtins.print')
@patch('options.easy')
@patch('options.try_again')
@patch('time.sleep')
def test_start_game_invalid(mock_sleep, mock_try_again, mock_easy, mock_print, mock_input):
    welcome.start_game()
    mock_print.assert_any_call('ERROR! Invalid value! Please try again.\n')
    # Because of recursion, it eventually calls easy
    mock_easy.assert_called_once()

@patch('builtins.input', side_effect=['Eve', 'not_an_int', 'Eve', '1'])
@patch('builtins.print')
@patch('options.easy')
@patch('options.try_again')
@patch('time.sleep')
def test_start_game_value_error(mock_sleep, mock_try_again, mock_easy, mock_print, mock_input):
    welcome.start_game()
    mock_print.assert_any_call('ERROR! Invalid value! Please try again.\n')
    mock_easy.assert_called_once()
