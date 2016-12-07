import os
import json
from Crypto.PublicKey import RSA
from google.protobuf import json_format
from lbryschema.schema.claim import Claim
from lbryschema.validate import validate_signed_stream_claim
from lbryschema.build import make_cert, sign_stream_claim
from lbryschema.migrate import migrate_003_to_010


def generate_key(data_dir, name, password):
    key_path = os.path.join(data_dir, "%s.pem" % name)
    key = RSA.generate(2048)
    with open(key_path, "w") as key_file:
        key_file.writelines(key.exportKey(passphrase=password))
    return key


def load_key(data_dir, name, password):
    key_path = os.path.join(data_dir, "%s.pem" % name)
    if not os.path.isfile(key_path):
        return generate_key(data_dir, name, password)
    with open(key_path, "r") as key_file:
        key = RSA.importKey(key_file.read(), passphrase=password)
    return key

data_dir = "/Users/johnrobison/Library/Application Support/LBRY"


key = load_key(data_dir, "jack", 'password')

cd = {
    'version': '_0_0_1',
    'stream': {
        'version': '_0_0_1',
        'source': {
            'version': '_0_0_1',
            'sourceType': 'lbry_sd_hash',
            'source': 'd5169241150022f996fa7cd6a9a1c421937276a3275eb912790bd07ba7aec1fac5fd45431d226b8fb402691e79aeb24b',
            'contentType': 'derp-text'
        },
        'metadata': {
            'version': '_0_1_0',
            'license': 'Seeyu Incourt v0.0.1',
            'fee': {
                'version': '_0_0_1',
                'currency': 'USD',
                'amount': 1.0,
                'address': 'bKYY1VGNSfxjz48FE8T8vL3cB72wqvT8n7',
            },
            'description': 'protobuf test',
            'language': 'en',
            'title': 'derp title',
            'author': 'jack',
            'nsfw': False
        }
    }
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

my_cert = make_cert(key)
migrate_test = migrate_003_to_010(json.dumps(example_003))
j = json_format.MessageToJson(migrate_test)
c2 = Claim.load(json.loads(j))
signed = sign_stream_claim(c2, key)
print validate_signed_stream_claim(signed, my_cert)
msg = signed.SerializeToString()
print "Json length: %i" % len(json.dumps(example_003))
print "Signed length: %i, unsigned length %i" % (len(c2.SerializeToString()), len(msg))