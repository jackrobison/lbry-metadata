import json
import google.protobuf.json_format as json_pb
from google.protobuf.message import Message


class Schema(Message):
    @classmethod
    def load(cls, message):
        raise NotImplementedError

    @classmethod
    def _load(cls, data, message):
        data = json.dumps(data)
        return json_pb.Parse(data, message)

    @property
    def serialized(self):
        return self.SerializeToString()
