from copy import deepcopy

from lbryschema.schema.schema import Schema
from lbryschema.schema import fee_pb2


# TODO: break out address validation, validate bitcoin addresses and lbrycrd addresses respectively


class Fee(Schema):
    @classmethod
    def load(cls, message):
        _fee = deepcopy(message)
        currency = _fee.pop('currency')
        if currency == "LBC":
            currency_code = 0
        elif currency == "BTC":
            currency_code = 1
        elif currency == "USD":
            currency_code = 2
        else:
            raise Exception("Unknown currency")
        addr = _fee.pop('address')
        address = addr
        _message_pb = fee_pb2.Fee()
        _message_pb.currency = currency_code
        _message_pb.address = address
        return cls._load(_fee, _message_pb)