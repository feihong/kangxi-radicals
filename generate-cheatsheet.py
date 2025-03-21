import re
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
    width: 100%;
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
  .char-border {
    border: 1px dashed gray;
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
  <div>Search: <input autocapitalize="off" oninput="filter(this.value)"></div>
  <table>
    <thead>
      <tr>
        <th>Radical</th>
        <th># Strokes</th>
        <th>Meaning</th>
      </tr>
    </thead>
    <tbody>
"""

suffix = """\
</tbody>
<script>
function filter(text) {
  text = text.trim().toLowerCase()
  if (text === '') {
    setRowVisibility(_ => true)
  } else {
    setRowVisibility(meaning => meaning.includes(text))
  }
}
function setRowVisibility(pred) {
  const rows = [...document.querySelectorAll('tr')].slice(1)
  for (const row of rows) {
    const meaning = row.querySelector('.meaning').textContent
    row.style.display = pred(meaning) ? '' : 'none'
  }
}
</script>
</body>
</html>
"""

def get_rows():
  for numbers, char, strokes, meaning in utils.get_cards(only_important=False):
    if m := re.match(r'\|(.*)\|', char):
      char = m.group(1)
      border_class = 'char-border'
    else:
      border_class = ''

    numbers_links = ', '.join(f'<a target="_blank" href="https://en.wikipedia.org/wiki/Radical_{n}">{n}</a>' for n in numbers)
    yield f"""<tr>
      <td class="char">
        <div class="number">{numbers_links}</div>
        <span class="{border_class}">{char}</span>
      </td>
      <td>{strokes}</td>
      <td class="meaning">{meaning}</td>
    </tr>"""

with out_file.open('w') as fp:
  fp.write(prefix)
  for row in get_rows():
    fp.write(row + '\n')
  fp.write(suffix)
