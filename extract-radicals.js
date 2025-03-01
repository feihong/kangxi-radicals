// Script to extract Kangxi radicals from table in https://en.wikipedia.org/wiki/Kangxi_radicals#Table
{
  const table = document.querySelectorAll('table.wikitable')[1];
  const rows = table.querySelectorAll('tr')
  const lines = [...rows].map(row => [...row.children].slice(0,4).map(n => n.textContent.trim()).join('; '))
  console.log(lines.join('\n'))
}
