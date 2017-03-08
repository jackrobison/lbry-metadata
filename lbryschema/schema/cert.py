from copy import deepcopy

from lbryschema.schema import cert_pb2 as cert_pb
from lbryschema.schema.schema import Schema
from lbryschema.utils import VERSION_MAP


class _ECDSAKeyHelper(object):
    def __init__(self, key):
        self._key = key

    @property
    def der(self):
        return self._key.to_der()


class Cert(Schema):
    KEY_TYPE_ECDSA = 1

    @classmethod
    def load(cls, message):
        _key = deepcopy(message)
        _message_pb = cert_pb.Cert()
        if isinstance(_key, dict):
            _message_pb.publicKey = _key.pop("publicKey")
            _message_pb.version = VERSION_MAP[_key.pop("version")]
            _message_pb.keyType = _key.pop("keyType")
        else:
            _message_pb.version = _key.version
            _message_pb.keyType = _key.keyType
            _message_pb.publicKey = _key.publicKey
        return cls._load(_key, _message_pb)

    @classmethod
    def load_from_key_obj(cls, key, key_type="ECDSA"):
        if key_type == "ECDSA":
            _key = _ECDSAKeyHelper(key)
            key_type = Cert.KEY_TYPE_ECDSA
        else:
            raise Exception("Unknown key type: %s" % str(type(key)))
        msg = {
            "version": "_0_0_1",
            "keyType": key_type,
            "publicKey": _key.der,
        }
        return cls.load(msg)
