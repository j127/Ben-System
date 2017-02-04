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


if __name__ == '__main__':
    main()