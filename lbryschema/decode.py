import json

from lbryschema.error import DecodeError
from lbryschema.legacy.migrate import migrate as schema_migrator
from lbryschema.claim import ClaimDict

from google.protobuf import json_format  # pylint: disable=no-name-in-module
from google.protobuf.internal.decoder import _DecodeError  # pylint: disable=no-name-in-module,import-error


def migrate_json_claim_value(claim_value):
    try:
        decoded_json = json.loads(claim_value)
        pb_migrated = schema_migrator(decoded_json)
        return pb_migrated
    except json_format.ParseError as parse_error:
        raise DecodeError("Failed to parse protobuf: %s" % parse_error)
    except Exception as err:
        raise DecodeError("Failed to migrate claim: %s" % err)


def smart_decode(claim_value):
    """
    Decode a claim value

    Try decoding claim protobuf, if this fails try decoding json and migrating it.
    If unable to decode or migrate, raise DecodeError
    """

    try:
        decoded_claim = ClaimDict.deserialize(claim_value)
        return decoded_claim
    except _DecodeError:
        migrated_claim = migrate_json_claim_value(claim_value)
        return migrated_claim
