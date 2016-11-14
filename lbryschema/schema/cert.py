from copy import deepcopy

from lbryschema.schema.public_key import RSAPublicKey
from lbryschema.schema import cert_pb2 as cert_pb
from lbryschema.schema.schema import Schema


class Cert(Schema):
    @classmethod
    def load(cls, message):
        _cert = deepcopy(message)
        _message_pb = cert_pb.Cert()
        publicKey = _cert.pop("rsa")
        if isinstance(publicKey, dict):
            _message_pb.publicKey.CopyFrom(RSAPublicKey.load(publicKey))
        else:
            _message_pb.publicKey.CopyFrom(publicKey)
        return cls._load(_cert, _message_pb)
