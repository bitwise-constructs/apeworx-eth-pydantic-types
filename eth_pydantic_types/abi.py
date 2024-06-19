from typing import ClassVar

from eth_pydantic_types.numbers import Int as _Int
from eth_pydantic_types.numbers import UInt as _UInt
from eth_pydantic_types.numbers import _make_cls

# from eth_pydantic_types.string import String as _String


class Int(_Int):
    """
    Represents an integer.
    This type is meant to be overridden by the larger types with a new size.
    e.g. Int32, Int64.
    """

    abi_type: ClassVar[str] = "int256"


class UInt(_UInt):
    """
    Represents an unsigned integer.
    This type is meant to be overridden by the larger types with a new size.
    e.g. UInt32, UInt64.
    """

    abi_type: ClassVar[str] = "uint256"


Int8 = _make_cls(8, int, dict_additions=dict(abi_type="int8"))
Int16 = _make_cls(16, int, dict_additions=dict(abi_type="int16"))
Int32 = _make_cls(32, int, dict_additions=dict(abi_type="int32"))
Int64 = _make_cls(64, int, dict_additions=dict(abi_type="int64"))
Int128 = _make_cls(128, int, dict_additions=dict(abi_type="int128"))
Int256 = _make_cls(256, int, dict_additions=dict(abi_type="int256"))
UInt8 = _make_cls(8, int, signed=False, dict_additions=dict(abi_type="uint8"))
UInt16 = _make_cls(16, int, signed=False, dict_additions=dict(abi_type="uint16"))
UInt32 = _make_cls(32, int, signed=False, dict_additions=dict(abi_type="uint32"))
UInt64 = _make_cls(64, int, signed=False, dict_additions=dict(abi_type="uint64"))
UInt128 = _make_cls(128, int, signed=False, dict_additions=dict(abi_type="uint128"))
UInt256 = _make_cls(256, int, signed=False, dict_additions=dict(abi_type="uint256"))


# class String(_String):
#     """
#     Represents a single-slot static hash as a str.
#     This type is meant to be overridden by the larger hash types with a new size.
#     e.g. String20, String32.
#     """

#     abi_type: ClassVar[str] = "string"
