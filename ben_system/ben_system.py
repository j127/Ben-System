""" A generator for the Ben System.

It allows customization of the output through the settings dictionary.
"""
from jinja2 import Template
from settings import systems


def suit_letters_to_entities(card):
    """Take a card like 2C and return the HTML entites."""
    pass


def render_template(context):
    """Take a context dictionary and return the rendered template as
    a string.
    """
    with open('template.html', 'r') as f:
        template = f.read()

    t = Template(template)
    return t.render(context)


def write_to_file(data):
    print('About to write to file: {}'.format(data[:20]))
    with open('build/output.html', 'w') as f:
        f.write()


def main():
    system = systems['josh_cohen']
    print(system)

    rows = []

    for i in range(19):
        for j in range(19):
                for k in range(19):

# Construct the binary number as bins
                    if k < 8 and i < 16 and j < 8:
                        b1 = bin(system['binaries'][i])[2:].zfill(3)
                        b2 = bin(system['binaries'][j])[2:].zfill(3)
                        b3 = bin(system['binaries'][k])[2:].zfill(3)
                        bins = '{} {} {}'.format(str(b1), str(b2), str(b3))
                    else:
                        bins = None

                    # Construct the decimals as decs
                    if k < 10:
                        decs = '{}{}{}'.format(system['decimals'][i], system['decimals'][j], system['decimals'][k])

                    # Construct letters as lets
                    if k < 19:
                        lets = '{}/{}/{}'.format(system['first_letters'][i], system['first_letters'][j], system['first_letters'][k])
                    else:
                        lets = None

                    # Construct the cards as cards
# Get the correct suit pair
                    card_suits = system['suits'][i]
# Split suit pair in half
                    card_suit = card_suits.split()

                    # Put each suit in a string
                    card_suit_1 = card_suit[0]
                    card_suit_2 = card_suit[1]

                    if card_suit_1 == 's':
                        suit_code_1 = '<span style="color: black;">&spades;</span>';
                    elif card_suit_1 == 'h':
                        suit_code_1 = '<span style="color: red;">&hearts;</span>';
                    elif card_suit == 'd':
                        suit_code_1 = '<span style="color: red;">&diams;</span>';
                    elif card_suit_1 == 'c':
                        suit_code_1 == '<span style="color: black">&clubs;</span>';
                    
                    if card_suit_2 == 's':
                        suit_code_2 = '<span style="color: black;">&spades;</span>';
                    elif card_suit_2 == 'h':
                        suit_code_2 = '<span style="color: red;">&hearts;</span>';
                    elif card_suit_2 == 'd':
                        suit_code_2 = '<span style="color: red;">&diams;</span>';
                    elif card_suit_2 == 'c':
                        suit_code_2 == '<span style="color: black">&clubs;</span>';

                    card_1 = system['cards'][j] + suit_code_1
                    card_2 = system['cards'][k] + suit_code_2

                    card = '{} {}'.format(card_1, card_2)

# Check if anything should be removed
                    if len(decs) == 3:
                        dec_check = 1
                    else:
                        dec_check = 0

                    if len(bins) == 12:
                        bin_check = 1
                    else:
                        bin_check = 0

                    # Card check to make sure the there is something worth printing
                    # if system.cards[j] 


        # current_row = {
        #     decimal: '',
        #     binary: '',
        #     cards: '',
        #     images: '',
        # }

        # # Decimal
        # if system['first_letters'][i]:
        #     current_row.append(system['first_letters'][i])
        # else:
        #     current_row.append('')


        # # Reset
        # current_row = []

if __name__ == '__main__':
    main()
