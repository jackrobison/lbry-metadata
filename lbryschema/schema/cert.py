from copy import deepcopy

from lbryschema.schema.public_key import RSAPublicKey
from lbryschema.schema import cert_pb2 as cert_pb
from lbryschema.schema.schema import Schema


class Cert(Schema):
    @classmethod
    def load(cls, message):
        _cert = deepcopy(message)
        _message_pb = cert_pb.Cert()
        public_key = _cert.pop("rsa")
        if isinstance(public_key, dict):
            _message_pb.public_key.CopyFrom(RSAPublicKey.load(public_key))
        else:
            _message_pb.public_key.CopyFrom(public_key)
        return cls._load(_cert, _message_pb)
