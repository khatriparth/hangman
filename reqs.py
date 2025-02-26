from rich.console import Console
from rich.text import Text

console = Console()

def strikethrough(text):
    return Text(text, style="strike")

import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
