import ecdsa
import hashlib
from copy import deepcopy


def validate_claim_id(claim_id):
    hex_chars = "0123456789abcdefABCDEF"
    assert len(claim_id) == 64, "Incorrect claimid length: %i" % len(claim_id)
    for c in claim_id:
        assert c in hex_chars, "Claim id is not hex encoded"


class Validator(object):
    KeyType = None
    VerifyingType = None

    def __init__(self, public_key, certificate_claim_id):
        if not isinstance(public_key, self.VerifyingType):
            raise Exception("Key is not type needed for verification")
        self._public_key = public_key
        self._certificate_claim_id = certificate_claim_id

    @property
    def public_key(self):
        return self._public_key

    @property
    def certificate_claim_id(self):
        return self._certificate_claim_id

    @staticmethod
    def key_from_der(der):
        raise NotImplementedError()

    @classmethod
    def load_from_certificate(cls, certificate_claim, certificate_claim_id):
        certificate = certificate_claim.certificate
        assert certificate.keyType == cls.KeyType, Exception("Certificate does not contain a \
                                                              %s public key" % cls.__name__)
        return cls(cls.key_from_der(certificate.publicKey), certificate_claim_id)

    def validate_signature(self, message, signature):
        raise NotImplementedError()

    def validate_claim_signature(self, claim, claim_id):
        # check that the claim ids provided are the 64 characters long and hex encoded
        validate_claim_id(claim_id)

        # extract and serialize the stream from the claim, then check the signature

        publisher_signature = claim['publisherSignature']['signature']

        to_sign = "%s%s%s" % (claim_id.decode('hex'),
                              claim.serialized_no_signature,
                              self.certificate_claim_id.decode('hex'))

        digest = hashlib.sha256(to_sign).digest()

        return self.validate_signature(digest, publisher_signature)


class NIST256pValidator(Validator):
    KeyType = 1
    VerifyingType = ecdsa.VerifyingKey

    @staticmethod
    def key_from_der(der):
        return ecdsa.VerifyingKey.from_der(der)

    def validate_signature(self, digest, signature):
        return self.public_key.verify_digest(signature, digest)
