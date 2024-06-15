from typing import Any, ClassVar, Optional, Tuple, Type

from pydantic_core.core_schema import (
    CoreSchema,
    ValidationInfo,
    str_schema,
    with_info_before_validator_function,
)

from eth_pydantic_types.hashing import get_hash_examples, get_hash_pattern
from eth_pydantic_types.hex import BaseHexStr
from eth_pydantic_types.validators import validate_str_size


class String(BaseHexStr):
    """
    Represents a single-slot static hash as a str.
    This type is meant to be overridden by the larger hash types with a new size.
    e.g. String20, String32.
    """

    bound: bool = False
    size: ClassVar[int] = 0
    schema_pattern: ClassVar[str] = get_hash_pattern(1)
    schema_examples: ClassVar[Tuple[str, ...]] = get_hash_examples(1)

    @classmethod
    def __get_pydantic_core_schema__(cls, value, handler=None) -> CoreSchema:
        str_size = cls.size * 2 + 2
        return with_info_before_validator_function(
            cls.__eth_pydantic_validate__, str_schema(max_length=str_size, min_length=str_size)
        )

    @classmethod
    def __eth_pydantic_validate__(cls, value: Any, info: Optional[ValidationInfo] = None) -> str:
        hex_str = cls.validate_hex(value)
        hex_value = hex_str[2:] if hex_str.startswith("0x") else hex_str
        sized_value = cls.validate_size(hex_value) if cls.bound else hex_value
        return cls(f"0x{sized_value}")

    @classmethod
    def validate_size(cls, value: str) -> str:
        return validate_str_size(value, cls.size * 2)


def _make_cls(size: int, base_type: Type, prefix: str = ""):
    str_size = size * 2
    if issubclass(base_type, str):
        display = "Str"
        base_type = String
        type_dict = dict(
            bound=True,
            size=size,
            schema_pattern=get_hash_pattern(str_size),
            schema_examples=get_hash_examples(str_size),
        )

    return type(
        f"{prefix}{display}{size}",
        (base_type,),
        type_dict,
    )


String4 = _make_cls(4, str)
String8 = _make_cls(8, str)
String16 = _make_cls(16, str)
String20 = _make_cls(20, str)
String32 = _make_cls(32, str)
String64 = _make_cls(64, str)
