from typing import TYPE_CHECKING, Any, ClassVar, Optional

from pydantic_core.core_schema import bytes_schema, str_schema, with_info_before_validator_function

from eth_pydantic_types.hex import BaseHexStr, HexBytes
from eth_pydantic_types.serializers import hex_serializer
from eth_pydantic_types.validators import validate_bytes_size, validate_str_size

if TYPE_CHECKING:
    from pydantic_core.core_schema import CoreSchema, ValidationInfo


def _get_hash_pattern(str_size: int) -> str:
    return f"^0x[a-fA-F0-9]{{{str_size}}}$"


def _get_hash_examples(str_size: int) -> tuple[str, str, str, str]:
    zero_hash = f"0x{'0' * str_size}"
    leading_zero = f"0x01{'1e' * ((str_size - 1) // 2)}"
    trailing_zero = f"0x{'1e' * ((str_size - 1) // 2)}10"
    full_hash = f"0x{'1e' * (str_size // 2)}"
    return zero_hash, leading_zero, trailing_zero, full_hash


class HashBytes(HexBytes):
    """
    Represents a single-slot static hash as bytes.
    This type is meant to be overridden by the larger hash types with a new size.
    The class variable "size" is overridden in subclasses for each byte-size,
    e.g. HashBytes20, HashBytes32.
    """

    size: ClassVar[int] = 1
    schema_pattern: ClassVar[str] = _get_hash_pattern(1)
    schema_examples: ClassVar[tuple[str, ...]] = _get_hash_examples(1)

    @classmethod
    def __get_pydantic_core_schema__(cls, value, handler=None) -> "CoreSchema":
        schema = with_info_before_validator_function(
            cls.__eth_pydantic_validate__,
            bytes_schema(max_length=cls.size, min_length=cls.size),
        )
        schema["serialization"] = hex_serializer
        return schema

    @classmethod
    def __eth_pydantic_validate__(
        cls, value: Any, info: Optional["ValidationInfo"] = None
    ) -> HexBytes:
        return cls(cls.validate_size(HexBytes(value)))

    @classmethod
    def validate_size(cls, value: bytes) -> bytes:
        return validate_bytes_size(value, cls.size)


class HashStr(BaseHexStr):
    """
    Represents a single-slot static hash as a str.
    This type is meant to be overridden by the larger hash types with a new size.
    e.g. HashStr20, HashStr32.
    """

    size: ClassVar[int] = 1
    schema_pattern: ClassVar[str] = _get_hash_pattern(1)
    schema_examples: ClassVar[tuple[str, ...]] = _get_hash_examples(1)

    @classmethod
    def __get_pydantic_core_schema__(cls, value, handler=None) -> "CoreSchema":
        str_size = cls.size * 2 + 2
        return with_info_before_validator_function(
            cls.__eth_pydantic_validate__, str_schema(max_length=str_size, min_length=str_size)
        )

    @classmethod
    def __eth_pydantic_validate__(cls, value: Any, info: Optional["ValidationInfo"] = None) -> str:
        hex_str = cls.validate_hex(value)
        hex_value = hex_str[2:] if hex_str.startswith("0x") else hex_str
        sized_value = cls.validate_size(hex_value)
        return cls(f"0x{sized_value}")

    @classmethod
    def validate_size(cls, value: str) -> str:
        return validate_str_size(value, cls.size * 2)


def _make_hash_cls(size: int, base_type: type):
    if issubclass(base_type, bytes):
        suffix = "Bytes"
        base_type = HashBytes
    else:
        suffix = "Str"
        base_type = HashStr

    str_size = size * 2
    return type(
        f"Hash{suffix}{size}",
        (base_type,),
        dict(
            size=size,
            schema_pattern=_get_hash_pattern(str_size),
            schema_examples=_get_hash_examples(str_size),
        ),
    )


def __getattr__(name: str):
    _type: type
    if name.startswith("HashBytes"):
        number = name.replace("HashBytes", "")
        _type = bytes
    elif name.startswith("HashStr"):
        number = name.replace("HashStr", "")
        _type = str
    else:
        raise AttributeError(name)

    if not number.isnumeric():
        raise AttributeError(name)

    return _make_hash_cls(int(number), _type)


__all__ = [
    "HashBytes4",
    "HashBytes8",
    "HashBytes16",
    "HashBytes20",
    "HashBytes32",
    "HashBytes64",
    "HashStr4",
    "HashStr8",
    "HashStr16",
    "HashStr20",
    "HashStr32",
    "HashStr64",
]
