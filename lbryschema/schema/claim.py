from copy import deepcopy

import claim_pb2 as claim_pb
from lbryschema.schema.signature import Signature
from lbryschema.schema.cert import Cert
from lbryschema.schema.schema import Schema
from lbryschema.schema.stream import Stream


class Claim(Schema):
    @classmethod
    def load(cls, message, address_base=64):
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
                stream = Stream.load(_stream, address_base)
            else:
                stream = _stream
            _message_pb.stream.MergeFrom(stream)
        else:
            raise AttributeError

        if "publisherSignature" in _claim:
            _publisherSignature = _claim.pop("publisherSignature")
            if isinstance(_stream, dict):
                publisherSignature = Signature.load(_publisherSignature)
            else:
                publisherSignature = _publisherSignature
            _message_pb.publisherSignature.MergeFrom(publisherSignature)

        return cls._load(_claim, _message_pb)
