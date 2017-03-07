from copy import deepcopy

from lbryschema.schema import cert_pb2 as cert_pb
from lbryschema.schema.schema import Schema


class Cert(Schema):
    KEY_TYPE_RSA = 1

    @classmethod
    def load(cls, message):
        _cert = deepcopy(message)
        _message_pb = cert_pb.Cert()
        key_type = _cert.pop("keyType")
        if key_type == "RSA":
            _message_pb.keyType = Cert.KEY_TYPE_RSA
        else:
            raise Exception("No key given for cert")

        _message_pb.publicKey.CopyFrom(_cert.pop("publicKey"))
        _message_pb.version = 1

        return cls._load(_cert, _message_pb)
