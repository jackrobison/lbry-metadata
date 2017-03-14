import json
import ecdsa
from copy import deepcopy
from twisted.trial import unittest

from test_data import example_003, example_010, example_010_signed, example_010_ecdsa_cert
from test_data import test_ec_priv_key, fake_stream_claim_id, fake_cert_claim_id
from lbryschema.claim import ClaimDict
from lbryschema.legacy.migrate import migrate
from lbryschema.signer import NIST256pSigner


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


class TestECDSASignatures(UnitTest):
    def test_make_ecdsa_cert(self):
        cert = ClaimDict.generate_certificate(test_ec_priv_key)
        self.assertDictEqual(cert.claim_dict, example_010_ecdsa_cert)

    def test_validate_ecdsa_signature(self):
        cert = ClaimDict.generate_certificate(test_ec_priv_key)
        signed = ClaimDict.load_dict(example_010).sign(test_ec_priv_key,
                                                       fake_stream_claim_id, fake_cert_claim_id)
        self.assertDictEqual(signed.claim_dict, example_010_signed)
        signed_copy = ClaimDict.load_protobuf(signed.protobuf)
        self.assertEquals(signed_copy.validate_signature(fake_stream_claim_id, cert,
                                                         fake_cert_claim_id), True)

    def test_remove_signature_equals_unsigned(self):
        unsigned = ClaimDict.load_dict(example_010)
        signed = unsigned.sign(test_ec_priv_key, fake_stream_claim_id, fake_cert_claim_id)
        self.assertEquals(unsigned.serialized, signed.serialized_no_signature)

    def test_fail_to_validate_fake_ecdsa_signature(self):
        signed = ClaimDict.load_dict(example_010).sign(test_ec_priv_key, fake_stream_claim_id,
                                                       fake_cert_claim_id)
        signed_copy = ClaimDict.load_protobuf(signed.protobuf)
        fake_key = NIST256pSigner.generate().private_key.to_pem()
        fake_cert = ClaimDict.generate_certificate(fake_key)
        self.assertRaises(ecdsa.keys.BadSignatureError, signed_copy.validate_signature,
                          fake_stream_claim_id, fake_cert, fake_cert_claim_id)

    def test_fail_to_validate_ecdsa_sig_for_altered_claim(self):
        cert = ClaimDict.generate_certificate(test_ec_priv_key)
        altered = ClaimDict.load_dict(example_010).sign(test_ec_priv_key, fake_stream_claim_id,
                                                        fake_cert_claim_id)
        sd_hash = altered['stream']['source']['source']
        altered['stream']['source']['source'] = sd_hash[::-1]
        altered_copy = ClaimDict.load_dict(altered.claim_dict)
        self.assertRaises(ecdsa.keys.BadSignatureError, altered_copy.validate_signature,
                          fake_stream_claim_id, cert, fake_cert_claim_id)


class TestMetadata(UnitTest):
    def test_fail_with_fake_sd_hash(self):
        claim = deepcopy(example_010)
        sd_hash = claim['stream']['source']['source'][:-2]
        claim['stream']['source']['source'] = sd_hash
        self.assertRaises(AssertionError, ClaimDict.load_dict, claim)
