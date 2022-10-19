import secrets
from math import log2
from enum import IntEnum

class StrengthToEntropy(IntEnum):
    Слабый = 0
    Легкий = 30
    Хороший = 50
    Сложный = 70
    Превосходный = 120


def create_new(length: int, characters: str) -> str:
    return ''.join(secrets.choice(characters) for _ in range(length))


def get_entropy(length: int, character_number: int):
    try:
        entropy = length * log2(character_number)
    except ValueError:
        return 0.0

    return round(entropy, 2)


