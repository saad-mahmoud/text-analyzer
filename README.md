# Text Analyzer

A simple Python text analysis tool that processes text files and provides word frequency analysis.

## Features

- Text processing:
  - Converts text to lowercase
  - Splits text into words
- Word analysis:
  - Counts total number of words
  - Counts unique words
  - Shows word frequencies
- Output:
  - Displays analysis results in console
  - Saves results to JSON file

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd text-analyzer
```

## Usage

1. Run the analyzer:
```bash
python analyzer.py
```

2. Follow the menu options:
   - Option 1: Analyze a text file
   - Option 2: Exit the program

3. View the results:
   - Console output shows:
     - Total word count
     - Number of unique words
     - Word frequencies
   - Results are saved in `results.json`

## Example Output

```
Total words: 10
Unique words: 5

Word frequencies:
hello: 3
world: 2
python: 2
text: 2
analyzer: 1

Results saved to results.json
```

## Project Structure

- `analyzer.py`: Main application code
- `results.json`: Analysis output file

## License

This project is licensed under the MIT License - see the LICENSE file for details. 