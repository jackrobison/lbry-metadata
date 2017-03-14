V_0_0_1 = "_0_0_1"
V_0_0_2 = "_0_0_2"
V_0_0_3 = "_0_0_3"
V_0_1_0 = "_0_1_0"


VERSION_MAP = {
    V_0_0_1: 1,
    V_0_0_2: 2,
    V_0_0_3: 3,
    V_0_1_0: 4,
}

LBC = "LBC"
BTC = "BTC"
USD = "USD"

CURRENCY_MAP = {
    LBC: 1,
    BTC: 2,
    USD: 3
}

ADDRESS_LENGTH = 25
VERSION = "version"
STREAM_TYPE = "streamType"
CERTIFICATE_TYPE = "certificateType"
CLAIM_TYPE = "claimType"
SIGNATURE = "publisherSignature"

CLAIM_TYPES = {
    STREAM_TYPE: "stream",
    CERTIFICATE_TYPE: "certificate"
}

ECDSA = "ECDSA"

KEY_TYPES = {
    ECDSA: 1
}

LBRY_SD_HASH = "lbry_sd_hash"
LBRY_SD_HASH_LENGTH = 48

SOURCE_TYPES = {
    LBRY_SD_HASH: 1
}
