from src.butterfly_generator.generator import ButterflyGenerator

def test_random_number_generation():
    bg = ButterflyGenerator()
    for _ in range(100):
        random = bg.random()
        assert random >= bg.CONST_MIN_VAL and random <= bg.CONST_MAX_VAL
