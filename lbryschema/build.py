from lbryschema.schema.signature import RSASignature, Signature
from lbryschema.schema.cert import Cert
from lbryschema.schema.claim import Claim
from lbryschema.schema.public_key import RSAPublicKey


def _make_sig(rsa_key, signature):
    rsa_sig = RSASignature.load_from_key_obj(rsa_key, signature)
    _sig = {
        "version": "_0_0_1",
        "rsa": rsa_sig
    }
    return Signature.load(_sig)


def _pack_sig(sig_long):
    while sig_long:
        yield chr(sig_long & 0xFF)
        sig_long >>= 8


def _sign_stream(stream, rsa_key):
    serialized = stream.SerializeToString()
    # What should K be?
    sig = rsa_key.sign(serialized, K=1)[0]
    packed_sig = "".join(_pack_sig(sig))
    sig_msg = _make_sig(rsa_key, packed_sig)
    return sig_msg


def sign_stream_claim(claim_dict, rsa_key):
    claim = Claim.load(claim_dict)
    signature = _sign_stream(claim, rsa_key)
    msg = {
        "version": "_0_0_1",
        "stream": claim.stream,
        "publisher_signature": signature
    }
    return Claim.load(msg)


def make_cert(rsa_key):
    public_key = RSAPublicKey.load_from_key_obj(rsa_key)
    _cert = {
        "version": "_0_0_1",
        "rsa": public_key
    }
    return Cert.load(_cert)
