from twisted.trial import unittest
import json
import ecdsa
from copy import deepcopy
from google.protobuf import json_format
from lbryschema.schema.claim import Claim
from lbryschema.schema.claim_pb2 import Claim as ClaimPB
from lbryschema.validator import NIST256pValidator
from lbryschema.signer import NIST256pSigner
from lbryschema.legacy.migrate import migrate_003_to_010

test_ec_priv_key = \
"""-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIA0pP1+zwmzDiImsh6i0z21CB4rjbKD9tejhc1v/61jYoAoGCCqGSM49
AwEHoUQDQgAE71RLHfb3dtV3tYP7fRmmHKqYBpstNbthEjV6XFvyV+zZrUKwUEr3
I8l/VpxKQIrFYstOcRuRAOwTqLVeaDW/nQ==
-----END EC PRIVATE KEY-----"""

test_ec_pub_key = \
"""
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE71RLHfb3dtV3tYP7fRmmHKqYBpst
NbthEjV6XFvyV+zZrUKwUEr3I8l/VpxKQIrFYstOcRuRAOwTqLVeaDW/nQ==
-----END PUBLIC KEY-----"""


fake_stream_claim_id = "aa04a949348f9f094d503e5816f0cfb57ee68a22f6d08d149217d071243e0378"
fake_cert_claim_id = "26ccfc3c4b21d1a6d07e6ff674e5038d3c290df974f3a2a4cb721996f7c882ba"

example_010_ecdsa_cert = {
  "publicKey": "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE71RLHfb3dtV3tYP7fRmmHKqYBpstNbthEjV6XFvyV+zZrUKwUEr3I8l/VpxKQIrFYstOcRuRAOwTqLVeaDW/nQ==",
  "keyType": "ECDSA",
  "version": "_0_0_1"
}

example_003 = {
    'author': 'Fake author',
    'content_type': 'fake/type',
    'description': '...',
    'language': 'en',
    'license': 'Creative Commons Attribution 3.0 United States',
    'license_url': 'https://creativecommons.org/licenses/by/3.0/us/legalcode',
    'nsfw': False,
    'sources': {
        'lbry_sd_hash': '2d1a78159a6da90f704daa96a44fa68e71340da9ab8d17943148819273e23da37e23b6ffe0794448225c199e97a83bf4',
    },
    'thumbnail': 'lbry.io',
    'title': 'Fake title',
    'ver': '0.0.3'
}

example_010 = {
  "version": "_0_0_1",
  "claimType": "streamClaim",
  "stream": {
    "source": {
      "source": "LRp4FZptqQ9wTaqWpE+mjnE0DamrjReUMUiBknPiPaN+I7b/4HlESCJcGZ6XqDv0",
      "version": "_0_0_1",
      "contentType": "fake/type",
      "sourceType": "lbry_sd_hash"
    },
    "version": "_0_0_1",
    "metadata": {
      "description": "...",
      "license": "Creative Commons Attribution 3.0 United States",
      "author": "Fake author",
      "title": "Fake title",
      "language": "en",
      "version": "_0_1_0",
      "nsfw": False,
      "thumbnail": "lbry.io"
    }
  }
}

example_010_signed = {
  "version": "_0_0_1",
  "publisherSignature": {
    "signatureType": "ECDSA",
    "version": "_0_0_1",
    "signature": "mmznfj/WhIiHbsBRifivDeWwaRjfnZMF0dTbk8Z1syiZJ7SHtdZf51fAu7FtAawkfmN5qUwtx2k1VUGPlboZFw=="
  },
  "claimType": "streamClaim",
  "stream": {
    "source": {
      "source": "LRp4FZptqQ9wTaqWpE+mjnE0DamrjReUMUiBknPiPaN+I7b/4HlESCJcGZ6XqDv0",
      "version": "_0_0_1",
      "contentType": "fake/type",
      "sourceType": "lbry_sd_hash"
    },
    "version": "_0_0_1",
    "metadata": {
      "description": "...",
      "license": "Creative Commons Attribution 3.0 United States",
      "author": "Fake author",
      "title": "Fake title",
      "language": "en",
      "version": "_0_1_0",
      "nsfw": False,
      "thumbnail": "lbry.io"
    }
  }
}


class UnitTest(unittest.TestCase):
    maxDiff = 4000


class TestEncoderAndDecoder(UnitTest):
    def test_encode_decode(self):
        test_pb = Claim.load(example_010)
        decoded_dict = json.loads(json_format.MessageToJson(test_pb))
        self.assertDictEqual(decoded_dict, example_010)
        claim_string = json.dumps(decoded_dict)
        back_to_pb = json_format.Parse(claim_string, ClaimPB())
        pb_back_to_dict = json.loads(json_format.MessageToJson(back_to_pb))
        self.assertDictEqual(pb_back_to_dict, example_010)


class TestMigration(UnitTest):
    def test_migrate_to_010(self):
        migrated_0_1_0_proto = migrate_003_to_010(example_003)
        migrated_0_1_0_json = json_format.MessageToJson(migrated_0_1_0_proto)
        migrated_dict = json.loads(migrated_0_1_0_json)
        self.assertDictEqual(migrated_dict, example_010)


class TestECDSASignatures(UnitTest):
    def test_make_ecdsa_cert(self):
        signer = NIST256pSigner.load_pem(test_ec_priv_key)
        cert_dict = json.loads(json_format.MessageToJson(signer.certificate))
        self.assertDictEqual(cert_dict, example_010_ecdsa_cert)

    def test_validate_ecdsa_signature(self):
        signer = NIST256pSigner.load_pem(test_ec_priv_key)
        migrated_0_1_0_proto = migrate_003_to_010(example_003)
        signed = signer.sign_stream_claim(migrated_0_1_0_proto,
                                          fake_stream_claim_id,
                                          fake_cert_claim_id)
        validator = NIST256pValidator.load_from_certificate(signer.certificate, fake_cert_claim_id)
        self.assertEquals(validator.validate_claim_signature(signed, fake_stream_claim_id), True)

    def test_fail_to_validate_fake_ecdsa_signature(self):
        signer = NIST256pSigner.load_pem(test_ec_priv_key)
        migrated_0_1_0_proto = migrate_003_to_010(example_003)
        signed = signer.sign_stream_claim(migrated_0_1_0_proto,
                                          fake_stream_claim_id,
                                          fake_cert_claim_id)
        fake_signer = NIST256pSigner.generate()
        bad_validator = NIST256pValidator.load_from_certificate(fake_signer.certificate,
                                                            fake_cert_claim_id)
        self.assertRaises(ecdsa.keys.BadSignatureError, bad_validator.validate_claim_signature,
                          signed, fake_stream_claim_id)

    def test_fail_to_validate_ecdsa_sig_for_altered_claim(self):
        signer = NIST256pSigner.load_pem(test_ec_priv_key)
        migrated_0_1_0_proto = migrate_003_to_010(example_003)
        signed = signer.sign_stream_claim(migrated_0_1_0_proto,
                                          fake_stream_claim_id,
                                          fake_cert_claim_id)

        signed_dict = json.loads(json_format.MessageToJson(signed))
        sd_hash = signed_dict['stream']['source']['source']
        signed_dict['stream']['source']['source'] = sd_hash[::-1]
        altered_json = json.dumps(signed_dict)
        altered_pb = json_format.Parse(altered_json, ClaimPB())

        validator = NIST256pValidator.load_from_certificate(signer.certificate, fake_cert_claim_id)
        self.assertRaises(ecdsa.keys.BadSignatureError, validator.validate_claim_signature,
                          altered_pb, fake_stream_claim_id)


class TestMetadata(UnitTest):
    def test_fail_to_validate_with_fake_sd_hash(self):
        claim = deepcopy(example_010)
        sd_hash = claim['stream']['source']['source'][:-1]
        claim['stream']['source']['source'] = sd_hash
        claim_with_short_sd_hash = json.dumps(claim)
        self.assertRaises(json_format.ParseError,
                          json_format.Parse, claim_with_short_sd_hash, ClaimPB())
