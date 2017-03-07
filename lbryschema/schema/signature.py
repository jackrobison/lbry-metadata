from copy import deepcopy

from lbryschema.schema import signature_pb2
from lbryschema.schema.schema import Schema


class Signature(Schema):
    SIGNATURE_TYPE_RSA = 1
    SIGNATURE_TYPE_ECDSA = 1

    @classmethod
    def load(cls, message):
        _signature = deepcopy(message)
        _message_pb = signature_pb2.Signature()
        sig_type = _signature.pop("signatureType")
        if sig_type == "RSA":
            sig_type = Signature.SIGNATURE_TYPE_RSA
        else:
            raise Exception("No key type given for signature")
        _message_pb.version = 1
        _message_pb.signatureType = sig_type
        _message_pb.signature = _signature.pop("signature")
        return cls._load(_signature, _message_pb)
