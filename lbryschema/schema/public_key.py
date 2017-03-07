from copy import deepcopy

from lbryschema.schema import public_key_pb2
from lbryschema.schema.schema import Schema


class _RSAKeyHelper(object):
    def __init__(self, key):
        self._key = key

    @property
    def der(self):
        return self._key.publickey().exportKey('DER')


class PublicKey(Schema):
    KEY_TYPE_RSA = "RSA"

    @classmethod
    def load(cls, message):
        _key = deepcopy(message)
        _message_pb = public_key_pb2.PublicKey()
        _message_pb.version = 1
        if isinstance(_key, dict):
            _message_pb.publicKey = _key.pop("publicKey")
        else:
            _message_pb.publicKey = _key.publicKey
        return cls._load(_key, _message_pb)

    @classmethod
    def load_from_key_obj(cls, key, key_type=KEY_TYPE_RSA):
        if key_type == PublicKey.KEY_TYPE_RSA:
            _key = _RSAKeyHelper(key)
        else:
            raise Exception("Unknown key type: %s" % key_type)
        msg = {
            "version": "_0_0_1",
            "keyType": PublicKey.KEY_TYPE_RSA,
            "publicKey": _key.der,
        }
        return cls.load(msg)
