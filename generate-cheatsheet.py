from pathlib import Path
import utils

out_file = Path('index.html')

prefix = """\
<!DOCTYPE html>
<html lang="en">
<head>
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
  }
  </style>
</head>
<body>
  <h1>Kangxi Radicals 中文部首</h1>
  <table>
    <thead>
      <th>Radical</th>
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
  for char, meaning in utils.get_cards():
    yield f"""<tr>
      <td class="char">{char}</td>
      <td>{meaning}</td>
    </tr>"""

with out_file.open('w') as fp:
  fp.write(prefix)
  for row in get_rows():
    fp.write(row + '\n')
  fp.write(suffix)
