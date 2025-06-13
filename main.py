#!/usr/bin/env python3
"""
Simple text analyzer application.
"""

import string
import json
from collections import Counter
from typing import Dict, List

class TextAnalyzer:
    def __init__(self, file_path: str):
        """Initialize the text analyzer with a file path."""
        self.file_path = file_path
        self.content = ""
        self.words: List[str] = []
        self.word_freq: Dict[str, int] = {}
    
    def read_file(self) -> bool:
        """Read the content from the file."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.content = file.read()
            return True
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
            return False
        except Exception as e:
            print(f"Error reading file: {str(e)}")
            return False
    
    def process_text(self) -> None:
        """Process the text by converting to lowercase, removing punctuation, and splitting into words."""
        # Convert to lowercase
        text = self.content.lower()
        
        # Remove punctuation
        translator = str.maketrans("", "", string.punctuation)
        text = text.translate(translator)
        
        # Split into words and remove empty strings
        self.words = [word for word in text.split() if word]
    
    def analyze_words(self) -> None:
        """Analyze the words to get word frequencies and statistics."""
        # Get word frequencies using Counter
        self.word_freq = dict(Counter(self.words))
        
        # Print statistics
        print(f"\nTotal number of words: {len(self.words)}")
        print(f"Number of unique words: {len(self.word_freq)}")
        
        # Print top 5 most frequent words
        print("\nTop 5 most frequent words:")
        for word, freq in Counter(self.words).most_common(5):
            print(f"{word}: {freq}")
    
    def save_results(self) -> None:
        """Save analysis results to a JSON file."""
        results = {
            "total_words": len(self.words),
            "unique_words": len(self.word_freq),
            "word_frequencies": self.word_freq
        }
        
        try:
            with open("results.json", "w", encoding="utf-8") as f:
                json.dump(results, f, indent=4)
            print("\nResults saved to results.json")
        except Exception as e:
            print(f"\nError saving results: {str(e)}")
    
    def analyze(self) -> None:
        """Run the complete analysis process."""
        if self.read_file():
            print("Original text:")
            print(self.content)
            
            self.process_text()
            self.analyze_words()
            self.save_results()
        else:
            print("No content to display.")

def main():
    """Main function."""
    analyzer = TextAnalyzer("file.txt")
    analyzer.analyze()

if __name__ == "__main__":
    main()