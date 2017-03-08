import ecdsa
import hashlib
from lbryschema.schema.claim import Claim


def validate_claim_id(claim_id):
    hex_chars = "0123456789abcdefABCDEF"
    assert len(claim_id) == 64, "Incorrect claimid length: %i" % len(claim_id)
    for c in claim_id:
        assert c in hex_chars, "Claim id is not hex encoded"


class Validator(object):
    KEY_TYPE = None
    VerifyingType = ecdsa.VerifyingKey

    def __init__(self, public_key, certificate_claim_id):
        self._public_key = public_key
        self._certificate_claim_id = certificate_claim_id

    @property
    def public_key(self):
        if not isinstance(self._public_key, self.VerifyingType):
            raise Exception("Key is not type needed for verification")
        return self._public_key

    @property
    def certificate_claim_id(self):
        return self._certificate_claim_id

    @staticmethod
    def key_from_der(der):
        raise NotImplementedError()

    @classmethod
    def load_from_certificate(cls, certificate, certificate_claim_id):
        assert certificate.keyType == cls.KEY_TYPE, Exception("Certificate does not contain a "
                                                              "%s public key" % cls.__name__)
        return cls(cls.key_from_der(certificate.publicKey), certificate_claim_id)

    def validate_signature(self, message, signature):
        raise NotImplementedError()

    def validate_claim_signature(self, claim, claim_id):
        # check that the claim ids provided are the 64 characters long and hex encoded
        validate_claim_id(claim_id)

        # extract and serialize the stream from the claim, then check the signature
        publisher_signature = claim.publisherSignature.signature
        _temp_claim_dict = {
            "version": "_0_0_1",
            "stream": claim.stream
        }
        _temp_claim = Claim.load(_temp_claim_dict)
        serialized = _temp_claim.SerializeToString()
        to_sign = "%s%s%s" % (claim_id, serialized, self.certificate_claim_id)
        return self.validate_signature(to_sign, publisher_signature)


class NIST256pValidator(Validator):
    KEY_TYPE = 1

    @staticmethod
    def key_from_der(der):
        return ecdsa.VerifyingKey.from_der(der)

    def validate_signature(self, message, signature):
        return self.public_key.verify(signature, message, hashfunc=hashlib.sha256)
