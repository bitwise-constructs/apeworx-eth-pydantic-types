from typing import Tuple


def get_hash_pattern(str_size: int) -> str:
    return f"^0x[a-fA-F0-9]{{{str_size}}}$"


def get_hash_examples(str_size: int) -> Tuple[str, str, str, str]:
    zero_hash = f"0x{'0' * str_size}"
    leading_zero = f"0x01{'1e' * ((str_size - 1) // 2)}"
    trailing_zero = f"0x{'1e' * ((str_size - 1) // 2)}10"
    full_hash = f"0x{'1e' * (str_size // 2)}"
    return zero_hash, leading_zero, trailing_zero, full_hash
