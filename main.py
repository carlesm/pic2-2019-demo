"""Brewery control.

Usage:
  main.py status <sensor> [--config=<cf>]
  main.py reseet <sensor> [--config=<cf>]
  main.py (-h | --help)
  main.py --version

Options:
-h --help    Shows this screen
--version    Shows program version

"""
from docopt import docopt


if __name__ == "__main__":
    arguments = docopt(__doc__,version="First version Brewery")
    print(arguments)