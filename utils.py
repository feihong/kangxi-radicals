from pathlib import Path

input_file = Path('radicals.txt')

def get_cards(only_important):
    for line in input_file.read_text().splitlines():
        line = line.strip()
        if line == '' or (only_important and line.startswith('#')):
            continue

        if line.startswith('#'):
            line = line[1:]

        numbers, char, strokes, meaning = line.split('; ')
        yield numbers.split(', '), char, strokes, meaning
