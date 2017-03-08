import ecdsa
import hashlib
from lbryschema.schema.signature import Signature
from lbryschema.schema.cert import Cert
from lbryschema.schema.claim import Claim
from lbryschema.validator import validate_claim_id
from lbryschema.utils import V_0_0_1


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
        return Cert.load_from_key_obj(self.public_key)

    @classmethod
    def load_pem(cls, pem_string):
        return cls(ecdsa.SigningKey.from_pem(pem_string, hashfunc="sha256"))

    @classmethod
    def generate(cls):
        return cls(ecdsa.SigningKey.generate(curve=ecdsa.NIST256p, hashfunc="sha256"))

    def sign_stream_claim(self, claim, claim_id, cert_claim_id):
        if isinstance(claim, dict):
            claim = Claim.load(claim)

        validate_claim_id(claim_id)
        validate_claim_id(cert_claim_id)
        serialized = claim.SerializeToString()
        to_sign = "%s%s%s" % (claim_id, serialized, cert_claim_id)
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
        sig_pb = Signature.load(sig_dict)

        msg = {
            "version": V_0_0_1,
            "stream": claim.stream,
            "publisherSignature": sig_pb
        }
        return Claim.load(msg)
