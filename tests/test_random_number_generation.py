import time

from src.generator.random_number_generator import TrueRandomNumberGenerator


def test_random_number_generation():
    generator = TrueRandomNumberGenerator()
    for _ in range(5):
        random = generator.random()
        time.sleep(1)
        assert (next(random) >= generator.CONST_MIN_VAL and next(random) <= generator.CONST_MAX_VAL)
