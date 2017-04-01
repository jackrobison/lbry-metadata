import json
import os

from lbryschema.legacy import migrate
from lbryschema.claim import ClaimDict
from lbryschema.schema import NIST256p, NIST384p, SECP256k1
from lbryschema.signer import get_signer

unmigrated_003 = {
    'author': 'Samuel Bryan',
    'content_type': 'video/mp4',
    'description': 'What is LBRY? An introduction with Alex Tabarrok',
    'language': 'en',
    'license': 'LBRY Inc',
    'nsfw': False,
    'sources': {
        'lbry_sd_hash': 'd5169241150022f996fa7cd6a9a1c421937276a3275eb912790bd07ba7aec1fac5fd45431d226b8fb402691e79aeb24b',
    },
    'thumbnail': 'https://s3.amazonaws.com/files.lbry.io/logo.png',
    'title': 'What is LBRY?',
    'ver': '0.0.3'
}

cert_claim_id = "63f2da17b0d90042c559cc73b6b17f853945c43e"
stream_claim_address = "bDtL6qriyimxz71DSYjojTBsm6cpM1bqmj"
stream_claim_address_2 = "bUG7VaMzLEqqyZQAyg9srxQzvf1wwnJ48w"

claim_010_unsigned = migrate.migrate(unmigrated_003)


# NIST256p test data
nist256p_private_key = get_signer(NIST256p).generate().private_key.to_pem()
claim_010_signed_nist256p = claim_010_unsigned.sign(nist256p_private_key,
                                                     stream_claim_address,
                                                     cert_claim_id,
                                                     curve=NIST256p)
nist256p_cert = ClaimDict.generate_certificate(nist256p_private_key, curve=NIST256p)

# NIST384p test data
nist384p_private_key = get_signer(NIST384p).generate().private_key.to_pem()
claim_010_signed_nist384p = claim_010_unsigned.sign(nist384p_private_key,
                                                     stream_claim_address,
                                                     cert_claim_id,
                                                     curve=NIST384p)
nist384p_cert = ClaimDict.generate_certificate(nist384p_private_key, curve=NIST384p)

# SECP256k1 test data
secp256k1_private_key = get_signer(SECP256k1).generate().private_key.to_pem()
claim_010_signed_secp256k1 = claim_010_unsigned.sign(secp256k1_private_key,
                                                     stream_claim_address,
                                                     cert_claim_id,
                                                     curve=SECP256k1)
secp256k1_cert = ClaimDict.generate_certificate(secp256k1_private_key, curve=SECP256k1)


formatted = lambda x: json.dumps(x.claim_dict, indent=2)

template = """

claim_id_1 = \"%s\"

claim_address_2 = \"%s\"

claim_address_1 = \"%s\"

nist256p_private_key = \"\"\"%s\"\"\"

nist384p_private_key = \"\"\"%s\"\"\"

secp256k1_private_key = \"\"\"%s\"\"\"

nist256p_cert = %s

nist384p_cert = %s

secp256k1_cert = %s

example_003 = %s

example_010 = %s

example_010_serialized = \"%s\"

claim_010_signed_nist256p = %s

claim_010_signed_nist384p = %s

claim_010_signed_secp256k1 = %s
"""

test_data = template % (cert_claim_id,
                        stream_claim_address,
                        stream_claim_address_2,
                        nist256p_private_key,
                        nist384p_private_key,
                        secp256k1_private_key,
                        formatted(nist256p_cert),
                        formatted(nist384p_cert),
                        formatted(secp256k1_cert),
                        json.dumps(unmigrated_003, indent=2),
                        formatted(claim_010_unsigned),
                        claim_010_unsigned.serialized.encode('hex'),
                        formatted(claim_010_signed_nist256p),
                        formatted(claim_010_signed_nist384p),
                        formatted(claim_010_signed_secp256k1))

test_data = test_data.replace("false", "False")
tests_data_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    "tests", "test_data.py")

with open(tests_data_file_path, "w") as tests_data_file:
    tests_data_file.write(test_data)
