# ipynb Text Extract

ipynb Text Extract is a simple script to extract all text cells
(`"cell_type": "markdown"`) from a notebook file (ipynb). The resulting text is
stored in a .md Markdown file.

## Requirements

This script does not have any dependencies outside of the Python standard
library.

It requires at least Python 3.6.

## Usage

```sh
python ipynb-text-extract.py your_notebook.ipynb
```

The result will be stored in `your_notebook.md`.

To also extract single line comments from code cells (`"cell_type": "code"`),
add the optional argument `-c`:

```sh
python ipynb-text-extract.py your_notebook.ipynb -c
```

To see a summary of these instructions, use `-h`:

```sh
python ipynb-text-extract.py -h
```
