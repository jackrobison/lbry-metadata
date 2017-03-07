from google.protobuf import json_format
from lbrynet.metadata import Metadata
from lbryschema.schema.claim import Claim

# migrate lbrynet json schema (0.0.3) to protobuf (0.1.0)


def migrate_003_to_010(value):
    migrated_to_003 = Metadata.Metadata(value)
    metadata = {
        "version": "_0_1_0"
    }
    for k in ["author", "description", "language", "license", "nsfw", "thumbnail", "title",
              "preview"]:
        if k in migrated_to_003:
            metadata.update({k: migrated_to_003[k]})

    if "fee" in migrated_to_003:
        fee = migrated_to_003["fee"]
        currency = fee.keys()[0]
        amount = fee[currency]['amount']
        address = fee[currency]['address']
        metadata.update(dict(fee={"currency": currency, "version": "_0_0_1",
                                    "amount": amount, "address": address}))
    source = {
        "source": migrated_to_003['sources']['lbry_sd_hash'],
        "contentType": migrated_to_003['content_type'],
        "sourceType": "lbry_sd_hash",
        "version": "_0_0_1"
    }

    migrated = {
        "version": "_0_0_1",
        "stream": {
            "version": "_0_0_1",
            "metadata": metadata,
            "source": source
        }
    }
    return Claim.load(migrated, address_base=58)


def migrate(value):
    try:
        return json_format.Parse(value, Claim)
    except AttributeError:
        return migrate_003_to_010(value)