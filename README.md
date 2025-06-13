# Text Analyzer

A Python-based text analysis tool that processes text files and provides word frequency analysis.

## Features

- Text processing:
  - Converts text to lowercase
  - Removes punctuation
  - Splits text into words
- Word analysis:
  - Counts total number of words
  - Counts unique words
  - Shows top 5 most frequent words
- Output:
  - Displays analysis results in console
  - Saves detailed results to JSON file

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd text-analyzer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your text file in the project directory (default: `file.txt`)

2. Run the analyzer:
```bash
python main.py
```

3. View the results:
   - Console output shows:
     - Original text
     - Total word count
     - Number of unique words
     - Top 5 most frequent words
   - Detailed results are saved in `results.json`

## Example Output

```
Original text:
[Your text here]

Total number of words: X
Number of unique words: Y

Top 5 most frequent words:
word1: 5
word2: 3
word3: 2
word4: 2
word5: 1

Results saved to results.json
```

## Project Structure

- `main.py`: Main application code
- `requirements.txt`: Project dependencies
- `results.json`: Analysis output file

## License

This project is licensed under the MIT License - see the LICENSE file for details. 