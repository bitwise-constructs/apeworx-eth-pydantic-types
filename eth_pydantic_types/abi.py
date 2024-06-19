"""
These models are used to match the lowercase type names used by the abi.
"""

from typing import ClassVar

from .address import Address
from .numbers import _make_cls

int8 = _make_cls(8, int, dict_additions=dict(abi_type="int8"))
int16 = _make_cls(16, int, dict_additions=dict(abi_type="int16"))
int32 = _make_cls(32, int, dict_additions=dict(abi_type="int32"))
int64 = _make_cls(64, int, dict_additions=dict(abi_type="int64"))
int128 = _make_cls(128, int, dict_additions=dict(abi_type="int128"))
int256 = _make_cls(256, int, dict_additions=dict(abi_type="int256"))
uint8 = _make_cls(8, int, signed=False, dict_additions=dict(abi_type="uint8"))
uint16 = _make_cls(16, int, signed=False, dict_additions=dict(abi_type="uint16"))
uint32 = _make_cls(32, int, signed=False, dict_additions=dict(abi_type="uint32"))
uint64 = _make_cls(64, int, signed=False, dict_additions=dict(abi_type="uint64"))
uint128 = _make_cls(128, int, signed=False, dict_additions=dict(abi_type="uint128"))
uint256 = _make_cls(256, int, signed=False, dict_additions=dict(abi_type="uint256"))


class string(str):
    """
    Represents a string.
    """

    abi_type: ClassVar[str] = "string"


class address(Address):
    """
    Represents a 20 character hex string address.
    """

    abi_type: ClassVar[str] = "address"
