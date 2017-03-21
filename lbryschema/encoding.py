import base64
from copy import deepcopy
from lbryschema.base import base_decode, base_encode
from lbryschema.schema import CLAIM_TYPES, CLAIM_TYPE, STREAM_TYPE, CERTIFICATE_TYPE
from lbryschema.schema import SIGNATURE


def encode_fields(claim_dictionary):
    """Encode bytes to hex and b58 for return by ClaimDict"""
    claim_dictionary = deepcopy(claim_dictionary)
    claim_type = CLAIM_TYPES[claim_dictionary[CLAIM_TYPE]]
    claim_value = claim_dictionary[claim_type]
    if claim_type == CLAIM_TYPES[STREAM_TYPE]:
        claim_value['source']['source'] = claim_value['source']['source'].encode('hex')
        if 'fee' in claim_value['metadata']:
            address = base_encode(claim_value['metadata']['fee']['address'], 58)
            claim_value['metadata']['fee']['address'] = address
    elif claim_type == CLAIM_TYPES[CERTIFICATE_TYPE]:
        public_key = claim_value["publicKey"]
        claim_value["publicKey"] = public_key.encode('hex')
    if SIGNATURE in claim_dictionary:
        claim_dictionary[SIGNATURE]['signature'] = claim_dictionary[SIGNATURE]['signature'].encode('hex')
        claim_dictionary[SIGNATURE]['certificateId'] = \
            claim_dictionary[SIGNATURE]['certificateId'].encode('hex')

    claim_dictionary[claim_type] = claim_value
    return claim_dictionary


def decode_fields(claim_dictionary):
    """Decode hex and b58 encoded bytes in dictionaries given to ClaimDict"""
    claim_dictionary = deepcopy(claim_dictionary)
    claim_type = CLAIM_TYPES[claim_dictionary[CLAIM_TYPE]]
    claim_value = claim_dictionary[claim_type]
    if claim_type == CLAIM_TYPES[STREAM_TYPE]:
        claim_value['source']['source'] = claim_value['source']['source'].decode('hex')
        if 'fee' in claim_value['metadata']:
            address = base_decode(claim_value['metadata']['fee']['address'], 25, 58)
            claim_value['metadata']['fee']['address'] = address
    elif claim_type == CLAIM_TYPES[CERTIFICATE_TYPE]:
        public_key = claim_value["publicKey"].decode('hex')
        claim_value["publicKey"] = public_key
    if SIGNATURE in claim_dictionary:
        claim_dictionary[SIGNATURE]['signature'] = claim_dictionary[SIGNATURE]['signature'].decode('hex')
        claim_dictionary[SIGNATURE]['certificateId'] = \
            claim_dictionary[SIGNATURE]['certificateId'].decode('hex')
    claim_dictionary[claim_type] = claim_value
    return claim_dictionary


def decode_b64_fields(claim_dictionary):
    """Decode b64 encoded bytes in protobuf generated dictionary to be given to ClaimDict"""
    claim_dictionary = deepcopy(claim_dictionary)
    claim_type = CLAIM_TYPES[claim_dictionary[CLAIM_TYPE]]
    claim_value = claim_dictionary[claim_type]
    if claim_type == CLAIM_TYPES[STREAM_TYPE]:
        claim_value['source']['source'] = base64.b64decode(claim_value['source']['source'])
        if 'fee' in claim_value['metadata']:
            address = base64.b64decode(claim_value['metadata']['fee']['address'])
            claim_value['metadata']['fee']['address'] = address
    elif claim_type == CLAIM_TYPES[CERTIFICATE_TYPE]:
        public_key = base64.b64decode(claim_value["publicKey"])
        claim_value["publicKey"] = public_key
    if SIGNATURE in claim_dictionary:
        claim_dictionary[SIGNATURE]['signature'] = base64.b64decode(claim_dictionary[SIGNATURE]['signature'])
        claim_dictionary[SIGNATURE]['certificateId'] = \
            base64.b64decode(claim_dictionary[SIGNATURE]['certificateId'])

    claim_dictionary[claim_type] = claim_value
    return claim_dictionary
