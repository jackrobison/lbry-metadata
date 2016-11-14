from copy import deepcopy

from lbryschema.schema import source_pb2
from lbryschema.schema.schema import Schema

LBRY_SD_HASH_LENGTH = 48
BTIH_LENGTH = 32


class UnknownSourceType(Exception):
    pass


def validate_lbry_stream_source(source):
    source_val = source.decode('hex')
    assert len(source_val) == LBRY_SD_HASH_LENGTH
    return 0, source_val


def validate_btih_stream_source(source):
    source_val = source.decode('hex')
    assert len(source_val) == BTIH_LENGTH
    return 1, source_val


def validate_source_and_get_prefix(source, source_type):
    if source_type == "lbry_sd_hash":
        return validate_lbry_stream_source(source)
    elif source_type == "btih":
        return validate_btih_stream_source(source)
    else:
        raise UnknownSourceType(source_type)


class Source(Schema):
    @classmethod
    def load(cls, message):
        _source = deepcopy(message)
        type_prefix, source_val = validate_source_and_get_prefix(_source.pop('source'), _source.pop('source_type'))
        _message_pb = source_pb2.Source()
        _message_pb.source_type = type_prefix
        _message_pb.source = source_val
        _message_pb.content_type = _source.pop('content_type')
        return cls._load(_source, _message_pb)
