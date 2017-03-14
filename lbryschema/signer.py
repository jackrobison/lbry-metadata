import ecdsa
import hashlib
from lbryschema.encoding import decode_b64_fields
from lbryschema.schema.certificate import Certificate
from lbryschema.schema.claim import Claim
from lbryschema.validator import validate_claim_id
from lbryschema.schema import V_0_0_1, CLAIM_TYPE, CLAIM_TYPES, CERTIFICATE_TYPE, VERSION


class NIST256pSigner(object):
    def __init__(self, private_key):
        self._private_key = private_key

    @property
    def private_key(self):
        return self._private_key

    @property
    def public_key(self):
        return self.private_key.get_verifying_key()

    @property
    def certificate(self):
        certificate_claim = {
            VERSION: V_0_0_1,
            CLAIM_TYPE: CERTIFICATE_TYPE,
            CLAIM_TYPES[CERTIFICATE_TYPE]: Certificate.load_from_key_obj(self.public_key)
        }
        return Claim.load(certificate_claim)

    @classmethod
    def load_pem(cls, pem_string):
        return cls(ecdsa.SigningKey.from_pem(pem_string, hashfunc="sha256"))

    @classmethod
    def generate(cls):
        return cls(ecdsa.SigningKey.generate(curve=ecdsa.NIST256p, hashfunc="sha256"))

    def sign_stream_claim(self, claim, claim_id, cert_claim_id):
        validate_claim_id(claim_id)
        validate_claim_id(cert_claim_id)
        to_sign = "%s%s%s" % (claim_id.decode('hex'),
                              claim.serialized,
                              cert_claim_id.decode('hex'))
        digest = hashlib.sha256(to_sign).digest()

        if isinstance(self.private_key, ecdsa.SigningKey):
            sig = self.private_key.sign_digest_deterministic(digest, hashfunc=hashlib.sha256)
            sig_type = "ECDSA"
        else:
            raise Exception("Unknown key type")

        sig_dict = {
            "version": V_0_0_1,
            "signatureType": sig_type,
            "signature": sig
        }

        msg = {
            "version": V_0_0_1,
            "stream": decode_b64_fields(claim.protobuf_dict)['stream'],
            "publisherSignature": sig_dict
        }

        return Claim.load(msg)
