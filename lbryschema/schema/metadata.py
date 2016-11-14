from copy import deepcopy

from lbryschema.schema import metadata_pb2
from lbryschema.schema.fee import Fee
from lbryschema.schema.schema import Schema


class Metadata(Schema):
    @classmethod
    def load(cls, message):
        _metadata = deepcopy(message)
        _message_pb = metadata_pb2.Metadata()
        if 'fee' in _metadata:
            fee_pb = Fee.load(_metadata.pop('fee'))
            _message_pb.fee.CopyFrom(fee_pb)
        return cls._load(_metadata, _message_pb)
