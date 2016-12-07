from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from lbryschema.schema.claim import Claim
from lbryschema.utils import unpack_sig


def validate_signed_stream_claim(claim, cert):
    # check pub key hashes match
    stream_pub_key_hash = claim.publisherSignature.signature.publicKeyHash
    cert_pub_key_hash = cert.publicKey.publicKeyHash
    if not stream_pub_key_hash == cert_pub_key_hash:
        return False

    # check that the public key hash is actually the hash of the public key
    cert_public_key = cert.publicKey.publicKey
    key_hash = SHA256.new(cert_public_key).digest()
    if not key_hash == stream_pub_key_hash:
        return False

    # extract and serialize the stream from the claim, then check the signature
    key = RSA.importKey(cert_public_key)
    stream = claim.stream
    publisher_signature = bytearray(claim.publisherSignature.signature.signature)
    _temp_claim_dict = {
        "version": "_0_0_1",
        "stream": stream
    }
    _temp_claim = Claim.load(_temp_claim_dict)
    msg = _temp_claim.SerializeToString()
    return key.verify(msg, unpack_sig(publisher_signature[::-1]))
