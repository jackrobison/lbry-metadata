from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA256

from lbryschema.schema.signature import Signature
from lbryschema.schema.cert import Cert
from lbryschema.schema.claim import Claim
from lbryschema.schema.public_key import PublicKey


def _make_sig(signature):
    _sig = {
        "version": "_0_0_1",
        "signatureType": "RSA",
        "signature": signature
    }
    return Signature.load(_sig)


def _sign_stream(stream, claim_id, rsa_key, cert_claim_id):
    validate_claim_id(claim_id)
    validate_claim_id(cert_claim_id)

    serialized = stream.SerializeToString()

    h = SHA256.new()
    h.update(claim_id)
    h.update(serialized)
    h.update(cert_claim_id)

    signer = PKCS1_PSS.new(rsa_key)
    sig = signer.sign(h)
    sig_msg = _make_sig(sig)
    return sig_msg


def sign_stream_claim(claim, claim_id, rsa_key, cert_claim_id):
    if isinstance(claim, dict):
        claim = Claim.load(claim)
    signature = _sign_stream(claim, claim_id, rsa_key, cert_claim_id)
    msg = {
        "version": "_0_0_1",
        "stream": claim.stream,
        "publisherSignature": signature
    }
    return Claim.load(msg)


def make_cert(rsa_key):
    public_key = PublicKey.load_from_key_obj(rsa_key)
    _cert = {
        "version": "_0_0_1",
        "keyType": "RSA",
        "publicKey": public_key
    }
    return Cert.load(_cert)


def validate_claim_id(claim_id):
    hex_chars = "0123456789abcdefABCDEF"
    assert len(claim_id) == 64, "Incorrect claimid length: %i" % len(claim_id)
    for c in claim_id:
        assert c in hex_chars, "Claim id is not hex encoded"


def validate_signed_stream_claim(claim, claim_id, cert, cert_id):
    # check that the claim ids provided are the 64 characters long and hex encoded
    validate_claim_id(claim_id)
    validate_claim_id(cert_id)

    # extract and serialize the stream from the claim, then check the signature
    cert_public_key = cert.publicKey.publicKey
    key = RSA.importKey(cert_public_key)
    publisher_signature = claim.publisherSignature.signature
    _temp_claim_dict = {
        "version": "_0_0_1",
        "stream": claim.stream
    }
    _temp_claim = Claim.load(_temp_claim_dict)
    msg = _temp_claim.SerializeToString()

    h = SHA256.new()
    h.update(claim_id)
    h.update(msg)
    h.update(cert_id)

    verifier = PKCS1_PSS.new(key)
    return verifier.verify(h, publisher_signature)
