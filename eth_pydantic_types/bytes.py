from typing import Any, ClassVar, Optional, Tuple, Type

from pydantic_core.core_schema import (
    CoreSchema,
    ValidationInfo,
    bytes_schema,
    with_info_before_validator_function,
)

from eth_pydantic_types.hashing import get_hash_examples, get_hash_pattern
from eth_pydantic_types.hex import HexBytes
from eth_pydantic_types.serializers import hex_serializer
from eth_pydantic_types.validators import validate_bytes_size


class Bytes(HexBytes):
    """
    Represents a single-slot static hash as bytes.
    This type is meant to be overridden by the larger hash types with a new size.
    The class variable "size" is overridden in subclasses for each byte-size,
    e.g. Bytes20, Bytes32.
    """

    size: ClassVar[int] = 1
    schema_pattern: ClassVar[str] = get_hash_pattern(1)
    schema_examples: ClassVar[Tuple[str, ...]] = get_hash_examples(1)

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


def _make_cls(size: int, base_type: Type, prefix: str = ""):
    str_size = size * 2
    if issubclass(base_type, bytes):
        display = "Bytes"
        base_type = Bytes
        type_dict = dict(
            size=size,
            schema_pattern=get_hash_pattern(str_size),
            schema_examples=get_hash_examples(str_size),
        )
    return type(
        f"{prefix}{display}{size}",
        (base_type,),
        type_dict,
    )


Bytes4 = _make_cls(4, bytes)
Bytes8 = _make_cls(8, bytes)
Bytes16 = _make_cls(16, bytes)
Bytes20 = _make_cls(20, bytes)
Bytes32 = _make_cls(32, bytes)
Bytes64 = _make_cls(64, bytes)
