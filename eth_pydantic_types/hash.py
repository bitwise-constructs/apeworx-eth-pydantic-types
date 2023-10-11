from typing import Any, ClassVar, Optional, Tuple, Type

from pydantic_core.core_schema import (
    CoreSchema,
    ValidationInfo,
    bytes_schema,
    str_schema,
    with_info_before_validator_function,
)

from eth_pydantic_types.hex import BaseHexStr, HexBytes
from eth_pydantic_types.serializers import hex_serializer
from eth_pydantic_types.validators import validate_bytes_size, validate_str_size


def _get_hash_pattern(str_size: int) -> str:
    return f"^0x[a-fA-F0-9]{{{str_size}}}$"


def _get_hash_examples(str_size: int) -> Tuple[str, str]:
    return f"0x{'0' * str_size}", f"0x{'1e' * (str_size // 2)}"


class HashBytes(HexBytes):
    """
    Represents a single-slot static hash as bytes.
    The class variable "size" is overridden in subclasses for each byte-size,
    e.g. HashBytes4, HashBytes20, HashBytes32.
    """

    size: ClassVar[int] = 1
    schema_pattern: ClassVar[str] = _get_hash_pattern(1)
    schema_examples: ClassVar[Tuple[str, ...]] = _get_hash_examples(1)

    def __get_pydantic_core_schema__(self, *args, **kwargs) -> CoreSchema:
        schema = with_info_before_validator_function(
            self._validate_hash, bytes_schema(max_length=self.size, min_length=self.size)
        )
        schema["serialization"] = hex_serializer
        return schema

    @classmethod
    def _validate_hash(cls, value: Any, info: Optional[ValidationInfo] = None) -> bytes:
        return cls(cls.validate_size(HexBytes(value)))

    @classmethod
    def validate_size(cls, value: bytes) -> bytes:
        return validate_bytes_size(value, cls.size)


class HashStr(BaseHexStr):
    """
    Represents a single-slot static hash as a str.
    The class variable "size" is overridden in subclasses for each byte-size,
    e.g. HashStr4, HashStr20, HashStr32.
    """

    size: ClassVar[int] = 1
    schema_pattern: ClassVar[str] = _get_hash_pattern(1)
    schema_examples: ClassVar[Tuple[str, ...]] = _get_hash_examples(1)

    def __get_pydantic_core_schema__(self, *args, **kwargs) -> CoreSchema:
        str_size = self.size * 2 + 2
        return with_info_before_validator_function(
            self._validate_hash, str_schema(max_length=str_size, min_length=str_size)
        )

    @classmethod
    def _validate_hash(cls, value: Any, info: Optional[ValidationInfo] = None) -> str:
        hex_str = cls.validate_hex(value)
        hex_value = hex_str[2:] if hex_str.startswith("0x") else hex_str
        sized_value = cls.validate_size(hex_value)
        return cls(f"0x{sized_value}")

    @classmethod
    def validate_size(cls, value: str) -> str:
        return validate_str_size(value, cls.size * 2)


def _make_hash_cls(size: int, base_type: Type):
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


HashBytes4 = _make_hash_cls(4, bytes)
HashBytes8 = _make_hash_cls(8, bytes)
HashBytes16 = _make_hash_cls(16, bytes)
HashBytes20 = _make_hash_cls(20, bytes)
HashBytes32 = _make_hash_cls(32, bytes)
HashBytes64 = _make_hash_cls(64, bytes)
HashStr4 = _make_hash_cls(4, str)
HashStr8 = _make_hash_cls(8, str)
HashStr16 = _make_hash_cls(16, str)
HashStr20 = _make_hash_cls(20, str)
HashStr32 = _make_hash_cls(32, str)
HashStr64 = _make_hash_cls(64, str)
