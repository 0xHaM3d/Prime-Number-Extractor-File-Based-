# Prime Number Extractor (File-Based)

This Python script reads numbers from a `.txt` file, identifies which ones are prime, and writes the prime numbers into a separate output file.

## How It Works

- Reads numbers line by line from an input text file

- Ignores invalid or non-numeric lines

- Checks each number for primality using an efficient square-root approach

- Saves all detected prime numbers into a new text file

## Files

- `numbers.txt — input` file containing one number per line

- `prime_numbers.txt` output file containing only prime numbers

## Usage

1. Place your list of numbers in a file named `numbers.txt` in the same directory as the script. Ensure each number is on a new line.

2. Run the script via your terminal:
    ```Bash
    python prime_extractor.py
    ```

3. The prime numbers will be generated in a new file named `prime_numbers.txt`.



