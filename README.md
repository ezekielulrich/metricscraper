# Citation Metrics Scraper

This Python program allows you to retrieve and compile the h-index of researchers from given universities. 

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

You can install the required libraries using `pip`:

```bash
pip install pandas scholarly
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

The program will search Google Scholar for authors from each university whose interests are associated with manufacturing and retrieve their corresponding h-index and citation count. These results are compiled into a .csv file and can be visualized as a box plot by running 
```bash
python graph.py
```

## Example

```bash
python main.py
```

Output:

```
Running...
...
{'Author': 'A. John Hart', 'Affiliation': 'MIT', 'Citations': 23499, 'H-index': 72}
Searching for information on Aaron Stebner
{'Author': 'Aaron Stebner', 'Affiliation': 'Georgia Tech', 'Citations': 2520, 'H-index': 26}
Searching for information on Adrian Lew
{'Author': 'Adrian Lew', 'Affiliation': 'Stanford', 'Citations': 3330, 'H-index': 28}
...
Saved to .csv file
```

## License

[MIT License](LICENSE)
