"""
Simple text analyzer that counts words and their frequencies.
"""

import json

def analyze_file(filename):
    """Read, analyze text file and return results."""
    try:
        # Read file
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Analyze text
        words = text.lower().split()
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        return {
            'total_words': len(words),
            'unique_words': len(word_freq),
            'word_frequencies': word_freq
        }
    except FileNotFoundError:
        print(f"\nError: File '{filename}' not found.")
    except Exception as e:
        print(f"\nError: {str(e)}")
    return None

def main():
    """Main function to run the text analyzer."""
    while True:
        print("\nText Analyzer")
        print("1. Analyze file")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ")
        
        if choice == "1":
            filename = input("Enter file path: ")
            results = analyze_file(filename)
            
            if results:
                # Display results
                print(f"\nTotal words: {results['total_words']}")
                print(f"Unique words: {results['unique_words']}")
                print("\nWord frequencies:")
                for word, freq in sorted(results['word_frequencies'].items(), 
                                      key=lambda x: x[1], reverse=True):
                    print(f"{word}: {freq}")
                
                # Save results
                try:
                    with open("results.json", "w", encoding="utf-8") as f:
                        json.dump(results, f, indent=4)
                    print("\nResults saved to results.json")
                except Exception as e:
                    print(f"\nError saving results: {str(e)}")
                    
        elif choice == "2":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main() 