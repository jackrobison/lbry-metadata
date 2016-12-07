from lbryschema.schema.signature import RSASignature, Signature
from lbryschema.schema.cert import Cert
from lbryschema.schema.claim import Claim
from lbryschema.schema.public_key import RSAPublicKey
from lbryschema.utils import pack_sig


def _make_sig(rsa_key, signature):
    rsa_sig = RSASignature.load_from_key_obj(rsa_key, signature)
    _sig = {
        "version": "_0_0_1",
        "rsa": rsa_sig
    }
    return Signature.load(_sig)


def _sign_stream(stream, rsa_key):
    serialized = stream.SerializeToString()
    # What should K be?
    sig = rsa_key.sign(serialized, K=1)[0]
    packed_sig = "".join(pack_sig(sig))
    sig_msg = _make_sig(rsa_key, packed_sig)
    return sig_msg


def sign_stream_claim(claim, rsa_key):
    if isinstance(claim, dict):
        claim = Claim.load(claim)
    signature = _sign_stream(claim, rsa_key)
    msg = {
        "version": "_0_0_1",
        "stream": claim.stream,
        "publisherSignature": signature
    }
    return Claim.load(msg)


def make_cert(rsa_key):
    public_key = RSAPublicKey.load_from_key_obj(rsa_key)
    _cert = {
        "version": "_0_0_1",
        "rsa": public_key
    }
    return Cert.load(_cert)


class _RSASignature(object):
    @staticmethod
    def _pack_sig(sig_long):
        while sig_long:
            yield chr(sig_long & 0xFF)
            sig_long >>= 8

    @staticmethod
    def _make_sig(rsa_key, signature):
        return RSASignature.load_from_key_obj(self._rsa_key, signature)


    def _make_sig(self, signature):
        rsa_sig = RSASignature.load_from_key_obj(self._rsa_key, signature)
        _sig = {
            "version": "_0_0_1",
            "rsa": rsa_sig
        }
        return Signature.load(_sig)


class _RSACertificate(object):


    def __init__(self, rsa_key):
        self._rsa_key = rsa_key
        self._public_key = rsa_key.publickey().exportKey()

    def create_cert(self):
        _cert = {
            "version": "_0_0_1",
            "rsa": self._public_key
        }
        return Cert.load(_cert)


    def _sign_stream(self, stream):
        serialized = stream.SerializeToString()
        # What should K be?
        sig = self._rsa_key.sign(serialized, K=1)[0]
        packed_sig = "".join(self._pack_sig(sig))
        sig_msg = _make_sig(self._rsa_key, packed_sig)
        return sig_msg

    def sign_stream(self, claim):
        if isinstance(claim, dict):
            claim = Claim.load(claim)
        signature = self._sign_stream(claim)
        msg = {
            "version": "_0_0_1",
            "stream": claim.stream,
            "publisherSignature": signature
        }
        return Claim.load(msg)