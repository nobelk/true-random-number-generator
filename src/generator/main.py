import sys
import time
from pprint import pprint

from random_number_generator import TrueRandomNumberGenerator
from tqdm import tqdm

if __name__ == "__main__":
    generator = TrueRandomNumberGenerator()
    count = int(sys.argv[1])
    random_numbers = []
    for _ in tqdm(range(count)):
        time.sleep(1)  # avoid hitting the API too frequently
        random_numbers.append(next(generator.random()))
    pprint(random_numbers)
