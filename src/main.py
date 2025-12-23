# read the .txt file containing digits
# Defining prime digits
# Save found prime digits in a new .txt file

import math

def is_prime(num: int) -> bool:
    """Defining the prime digits

    :param num: Prime Numbers 
    :return: True False
    """
    if num <= 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


def extract_primes(input_file: str, output_file: str):
    """Setting output and input files

    :param input_file: a txt file contining numbers with one number per line
    :param output_file: A txt file contining extracing prime numbers from input file
    """
    primes = []

    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip() # remove whitespace/newline

            if line.isdigit():  # ensure it's a digit
                number = int(line)

                if is_prime(number):
                    primes.append(str(number))

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("\n".join(primes))


if __name__ == '__main__':
    extract_primes("numbers.txt", "prime_numbers.txt")