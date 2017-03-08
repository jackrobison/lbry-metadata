from twisted.trial import unittest
import json
import ecdsa
from copy import deepcopy
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from google.protobuf import json_format
from lbryschema.schema.claim import Claim
from lbryschema.schema.claim_pb2 import Claim as ClaimPB
from lbryschema.validate import validate_signed_stream_claim, make_cert, sign_stream_claim
from lbryschema.legacy.migrate import migrate_003_to_010


test_rsa_key = \
"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEApPqDTeeVO2ZeI/jxcgbFcndhzvEqmKW7Et+cQLdhJNhQR9hA
Y/39m6qsuFEJnwyonPRgDWj05dgv3soS7uTeR6BQoVZlHVX1NLdLMHaDBVUwDp1G
rbSnOmlqpjp3kOFVgHTaJk3g4p+eLDpZ3wzSqyOx/O375MI+v0+D8NLcnhWMWmeA
ph6wszYjuEvXoPr+D47pN+JFVAcvj3Rpm3qDpZ214Tn7QuGBhjIzbfTa3C/QJNqW
vHLkJTvcWZhY5uyt1aDS7ID6jpDsAAYLmszf4KTzF2CtlnEo1S4HLONtetKjr6CL
1jYvxlKlYsY9mvTCYEa+7YgdnGH9Gl5o9CBbxwIDAQABAoIBAB+/pe0kF+/qb0t0
6OIMs4qntsbgWlYt7qZfKe66W5N/nVN2Jk4X3upKGhsOXU+iXAB4dtOd0yM4S14Q
fTxEBxK5o0qpGaRfmmSesXWOGQC5uBnX4nYjQdtX1hJPRhs3ggDKfADLE/AIz6Or
RwhJq3EL2YDXO5Z2WyTt5HI/4fz50Xr477mcW+E0cCdemlsqvSmXCLbCj4gbyeCr
WbmDZ7usKx3TMbM7R7HbpblBiLkpBEAXDS241AgTtzSp7b+0lixs8UW98d8O+658
F74xASoQygJ/gVrE9GAEGIX4kNyszpiUfiP+E3m75pb9yNkthnC2+k+KDe/5nBYB
UefF58ECgYEAx5tyoOuxCC86q6vRjLK+qo+4irlYETAqXar196pabFVhgIWbqGDz
tACzBioSxiM1pUsRspcweOlfeN8G0V4X85mklsO9+cB4sjBF3cZGtUvqpz0le5+y
/N8m49s9aB8mugJ+kJCLLpcHpiFZLGkxW6BUrGo3w27yKRsTpkokJskCgYEA05aO
B4rEQqscUwdjR7ppn/ndoTK4hKD+eXbwty575P4mzFXjWNdvaGnnmVBm3yl5h6Gd
GkkGTQMIAOdDITLhwubAR8vktLUR6xsu4WGz5Asl3/ZLB9wlYoCx9MDw/D1Fizij
1ZbGYJb9C7NU4ANF4q9vSnwUkIkH+01e5eEeZg8CgYEAwquMQ/0Zjs3g/oR3viyl
X1sDs+fHSBwddXTCpmRyA63RhbLIeJL1mtwDvUNTRAIa07Y+8FobYBDal9uLnq2R
1nZF2vPUV7uq+r2xpfU2CKKdm7U61TKPMafBGgA8B0w6TLcaEIun8ixBvXhQq8t7
48yeR/jfoa6WZhiONWOhlmECgYBJQIlBYTBbKGQw9pDPh2EECnxJT4cEG7yeDqh9
srEf8UE7YszHuCYQzwFoWaaTwgcaBsCeFgQBa3g839OkzbnNQRf2g0dVrI5ch9eu
HaYq4BUnuVv2h6fFt2pkotuLaCcIcP5/dqiNThijEV3kBB4Qwc3UyqpP87D4tquR
CGP+zwKBgDgIMwgo7R6gMeTBZOp1FpiHVPqfSRAw14PRA6cJ4/2qZqy30+z80X8G
EoBDqaaQMiP4DAKqzrHjAB4YzdHJ+ZYudWtW3q2yK969fs8O4x6j9vImf+/8Imrb
AsNxmHFyxPqs+TQoNmfxfx00kQhdgBRDs8DzsWgA1TOZ5ZKCTYiT
-----END RSA PRIVATE KEY-----"""

fake_stream_claim_id = "aa04a949348f9f094d503e5816f0cfb57ee68a22f6d08d149217d071243e0378"
fake_cert_claim_id = "26ccfc3c4b21d1a6d07e6ff674e5038d3c290df974f3a2a4cb721996f7c882ba"

example_010_rsa_cert = {
  "publicKey": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApPqDTeeVO2ZeI/jxcgbFcndhzvEqmKW7Et+cQLdhJNhQR9hAY/39m6qsuFEJnwyonPRgDWj05dgv3soS7uTeR6BQoVZlHVX1NLdLMHaDBVUwDp1GrbSnOmlqpjp3kOFVgHTaJk3g4p+eLDpZ3wzSqyOx/O375MI+v0+D8NLcnhWMWmeAph6wszYjuEvXoPr+D47pN+JFVAcvj3Rpm3qDpZ214Tn7QuGBhjIzbfTa3C/QJNqWvHLkJTvcWZhY5uyt1aDS7ID6jpDsAAYLmszf4KTzF2CtlnEo1S4HLONtetKjr6CL1jYvxlKlYsY9mvTCYEa+7YgdnGH9Gl5o9CBbxwIDAQAB",
  "keyType": "RSA",
  "version": "_0_0_1"
}

example_003 = {
    'author': 'Dr Comet',
    'content_type': 'image/jpeg',
    'description': 'Sexy catgirl posing outdoors.',
    'language': 'en',
    'license': 'Creative Commons Attribution 3.0 United States',
    'license_url': 'https://creativecommons.org/licenses/by/3.0/us/legalcode',
    'nsfw': True,
    'sources': {
        'lbry_sd_hash': '2d1a78159a6da90f704daa96a44fa68e71340da9ab8d17943148819273e23da37e23b6ffe0794448225c199e97a83bf4',
    },
    'thumbnail': 'http://i.imgur.com/Q0lZZHX.jpg',
    'title': 'Sexy Catgirl',
    'ver': '0.0.3'
}

example_010 = {
  "version": "_0_0_1",
  "claimType": "streamClaim",
  "stream": {
    "source": {
      "source": "LRp4FZptqQ9wTaqWpE+mjnE0DamrjReUMUiBknPiPaN+I7b/4HlESCJcGZ6XqDv0",
      "version": "_0_0_1",
      "contentType": "image/jpeg",
      "sourceType": "lbry_sd_hash"
    },
    "version": "_0_0_1",
    "metadata": {
      "description": "Sexy catgirl posing outdoors.",
      "license": "Creative Commons Attribution 3.0 United States",
      "author": "Dr Comet",
      "title": "Sexy Catgirl",
      "language": "en",
      "version": "_0_1_0",
      "nsfw": True,
      "thumbnail": "http://i.imgur.com/Q0lZZHX.jpg"
    }
  }
}

example_010_signed = {
  "version": "_0_0_1",
  "publisherSignature": {
    "signatureType": "RSA",
    "version": "_0_0_1",
    "signature": "bnke3qdvbmBBkW2vVnNVK6S/VwP7JUDN8FxB72s1SoFNLN1Mq9F55QDOtLxokRBtfzLDgfX0MfWP005Br8195xnBOi5qgxCBym34G/UkyLSc0MDf3j6djRXOs4SWVS636yA4sdv8stCI3id5dbQiP/F8trYKQsFlp012eieNchvRJ1cy+eHJ81PRaSrlWM/FHu5rYLOZSfWliUCc2scHQcduFKqCdHSNH5bX5WxVGxy/wbLddsTxq/JOU0ryp3viAIhlciM4qEM5X6VsVBubTaLDpYdF8/Dj0G23AO4pdHIq4ye7kva0e/Y8+FlM0gqdHLQRKiBVhYNOC01+Q4g+Aw=="
  },
  "claimType": "streamClaim",
  "stream": {
    "source": {
      "source": "LRp4FZptqQ9wTaqWpE+mjnE0DamrjReUMUiBknPiPaN+I7b/4HlESCJcGZ6XqDv0",
      "version": "_0_0_1",
      "contentType": "image/jpeg",
      "sourceType": "lbry_sd_hash"
    },
    "version": "_0_0_1",
    "metadata": {
      "description": "Sexy catgirl posing outdoors.",
      "license": "Creative Commons Attribution 3.0 United States",
      "author": "Dr Comet",
      "title": "Sexy Catgirl",
      "language": "en",
      "version": "_0_1_0",
      "nsfw": True,
      "thumbnail": "http://i.imgur.com/Q0lZZHX.jpg"
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


class TestRSASignatures(UnitTest):
    def test_make_rsa_cert(self):
        key = RSA.importKey(test_rsa_key)
        cert = make_cert(key)
        cert_dict = json.loads(json_format.MessageToJson(cert))
        self.assertDictEqual(cert_dict, example_010_rsa_cert)

    def test_validate_rsa_signature(self):
        key = RSA.importKey(test_rsa_key)
        cert = make_cert(key)
        migrated_0_1_0_proto = migrate_003_to_010(example_003)
        signed = sign_stream_claim(migrated_0_1_0_proto, fake_stream_claim_id,
                                   key, fake_cert_claim_id)
        self.assertEquals(validate_signed_stream_claim(signed, fake_stream_claim_id,
                                                       cert, fake_cert_claim_id), True)

    def test_fail_to_validate_fake_rsa_signature(self):
        real_key = RSA.importKey(test_rsa_key)
        fake_cert = make_cert(RSA.generate(2048))
        migrated_0_1_0_proto = migrate_003_to_010(example_003)
        signed = sign_stream_claim(migrated_0_1_0_proto, fake_stream_claim_id,
                                   real_key, fake_cert_claim_id)
        self.assertEquals(validate_signed_stream_claim(signed, fake_stream_claim_id,
                                                       fake_cert, fake_cert_claim_id), False)

    def test_fail_to_validate_rsa_sig_for_altered_claim(self):
        key = RSA.importKey(test_rsa_key)
        cert = make_cert(key)
        migrated_0_1_0_proto = migrate_003_to_010(example_003)
        signed = sign_stream_claim(migrated_0_1_0_proto, fake_stream_claim_id,
                                   key, fake_cert_claim_id)
        signed_dict = json.loads(json_format.MessageToJson(signed))
        sd_hash = signed_dict['stream']['source']['source']
        signed_dict['stream']['source']['source'] = sd_hash[::-1]
        altered_json = json.dumps(signed_dict)
        altered_pb = json_format.Parse(altered_json, ClaimPB())
        self.assertEquals(validate_signed_stream_claim(altered_pb, fake_stream_claim_id,
                                                       cert, fake_cert_claim_id), False)


class TestMetadata(UnitTest):
    def test_fail_to_validate_with_fake_sd_hash(self):
        claim = deepcopy(example_010)
        sd_hash = claim['stream']['source']['source'][:-1]
        claim['stream']['source']['source'] = sd_hash
        claim_with_short_sd_hash = json.dumps(claim)
        self.assertRaises(json_format.ParseError,
                          json_format.Parse, claim_with_short_sd_hash, ClaimPB())


# key = ecdsa.SigningKey.generate(ecdsa.NIST256p, hashfunc='sha256')
# cert = make_cert(key)
# print "Made cert: ", json_format.MessageToJson(cert)
#
# migrated_0_1_0_proto = migrate_003_to_010(example_003)
# signed = sign_stream_claim(migrated_0_1_0_proto, fake_stream_claim_id,
#                            key, fake_cert_claim_id)
# print " *" * 10
# print json_format.MessageToJson(signed)
# print " *" * 10
# validate_signed_stream_claim(signed, fake_stream_claim_id,
#                              cert, fake_cert_claim_id)
# print "json 0.0.3 stream claim: %i bytes" % len(json.dumps(example_003))
# print "pb 0.1.0 stream claim: %i bytes" % len(signed.SerializeToString())
