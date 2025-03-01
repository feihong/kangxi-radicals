from pathlib import Path
import utils

input_file = Path('radicals.txt')
output_file = Path('radical-anki-cards.txt')

with output_file.open('w') as fp:
    fp.write("""#separator:tab
#html:true
#notetype column: 1
#tags column:2
""")
    for _number, char, _strokes, meaning in utils.get_cards(only_important=True):
        fp.write(f'cloze\tradical\t<span style="font-size: 40px">{{{{c1::{char}}}}}</span> is the radical for {{{{c2::{meaning}}}}}\t\t\n')
