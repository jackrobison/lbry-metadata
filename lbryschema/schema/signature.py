from copy import deepcopy

from lbryschema.schema import signature_pb2
from lbryschema.schema.public_key import RSASignature
from lbryschema.schema.schema import Schema


class Signature(Schema):
    @classmethod
    def load(cls, message):
        _signature = deepcopy(message)
        _message_pb = signature_pb2.Signature()
        rsa_sig = _signature.pop("rsa")
        if isinstance(rsa_sig, dict):
            _message_pb.signature.CopyFrom(RSASignature.load(rsa_sig))
        else:
            _message_pb.signature.CopyFrom(rsa_sig)
        return cls._load(_signature, _message_pb)