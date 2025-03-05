cards:
  python generate-anki-cards.py

sheet:
  python generate-cheatsheet.py

install:
  pip install ghp-import

publish:
  mkdir -p _build
  cp index.html radical-anki-cards.txt _build
  ghp-import --no-jekyll --push --no-history _build
