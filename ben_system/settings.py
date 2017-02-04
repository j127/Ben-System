"""These settings can be extended to customize the system."""


systems = {}

systems['ben_pridmore'] = {
    # TODO: double-check accuracy
    'first_letters': ['s', 't', 'n', 'm', 'r', 'l', 'g/j', 'k', 'f/th', 'b',
                      'p', 'h', 'sk/sn/sm', 'st/sp', 'sh/sl/sw', 'd', None,
                      None, None],
    'middle_letters': ['oo', 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O',
                       None, None, None, None, None, None, 'ow', 'or', 'ar'],
    'final_letters': ['s', 't', 'n', 'm', 'r', 'l', 'g', 'k', 'f/th', 'b',
                      None, None, None, None, None, None, 'j/sh/ch', 'p', 'd'],
    'decimals': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', None, None,
                 None, None, None, None, None, None, None],
    'binaries': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', None, None, None],
    'card_suits': ['ss', 'cd', 'ch', 'cs', 'dc', 'dh', 'ds', 'cc', 'hc', 'hd',
                   'hs', 'hh', 'sc', 'sd', 'sh', 'dd', None, None, None],
    'card_values': ['10', 'A', '2', '3', '4', '5', '6', '7', '8', '9', None,
                    None, None, None, None, None, 'J', 'Q', 'K'],
}

systems['josh_cohen'] = {
    'first_letters': ['s/z', 't', 'n', 'm', 'r', 'l', 'b', 'k', 'f/v', 'p',
                      'g/y', 'h', 'sk/sn/sm', 'st/sp', 'sh/sl/sw/j', 'd', None,
                      None, None],
    'middle_letters': ['o', 'i', 'u', 'aa', 'a', 'ai', 'ih', 'e', 'ei', 'u',
                       None, None, None, None, None, None, 'ow', 'or', 'ar'],
    'final_letters': ['s/z', 't', 'n', 'm', 'r/th', 'l', 'b', 'k', 'f/v', 'p',
                      None, None, None, None, None, None, 'j/sh/ch', 'g/y',
                      'd'],
    'decimals': ['0',  '1', '2', '3', '4', '5', '6', '7', '8', '9', None, None,
                 None, None, None, None, None, None, None],
    'binaries': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', None, None, None],
    'card_suits': ['s/s', 'c/d', 'c/h', 'c/s', 'd/c', 'd/h', 'd/s', 'c/c',
                   'h/c', 'h/d', 'h/s', 'h/h', 's/c', 's/d', 's/h', 'd/d',
                   None, None, None],
    'card_values': ['10', 'A', '2', '3', '4', '5', '6', '7', '8', '9', None,
                    None, None, None, None, None, 'J', 'Q', 'K'],
}
