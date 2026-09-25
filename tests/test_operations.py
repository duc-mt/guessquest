import pytest
from unittest.mock import patch, call
from operations import guessing, validate_input

def test_validate_input_valid_initially():
    # guess is already valid
    assert validate_input(3, 5) == 3

@patch('builtins.input', side_effect=['6', '0', '4'])
@patch('builtins.print')
def test_validate_input_invalid_then_valid(mock_print, mock_input):
    # initial guess is 8, range is 5. So it asks again.
    # inputs: '6' (invalid), '0' (invalid), '4' (valid)
    assert validate_input(8, 5) == 4
    assert mock_input.call_count == 3
    assert mock_print.call_count == 3

@patch('builtins.input', side_effect=['invalid', '3'])
@patch('builtins.print')
def test_validate_input_value_error(mock_print, mock_input):
    # Tests exception handling for non-integer inputs
    assert validate_input(8, 5) == 3
    assert mock_input.call_count == 2

@patch('random.randint', return_value=5)
@patch('builtins.input', side_effect=['5'])
@patch('builtins.print')
def test_guessing_correct_first_try(mock_print, mock_input, mock_randint):
    guessing(10, 3)
    mock_print.assert_any_call('You nailed it! And it only took you', 1, 'attempts.')

@patch('random.randint', return_value=5)
@patch('builtins.input', side_effect=['2', '5'])
@patch('builtins.print')
def test_guessing_too_low_then_correct(mock_print, mock_input, mock_randint):
    guessing(10, 3)
    mock_print.assert_any_call('It should be higher than 2.')
    mock_print.assert_any_call('You nailed it! And it only took you', 2, 'attempts.')

@patch('random.randint', return_value=5)
@patch('builtins.input', side_effect=['8', '5'])
@patch('builtins.print')
def test_guessing_too_high_then_correct(mock_print, mock_input, mock_randint):
    guessing(10, 3)
    mock_print.assert_any_call('It should be lower than 8.')
    mock_print.assert_any_call('You nailed it! And it only took you', 2, 'attempts.')

@patch('random.randint', return_value=5)
@patch('builtins.input', side_effect=['1', '2', '3'])
@patch('builtins.print')
def test_guessing_game_over(mock_print, mock_input, mock_randint):
    guessing(10, 3)
    mock_print.assert_any_call('GAME OVER! It took you more than', 3, 'attempts.', 'The correct number is', '5.')

@patch('random.randint', return_value=5)
@patch('builtins.input', side_effect=['1', '2', '5'])
@patch('builtins.print')
def test_guessing_correct_last_try(mock_print, mock_input, mock_randint):
    guessing(10, 3)
    mock_print.assert_any_call('You nailed it! However, it took you all the', 3, 'attempts.')

@patch('random.randint', return_value=5)
@patch('builtins.input', side_effect=['notanumber', '5'])
@patch('builtins.print')
def test_guessing_value_error_first_guess(mock_print, mock_input, mock_randint):
    guessing(10, 3)
    # The first guess is invalid (0 due to exception), so it asks again via validate_input.
    mock_print.assert_any_call('You nailed it! And it only took you', 1, 'attempts.')
