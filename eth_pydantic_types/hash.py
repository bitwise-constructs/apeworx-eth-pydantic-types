from typing import Any, ClassVar, Optional, Tuple, Type

from pydantic_core.core_schema import (
    CoreSchema,
    ValidationInfo,
    bytes_schema,
    int_schema,
    str_schema,
    with_info_before_validator_function,
)

from eth_pydantic_types.hex import BaseHexStr, HexBytes
from eth_pydantic_types.serializers import hex_serializer
from eth_pydantic_types.validators import validate_bytes_size, validate_int_size, validate_str_size


def _get_hash_pattern(str_size: int) -> str:
    return f"^0x[a-fA-F0-9]{{{str_size}}}$"


def _get_hash_examples(str_size: int) -> Tuple[str, str, str, str]:
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
    schema_examples: ClassVar[Tuple[str, ...]] = _get_hash_examples(1)

    @classmethod
    def __get_pydantic_core_schema__(cls, value, handler=None) -> CoreSchema:
        schema = with_info_before_validator_function(
            cls.__eth_pydantic_validate__,
            bytes_schema(max_length=cls.size, min_length=cls.size),
        )
        schema["serialization"] = hex_serializer
        return schema

    @classmethod
    def __eth_pydantic_validate__(
        cls, value: Any, info: Optional[ValidationInfo] = None
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
    schema_examples: ClassVar[Tuple[str, ...]] = _get_hash_examples(1)

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
        sized_value = cls.validate_size(hex_value)
        return cls(f"0x{sized_value}")

    @classmethod
    def validate_size(cls, value: str) -> str:
        return validate_str_size(value, cls.size * 2)


class HashInt(int):
    """
    Represents an integer.
    This type is meant to be overridden by the larger hash types with a new size.
    e.g. Int32, UInt64.
    """

    size: ClassVar[int] = 1
    signed: ClassVar[bool] = True

    @classmethod
    def __get_pydantic_core_schema__(cls, value, handler=None) -> CoreSchema:
        return with_info_before_validator_function(cls.__eth_pydantic_validate__, int_schema())

    @classmethod
    def __eth_pydantic_validate__(cls, value: Any, info: Optional[ValidationInfo] = None) -> int:
        return cls(cls.validate_size(int(value)))

    @classmethod
    def validate_size(cls, value: int) -> int:
        return validate_int_size(value, cls.size, cls.signed)


def _make_hash_cls(size: int, base_type: Type, signed: bool = True):

    str_size = size * 2
    if issubclass(base_type, bytes):
        suffix = "Bytes"
        base_type = HashBytes
        type_dict = dict(
            size=size,
            schema_pattern=_get_hash_pattern(str_size),
            schema_examples=_get_hash_examples(str_size),
        )
    elif issubclass(base_type, str):
        suffix = "Str"
        base_type = HashStr
        type_dict = dict(
            size=size,
            schema_pattern=_get_hash_pattern(str_size),
            schema_examples=_get_hash_examples(str_size),
        )
    else:
        suffix = "Int" if signed else "UInt"
        base_type = HashInt
        type_dict = dict(
            size=size,
            signed=signed,
        )

    return type(
        f"Hash{suffix}{size}",
        (base_type,),
        type_dict,
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
HashInt8 = _make_hash_cls(8, int, signed=True)
HashInt16 = _make_hash_cls(16, int, signed=True)
HashInt32 = _make_hash_cls(32, int, signed=True)
HashInt64 = _make_hash_cls(64, int, signed=True)
HashInt128 = _make_hash_cls(128, int, signed=True)
HashInt256 = _make_hash_cls(256, int, signed=True)
HashUInt8 = _make_hash_cls(8, int, signed=False)
HashUInt16 = _make_hash_cls(16, int, signed=False)
HashUInt32 = _make_hash_cls(32, int, signed=False)
HashUInt64 = _make_hash_cls(64, int, signed=False)
HashUInt128 = _make_hash_cls(128, int, signed=False)
HashUInt256 = _make_hash_cls(256, int, signed=False)
