from pathlib import Path
import utils

input_file = Path('radicals.txt')
output_file = Path('radical-anki-cards.txt')

with output_file.open('w') as fp:
    fp.write("""#separator:tab
#html:true
#tags column:3
""")
    for char, meaning in utils.get_cards():
        fp.write(f'<span style="font-size: 32px">{{{{c1::{char}}}}}</span> is the radical for {{{{c2::{meaning}}}}}\t\tradical\n')
