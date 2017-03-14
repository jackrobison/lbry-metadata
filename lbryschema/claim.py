import json
from google.protobuf import json_format
from collections import OrderedDict
from lbryschema.schema.claim import Claim
from lbryschema.schema.claim_pb2 import Claim as ClaimPB
from lbryschema.validator import NIST256pValidator
from lbryschema.signer import NIST256pSigner
from lbryschema.encoding import decode_fields, decode_b64_fields, encode_fields


class ClaimDict(OrderedDict):
    def __init__(self, claim_dict):
        if isinstance(claim_dict, ClaimPB):
            raise Exception("To initialize %s with a Claim protobuf use %s.load_protobuf" %
                            (self.__class__.__name__, self.__class__.__name__))
        OrderedDict.__init__(self, claim_dict)

    @property
    def protobuf_dict(self):
        """Claim dictionary using base64 to represent bytes"""

        return json.loads(json_format.MessageToJson(self.protobuf, True))

    @property
    def protobuf(self):
        """Claim message object"""

        return Claim.load(self)

    @property
    def serialized(self):
        """Serialized Claim protobuf"""

        return self.protobuf.SerializeToString()

    @property
    def serialized_no_signature(self):
        """Serialized Claim protobuf without publisherSignature field"""
        claim = self.protobuf
        claim.ClearField("publisherSignature")
        return ClaimDict.load_protobuf(claim).serialized

    @property
    def protobuf_len(self):
        """Length of serialized string"""

        return self.protobuf.ByteSize()

    @property
    def json_len(self):
        """Length of json encoded string"""

        return len(json.dumps(self.claim_dict))

    @property
    def claim_dict(self):
        """Claim dictionary with bytes represented as hex and base58"""

        return dict(encode_fields(self))

    @classmethod
    def load_protobuf_dict(cls, protobuf_dict):
        return cls(decode_b64_fields(protobuf_dict))

    @classmethod
    def load_protobuf(cls, protobuf_claim):
        return cls.load_protobuf_dict(json.loads(json_format.MessageToJson(protobuf_claim, True)))

    @classmethod
    def load_dict(cls, claim_dict):
        return cls.load_protobuf(cls(decode_fields(claim_dict)).protobuf)

    @classmethod
    def generate_certificate(cls, private_key):
        signer = NIST256pSigner.load_pem(private_key)
        return cls.load_protobuf(signer.certificate)

    def sign(self, private_key, claim_id, cert_claim_id):
        signer = NIST256pSigner.load_pem(private_key)
        signed = signer.sign_stream_claim(self, claim_id, cert_claim_id)
        return ClaimDict.load_protobuf(signed)

    def validate_signature(self, claim_id, certificate, certificate_claim_id):
        if isinstance(certificate, ClaimDict):
            certificate = certificate.protobuf
        validator = NIST256pValidator.load_from_certificate(certificate, certificate_claim_id)
        return validator.validate_claim_signature(self, claim_id)
