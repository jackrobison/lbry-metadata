from copy import deepcopy

from lbryschema.schema.source import Source
from lbryschema.schema import stream_pb2 as stream_pb
from lbryschema.schema.metadata import Metadata
from lbryschema.schema.schema import Schema
from lbryschema.utils import VERSION_MAP


class Stream(Schema):
    @classmethod
    def load(cls, message, address_base=64):
        _claim = deepcopy(message)
        source = Source.load(_claim.pop('source'))
        metadata = Metadata.load(_claim.pop('metadata'), address_base)
        _message_pb = stream_pb.Stream()
        _message_pb.version = VERSION_MAP[_claim.pop("version")]
        _message_pb.source.CopyFrom(source)
        _message_pb.metadata.CopyFrom(metadata)
        return cls._load(_claim, _message_pb)
