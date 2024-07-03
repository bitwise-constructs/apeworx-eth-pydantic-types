"""
These models are used to match the lowercase type names used by the abi.
"""

from typing import Annotated, ClassVar

from hexbytes import HexBytes
from pydantic import Field
from typing_extensions import TypeAlias

from .address import Address
from .hex import BoundHexBytes

bytes: TypeAlias = HexBytes
string: TypeAlias = str

bytes1 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=1))]
bytes2 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=2))]
bytes3 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=3))]
bytes4 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=4))]
bytes5 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=5))]
bytes6 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=6))]
bytes7 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=7))]
bytes8 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=8))]
bytes9 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=9))]
bytes10 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=10))]
bytes11 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=11))]
bytes12 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=12))]
bytes13 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=13))]
bytes14 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=14))]
bytes15 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=15))]
bytes16 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=16))]
bytes17 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=17))]
bytes18 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=18))]
bytes19 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=19))]
bytes20 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=20))]
bytes21 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=21))]
bytes22 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=22))]
bytes23 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=23))]
bytes24 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=24))]
bytes25 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=25))]
bytes26 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=26))]
bytes27 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=27))]
bytes28 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=28))]
bytes29 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=29))]
bytes30 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=30))]
bytes31 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=31))]
bytes32 = Annotated[BoundHexBytes, Field(default=BoundHexBytes(size=32))]


class address(Address):
    """
    Represents a 20 character hex string address.
    """

    abi_type: ClassVar[str] = "address"


int8 = Annotated[int, Field(lt=2**7, ge=-(2**7))]
int16 = Annotated[int, Field(lt=2**15, ge=-(2**15))]
int24 = Annotated[int, Field(lt=2**23, ge=-(2**23))]
int32 = Annotated[int, Field(lt=2**31, ge=-(2**31))]
int40 = Annotated[int, Field(lt=2**39, ge=-(2**39))]
int48 = Annotated[int, Field(lt=2**47, ge=-(2**47))]
int56 = Annotated[int, Field(lt=2**55, ge=-(2**55))]
int64 = Annotated[int, Field(lt=2**63, ge=-(2**63))]
int72 = Annotated[int, Field(lt=2**71, ge=-(2**71))]
int80 = Annotated[int, Field(lt=2**79, ge=-(2**79))]
int88 = Annotated[int, Field(lt=2**87, ge=-(2**87))]
int96 = Annotated[int, Field(lt=2**95, ge=-(2**95))]
int104 = Annotated[int, Field(lt=2**103, ge=-(2**103))]
int112 = Annotated[int, Field(lt=2**111, ge=-(2**111))]
int120 = Annotated[int, Field(lt=2**119, ge=-(2**119))]
int128 = Annotated[int, Field(lt=2**127, ge=-(2**127))]
int136 = Annotated[int, Field(lt=2**135, ge=-(2**135))]
int144 = Annotated[int, Field(lt=2**143, ge=-(2**143))]
int152 = Annotated[int, Field(lt=2**151, ge=-(2**151))]
int160 = Annotated[int, Field(lt=2**159, ge=-(2**159))]
int168 = Annotated[int, Field(lt=2**167, ge=-(2**167))]
int176 = Annotated[int, Field(lt=2**175, ge=-(2**175))]
int184 = Annotated[int, Field(lt=2**183, ge=-(2**183))]
int192 = Annotated[int, Field(lt=2**191, ge=-(2**191))]
int200 = Annotated[int, Field(lt=2**199, ge=-(2**199))]
int208 = Annotated[int, Field(lt=2**207, ge=-(2**207))]
int216 = Annotated[int, Field(lt=2**215, ge=-(2**215))]
int224 = Annotated[int, Field(lt=2**223, ge=-(2**223))]
int232 = Annotated[int, Field(lt=2**231, ge=-(2**231))]
int240 = Annotated[int, Field(lt=2**239, ge=-(2**239))]
int248 = Annotated[int, Field(lt=2**247, ge=-(2**247))]
int256 = Annotated[int, Field(lt=2**255, ge=-(2**255))]
uint8 = Annotated[int, Field(lt=2**8, ge=0)]
uint16 = Annotated[int, Field(lt=2**16, ge=0)]
uint24 = Annotated[int, Field(lt=2**24, ge=0)]
uint32 = Annotated[int, Field(lt=2**32, ge=0)]
uint40 = Annotated[int, Field(lt=2**40, ge=0)]
uint48 = Annotated[int, Field(lt=2**48, ge=0)]
uint56 = Annotated[int, Field(lt=2**56, ge=0)]
uint64 = Annotated[int, Field(lt=2**64, ge=0)]
uint72 = Annotated[int, Field(lt=2**72, ge=0)]
uint80 = Annotated[int, Field(lt=2**80, ge=0)]
uint88 = Annotated[int, Field(lt=2**88, ge=0)]
uint96 = Annotated[int, Field(lt=2**96, ge=0)]
uint104 = Annotated[int, Field(lt=2**104, ge=0)]
uint112 = Annotated[int, Field(lt=2**112, ge=0)]
uint120 = Annotated[int, Field(lt=2**120, ge=0)]
uint128 = Annotated[int, Field(lt=2**128, ge=0)]
uint136 = Annotated[int, Field(lt=2**136, ge=0)]
uint144 = Annotated[int, Field(lt=2**144, ge=0)]
uint152 = Annotated[int, Field(lt=2**152, ge=0)]
uint160 = Annotated[int, Field(lt=2**160, ge=0)]
uint168 = Annotated[int, Field(lt=2**168, ge=0)]
uint176 = Annotated[int, Field(lt=2**176, ge=0)]
uint184 = Annotated[int, Field(lt=2**184, ge=0)]
uint192 = Annotated[int, Field(lt=2**192, ge=0)]
uint200 = Annotated[int, Field(lt=2**200, ge=0)]
uint208 = Annotated[int, Field(lt=2**208, ge=0)]
uint216 = Annotated[int, Field(lt=2**216, ge=0)]
uint224 = Annotated[int, Field(lt=2**224, ge=0)]
uint232 = Annotated[int, Field(lt=2**232, ge=0)]
uint240 = Annotated[int, Field(lt=2**240, ge=0)]
uint248 = Annotated[int, Field(lt=2**248, ge=0)]
uint256 = Annotated[int, Field(lt=2**256, ge=0)]
