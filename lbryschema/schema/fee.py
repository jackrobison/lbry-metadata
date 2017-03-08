from copy import deepcopy

from lbryschema.schema.schema import Schema
from lbryschema.schema import fee_pb2
from lbryschema.utils import base_decode


class UnknownSourceType(Exception):
    pass


class Fee(Schema):
    @classmethod
    def load(cls, message, address_base=64):
        _fee = deepcopy(message)
        currency = _fee.pop('currency')
        if currency == "LBC":
            currency_code = 1
        elif currency == "BTC":
            currency_code = 2
        elif currency == "USD":
            currency_code = 3
        else:
            raise Exception("Unknown currency")
        _message_pb = fee_pb2.Fee()
        _message_pb.version = 1
        _message_pb.currency = currency_code
        if address_base == 58:
            _message_pb.address = base_decode(_fee.pop('address'), 25, 58)
        elif address_base == 64:
            _message_pb.address = _fee.pop('address').decode("base64")
        else:
            raise Exception("Unsupported address base %i" % address_base)
        return cls._load(_fee, _message_pb)
