from src.generator.random_number_generator import TrueRandomGenerator


def test_random_number_generation():
    generator = TrueRandomGenerator()
    for _ in range(100):
        random = generator.random()
        assert random >= generator.CONST_MIN_VAL and random <= generator.CONST_MAX_VAL
