from copy import deepcopy

import claim_pb2 as claim_pb
from lbryschema.schema.signature import Signature
from lbryschema.schema.cert import Cert
from lbryschema.schema.schema import Schema
from lbryschema.schema.stream import Stream


class Claim(Schema):
    @classmethod
    def load(cls, message):
        _claim = deepcopy(message)
        _message_pb = claim_pb.Claim()
        if "cert" in _claim:
            _cert = _claim.pop("cert")
            if isinstance(_cert, dict):
                cert = Cert.load(_cert)
            else:
                cert = _cert
            _message_pb.cert.MergeFrom(cert)
        elif "stream" in _claim:
            _stream = _claim.pop("stream")
            if isinstance(_stream, dict):
                stream = Stream.load(_stream)
            else:
                stream = _stream
            _message_pb.stream.MergeFrom(stream)
        else:
            raise AttributeError

        if "publisher_signature" in _claim:
            _publisher_signature = _claim.pop("publisher_signature")
            if isinstance(_stream, dict):
                publisher_signature = Signature.load(_publisher_signature)
            else:
                publisher_signature = _publisher_signature
            _message_pb.publisher_signature.MergeFrom(publisher_signature)

        return cls._load(_claim, _message_pb)
