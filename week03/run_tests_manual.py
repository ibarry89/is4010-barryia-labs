from lab03 import generate_mad_lib, guessing_game
from unittest.mock import patch


def run():
    print('Testing generate_mad_lib...')
    s = generate_mad_lib('silly', 'cat', 'jumped')
    assert isinstance(s, str)
    assert 'silly' in s
    assert 'cat' in s
    assert 'jumped' in s
    print('-> generate_mad_lib OK')

    print('Testing guessing_game (multi-guess)...')
    with patch('lab03.random.randint', return_value=50):
        with patch('builtins.input', side_effect=['75', '25', '50']):
            with patch('builtins.print') as mock_print:
                guessing_game()
                assert mock_print.called
                printed = ' '.join(str(c) for c in mock_print.call_args_list).lower()
                assert ('too high' in printed) or ('too low' in printed) or ('congratulations' in printed)
    print('-> guessing_game multi-guess OK')

    print('Testing guessing_game (immediate correct)...')
    with patch('lab03.random.randint', return_value=42):
        with patch('builtins.input', side_effect=['42']):
            with patch('builtins.print') as mock_print:
                guessing_game()
                assert mock_print.called
    print('-> guessing_game immediate correct OK')

    print('\nALL MANUAL TESTS PASSED')


if __name__ == '__main__':
    run()
