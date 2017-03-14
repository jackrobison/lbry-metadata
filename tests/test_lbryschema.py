import json
import ecdsa
from copy import deepcopy
from twisted.trial import unittest

from test_data import example_003, example_010, claim_id_1, claim_id_2
from test_data import nist256p_private_key, claim_010_signed_nist256p, nist256p_cert
from test_data import nist384p_private_key, claim_010_signed_nist384p, nist384p_cert
from test_data import secp256k1_private_key, claim_010_signed_secp256k1, secp256k1_cert
from lbryschema.claim import ClaimDict
from lbryschema.schema import NIST256p, NIST384p, SECP256k1
from lbryschema.legacy.migrate import migrate
from lbryschema.signer import get_signer


class UnitTest(unittest.TestCase):
    maxDiff = 4000


class TestEncoderAndDecoder(UnitTest):
    def test_encode_decode(self):
        test_claim = ClaimDict.load_dict(example_010)
        self.assertDictEqual(test_claim.claim_dict, example_010)
        test_pb = test_claim.protobuf
        self.assertDictEqual(ClaimDict.load_protobuf(test_pb).claim_dict, example_010)
        self.assertEquals(test_pb.ByteSize(), ClaimDict.load_protobuf(test_pb).protobuf_len)
        self.assertEquals(test_claim.json_len, ClaimDict.load_protobuf(test_pb).json_len)


class TestMigration(UnitTest):
    def test_migrate_to_010(self):
        migrated_0_1_0 = migrate(example_003)
        self.assertDictEqual(migrated_0_1_0.claim_dict, example_010)


class TestNIST256pSignatures(UnitTest):
    def test_make_ecdsa_cert(self):
        cert = ClaimDict.generate_certificate(nist256p_private_key, curve=NIST256p)
        self.assertDictEqual(cert.claim_dict, nist256p_cert)

    def test_validate_ecdsa_signature(self):
        cert = ClaimDict.generate_certificate(nist256p_private_key, curve=NIST256p)
        signed = ClaimDict.load_dict(example_010).sign(nist256p_private_key,
                                                       claim_id_1, claim_id_2, curve=NIST256p)
        self.assertDictEqual(signed.claim_dict, claim_010_signed_nist256p)
        signed_copy = ClaimDict.load_protobuf(signed.protobuf)
        self.assertEquals(signed_copy.validate_signature(claim_id_1, cert,
                                                         claim_id_2), True)

    def test_remove_signature_equals_unsigned(self):
        unsigned = ClaimDict.load_dict(example_010)
        signed = unsigned.sign(nist256p_private_key, claim_id_1, claim_id_2, curve=NIST256p)
        self.assertEquals(unsigned.serialized, signed.serialized_no_signature)

    def test_fail_to_validate_fake_ecdsa_signature(self):
        signed = ClaimDict.load_dict(example_010).sign(nist256p_private_key, claim_id_1,
                                                       claim_id_2, curve=NIST256p)
        signed_copy = ClaimDict.load_protobuf(signed.protobuf)
        fake_key = get_signer(NIST256p).generate().private_key.to_pem()
        fake_cert = ClaimDict.generate_certificate(fake_key, curve=NIST256p)
        self.assertRaises(ecdsa.keys.BadSignatureError, signed_copy.validate_signature,
                          claim_id_1, fake_cert, claim_id_2)

    def test_fail_to_validate_ecdsa_sig_for_altered_claim(self):
        cert = ClaimDict.generate_certificate(nist256p_private_key, curve=NIST256p)
        altered = ClaimDict.load_dict(example_010).sign(nist256p_private_key, claim_id_1,
                                                        claim_id_2, curve=NIST256p)
        sd_hash = altered['stream']['source']['source']
        altered['stream']['source']['source'] = sd_hash[::-1]
        altered_copy = ClaimDict.load_dict(altered.claim_dict)
        self.assertRaises(ecdsa.keys.BadSignatureError, altered_copy.validate_signature,
                          claim_id_1, cert, claim_id_2)


class TestNIST384pSignatures(UnitTest):
    def test_make_ecdsa_cert(self):
        cert = ClaimDict.generate_certificate(nist384p_private_key, curve=NIST384p)
        self.assertDictEqual(cert.claim_dict, nist384p_cert)

    def test_validate_ecdsa_signature(self):
        cert = ClaimDict.generate_certificate(nist384p_private_key, curve=NIST384p)
        signed = ClaimDict.load_dict(example_010).sign(nist384p_private_key,
                                                       claim_id_1, claim_id_2, curve=NIST384p)
        self.assertDictEqual(signed.claim_dict, claim_010_signed_nist384p)
        signed_copy = ClaimDict.load_protobuf(signed.protobuf)
        self.assertEquals(signed_copy.validate_signature(claim_id_1, cert,
                                                         claim_id_2), True)

    def test_remove_signature_equals_unsigned(self):
        unsigned = ClaimDict.load_dict(example_010)
        signed = unsigned.sign(nist384p_private_key, claim_id_1, claim_id_2, curve=NIST384p)
        self.assertEquals(unsigned.serialized, signed.serialized_no_signature)

    def test_fail_to_validate_fake_ecdsa_signature(self):
        signed = ClaimDict.load_dict(example_010).sign(nist384p_private_key, claim_id_1,
                                                       claim_id_2, curve=NIST384p)
        signed_copy = ClaimDict.load_protobuf(signed.protobuf)
        fake_key = get_signer(NIST384p).generate().private_key.to_pem()
        fake_cert = ClaimDict.generate_certificate(fake_key, curve=NIST384p)
        self.assertRaises(ecdsa.keys.BadSignatureError, signed_copy.validate_signature,
                          claim_id_1, fake_cert, claim_id_2)

    def test_fail_to_validate_ecdsa_sig_for_altered_claim(self):
        cert = ClaimDict.generate_certificate(nist384p_private_key, curve=NIST384p)
        altered = ClaimDict.load_dict(example_010).sign(nist384p_private_key, claim_id_1,
                                                        claim_id_2, curve=NIST384p)
        sd_hash = altered['stream']['source']['source']
        altered['stream']['source']['source'] = sd_hash[::-1]
        altered_copy = ClaimDict.load_dict(altered.claim_dict)
        self.assertRaises(ecdsa.keys.BadSignatureError, altered_copy.validate_signature,
                          claim_id_1, cert, claim_id_2)


class TestSECP256k1Signatures(UnitTest):
    def test_make_ecdsa_cert(self):
        cert = ClaimDict.generate_certificate(secp256k1_private_key, curve=SECP256k1)
        self.assertDictEqual(cert.claim_dict, secp256k1_cert)

    def test_validate_ecdsa_signature(self):
        cert = ClaimDict.generate_certificate(secp256k1_private_key, curve=SECP256k1)
        signed = ClaimDict.load_dict(example_010).sign(secp256k1_private_key,
                                                       claim_id_1, claim_id_2, curve=SECP256k1)
        self.assertDictEqual(signed.claim_dict, claim_010_signed_secp256k1)
        signed_copy = ClaimDict.load_protobuf(signed.protobuf)
        self.assertEquals(signed_copy.validate_signature(claim_id_1, cert,
                                                         claim_id_2), True)

    def test_remove_signature_equals_unsigned(self):
        unsigned = ClaimDict.load_dict(example_010)
        signed = unsigned.sign(secp256k1_private_key, claim_id_1, claim_id_2, curve=SECP256k1)
        self.assertEquals(unsigned.serialized, signed.serialized_no_signature)

    def test_fail_to_validate_fake_ecdsa_signature(self):
        signed = ClaimDict.load_dict(example_010).sign(secp256k1_private_key, claim_id_1,
                                                       claim_id_2, curve=SECP256k1)
        signed_copy = ClaimDict.load_protobuf(signed.protobuf)
        fake_key = get_signer(SECP256k1).generate().private_key.to_pem()
        fake_cert = ClaimDict.generate_certificate(fake_key, curve=SECP256k1)
        self.assertRaises(ecdsa.keys.BadSignatureError, signed_copy.validate_signature,
                          claim_id_1, fake_cert, claim_id_2)

    def test_fail_to_validate_ecdsa_sig_for_altered_claim(self):
        cert = ClaimDict.generate_certificate(secp256k1_private_key, curve=SECP256k1)
        altered = ClaimDict.load_dict(example_010).sign(secp256k1_private_key, claim_id_1,
                                                        claim_id_2, curve=SECP256k1)
        sd_hash = altered['stream']['source']['source']
        altered['stream']['source']['source'] = sd_hash[::-1]
        altered_copy = ClaimDict.load_dict(altered.claim_dict)
        self.assertRaises(ecdsa.keys.BadSignatureError, altered_copy.validate_signature,
                          claim_id_1, cert, claim_id_2)


class TestMetadata(UnitTest):
    def test_fail_with_fake_sd_hash(self):
        claim = deepcopy(example_010)
        sd_hash = claim['stream']['source']['source'][:-2]
        claim['stream']['source']['source'] = sd_hash
        self.assertRaises(AssertionError, ClaimDict.load_dict, claim)
