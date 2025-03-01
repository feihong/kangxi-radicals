from pathlib import Path
import utils

out_file = Path('index.html')

prefix = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Kangxi Radicals 中文部首</title>
  <style>
  html {
    max-width: 70ch;
    padding: 3em 1em;
    margin: auto;
    line-height: 1.75;
    font-size: 1.25em;
  }
  table {
    border-collapse: collapse;
  }
  td {
    border: 1px solid gray;
    padding: 1em;
    text-align: center;
  }
  td.char {
    font-size: 3em;
    padding: 0;
    position: relative;
    font-family: monospace;
  }
  .number {
    font-size: 0.3em;
    color: gray;
    position: absolute;
    top: 0;
    left: 0;
    padding: 0 0.2em;
  }
  </style>
</head>
<body>
  <h1>Kangxi Radicals 中文部首</h1>
  <p><a href="radical-anki-cards.txt">Download Anki cards</a></p>
  <table>
    <thead>
      <th>Radical</th>
      <th># Strokes</th>
      <th>Meaning</th>
    </thead>
    <tbody>
"""

suffix = """\
</tbody>
</body>
</html>
"""

def get_rows():
  for numbers, char, strokes, meaning in utils.get_cards(only_important=False):
    numbers_links = ', '.join(f'<a target="_blank" href="https://en.wikipedia.org/wiki/Radical_{n}">{n}</a>' for n in numbers)
    yield f"""<tr>
      <td class="char">
        <div class="number">{numbers_links}</div>
        {char}
      </td>
      <td>{strokes}</td>
      <td>{meaning}</td>
    </tr>"""

with out_file.open('w') as fp:
  fp.write(prefix)
  for row in get_rows():
    fp.write(row + '\n')
  fp.write(suffix)
