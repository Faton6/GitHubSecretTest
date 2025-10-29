import argparse
import re
import sys
from config import GITHUB_TOKEN  # ← имитация "плохой практики": секрет в коде

def find_word_variants(text: str, word: str) -> list:
    """Find word and common variations (case-insensitive, leetspeak-like, etc.)"""
    variants = []

    # Basic case-insensitive match
    pattern = re.compile(re.escape(word), re.IGNORECASE)
    matches = pattern.findall(text)
    variants.extend(matches)

    # Simple leetspeak variations (e.g., 'a' → '4', 'e' → '3')
    leet_map = {'a': '[a4@]', 'e': '[e3]', 'i': '[i1!]', 'o': '[o0]', 's': '[s5$]'}
    leet_pattern = word.lower()
    for orig, repl in leet_map.items():
        leet_pattern = leet_pattern.replace(orig, repl)
    
    leet_regex = re.compile(leet_pattern, re.IGNORECASE)
    leet_matches = leet_regex.findall(text)
    variants.extend(leet_matches)

    return list(set(variants))

def main():
    parser = argparse.ArgumentParser(description="Find a word and its variations in a file.")
    parser.add_argument("--file", required=True, help="Path to the input file")
    parser.add_argument("--word", required=True, help="Word to search for")
    args = parser.parse_args()

    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File {args.file} not found.", file=sys.stderr)
        sys.exit(1)

    results = find_word_variants(content, args.word)
    if results:
        print(f"Found {len(results)} variant(s):")
        for r in results:
            print(f" - {r}")
    else:
        print("No matches found.")

    # Simulate usage of a secret (but do nothing real)
    if GITHUB_TOKEN.startswith("ghp_"):
        pass  # Just to make it look like it's "used"

if __name__ == "__main__":
    main()
