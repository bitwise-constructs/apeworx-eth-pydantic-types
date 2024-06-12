import pytest
from pydantic import BaseModel, ValidationError

from eth_pydantic_types.hash import (
    HashInt8,
    HashInt16,
    HashInt32,
    HashInt64,
    HashInt128,
    HashInt256,
    HashUInt8,
    HashUInt16,
    HashUInt32,
    HashUInt64,
    HashUInt128,
    HashUInt256,
)


class IntModel(BaseModel):
    valueint8: HashInt8
    valueint16: HashInt16
    valueint32: HashInt32
    valueint64: HashInt64
    valueint128: HashInt128
    valueint256: HashInt256
    valueuint8: HashUInt8
    valueuint16: HashUInt16
    valueuint32: HashUInt32
    valueuint64: HashUInt64
    valueuint128: HashUInt128
    valueuint256: HashUInt256

    @classmethod
    def from_single(cls, value):
        return cls(
            valueint8=value,
            valueint16=value,
            valueint32=value,
            valueint64=value,
            valueint128=value,
            valueint256=value,
            valueuint8=value,
            valueuint16=value,
            valueuint32=value,
            valueuint64=value,
            valueuint128=value,
            valueuint256=value,
        )

    @classmethod
    def signed_from_single(cls, value):
        return cls(
            valueint8=value,
            valueint16=value,
            valueint32=value,
            valueint64=value,
            valueint128=value,
            valueint256=value,
        )

    @classmethod
    def unsigned_from_single(cls, value):
        return cls(
            valueuint8=value,
            valueuint16=value,
            valueuint32=value,
            valueuint64=value,
            valueuint128=value,
            valueuint256=value,
        )


def test_invalid_int():
    with pytest.raises(ValidationError):
        IntModel.unsigned_from_single(-1)
