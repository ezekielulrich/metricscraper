# Citation Metrics Scraper

This Python program allows you to retrieve the h-index of researchers from Google Scholar using a list of names.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [License](#license)

## Requirements

- Python 3.x
- `pandas` library
- `scholarly` library
- `re` library

You can install the required libraries using `pip`:

```bash
pip install pandas scholarly re
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ezekielulrich/metricscraper.git
```

2. Navigate to the project directory:

```bash
cd metricscraper
```

## Usage

1. Run the program:

```bash
python main.py
```

The program will search Google Scholar for authors from each university whose interests are associated with manufacturing and retrieve their corresponding h-index, university, and citation count.

## Example

```bash
python main.py
```

Output:

```
{'Author': 'A. John Hart', 'Affiliation': 'MIT', 'Citations': 23499, 'H-index': 72}
Searching for information on Aaron Stebner
{'Author': 'Aaron Stebner', 'Affiliation': 'Georgia Tech', 'Citations': 2520, 'H-index': 26}
Searching for information on Adrian Lew
{'Author': 'Adrian Lew', 'Affiliation': 'Stanford', 'Citations': 3330, 'H-index': 28}
...
```

## License

[MIT License](LICENSE)
