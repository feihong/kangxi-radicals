from pathlib import Path

input_file = Path('radicals.txt')

def get_cards():
    for line in input_file.read_text().splitlines():
        line = line.strip()
        if line != '':
            yield line.split(' ', 1)
