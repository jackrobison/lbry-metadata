from lbryschema.schema.claim import Claim
# migrate lbrynet json schema (0.0.3) to protobuf (0.1.0)


def migrate_003_to_010(old_dict):
    metadata = {
        "version": "_0_1_0"
    }
    for k in ["author", "description", "language", "license", "nsfw", "thumbnail", "title", "preview"]:
        if k in old_dict:
            metadata.update({k: old_dict[k]})

    if "fee" in old_dict:
        fee = old_dict["fee"]
        currency = fee.keys()[0]
        amount = fee[currency]['amount']
        address = fee[currency]['address']
        metadata.update(
            {
                "fee": {
                    "currency": currency,
                    "version": "_0_0_1",
                    "amount": amount,
                    "address": address
                }
            }
        )

    source = {
        "source": old_dict['sources']['lbry_sd_hash'],
        "contentType": old_dict['content_type'],
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
    return Claim.load(migrated)
