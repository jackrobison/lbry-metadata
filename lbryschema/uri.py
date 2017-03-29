import string

N_CHAR = ":"
CLAIM_ID_CHAR = "#"
RANK_CHAR = "$"
PROTOCOL_PREFIX = "lbry://"
CHANNEL_PREFIX = "@"
PATH_CHAR = "/"
QUERY_CHAR = "?"
CLAIM_ID_LEN = 40
FORBIDDEN_CHARACTERS = [N_CHAR, RANK_CHAR, CLAIM_ID_CHAR, PATH_CHAR, QUERY_CHAR]


class URIParseError(Exception):
    pass


def contains_forbidden_characters(message):
    for char in message:
        if char in FORBIDDEN_CHARACTERS or char not in string.printable:
            return True
    return False


def extract_hash(partial_uri):
    hex_chars = "0123456789abcdefABCDEF"

    def _get_position(msg):
        for i, char in enumerate(msg):
            if char not in hex_chars:
                return i

    end_of_hash_pos = _get_position(partial_uri)
    if end_of_hash_pos is not None:
        _hash, remaining = partial_uri[:end_of_hash_pos], partial_uri[end_of_hash_pos:]
    else:
        _hash, remaining = partial_uri, ""
    partial_hash = _hash.lower()
    if not partial_hash:
        raise URIParseError("no hash provided")
    if contains_forbidden_characters(partial_hash):
        raise URIParseError("invalid hash")
    if len(partial_hash) > CLAIM_ID_LEN:
        raise URIParseError("hash is too long")
    return partial_hash, remaining


def extract_int(partial_uri):
    def _get_position(msg):
        argstr = str(msg)
        for i, c in enumerate(argstr):
            if c in FORBIDDEN_CHARACTERS:
                return i
    end_of_int_pos = _get_position(partial_uri)
    if end_of_int_pos is not None:
        _i, remaining = partial_uri[:end_of_int_pos], partial_uri[end_of_int_pos:]
    else:
        _i, remaining = partial_uri, ""
    try:
        i = int(_i)
    except ValueError:
        raise URIParseError("invalid integer")
    return i, remaining


def parse_lbry_uri(uri_string):
    """
    Parser for lbry uris, only one filter (:#) may be used at a time

    :param uri_string: format - lbry://name:n$rank#id/path?query
                       optional filters:
                       n (int): preceded by ":", n indicates the nth claim to the name
                       rank (int): preceded by "$", rank indicates the bid queue position of the
                                   claim for the name
                       id (str): preceded by "#", indicates the claim id for the claim
                       path (str): preceded by "/", indicates claim within a channel
                       query (str): preceded by "?", query to be passed to the requested claim
    :return:
    """

    parsed = uri_string
    if parsed.startswith(PROTOCOL_PREFIX):
        parsed = parsed[7:]

    if "@" in parsed:
        if not parsed.startswith("@"):
            raise URIParseError("@ not at the beginning of the name")
        if "@" in parsed[1:]:
            raise URIParseError("invalid @")
        is_channel = True
    else:
        is_channel = False

    if N_CHAR in parsed:
        args = parsed.split(N_CHAR)
        if len(args) != 2:
            raise URIParseError("n parse error")
        parsed = args[0]
        n, p = extract_int(args[1])
        parsed += p
        if n == 0:
            raise URIParseError("n == 0")
    else:
        n = None

    if RANK_CHAR in parsed:
        args = parsed.split(RANK_CHAR)
        if len(args) != 2:
            raise URIParseError("rank parse error")
        parsed = args[0]
        rank, p = extract_int(args[1])
        parsed += p
        if rank == 0:
            raise URIParseError("rank == 0")
    else:
        rank = None

    if CLAIM_ID_CHAR in parsed:
        args = parsed.split(CLAIM_ID_CHAR)
        if len(args) != 2:
            raise URIParseError("claim id parse error")
        claim_id, p = extract_hash(args[1])
        parsed = args[0] + p
    else:
        claim_id = None

    if PATH_CHAR in parsed:
        if not is_channel:
            raise URIParseError("path given for non channel claim")
        args = parsed.split(PATH_CHAR)
        parsed = args[0]
        path = str(PATH_CHAR).join(args[1:])
    else:
        path = None

    if QUERY_CHAR in parsed and path is None:
        args = parsed.split(QUERY_CHAR)
        parsed = args[0]
        query = str(QUERY_CHAR).join(args[1:])
    elif path and QUERY_CHAR in path:
        args = path.split(QUERY_CHAR)
        path = args[0]
        query = str(QUERY_CHAR).join(args[1:])
    else:
        query = None

    if not all(c in string.printable for c in parsed):
        raise URIParseError("invalid characters in name")
    if sum(1 if x is not None else 0 for x in [n, rank, claim_id]) > 1:
        raise URIParseError("too many flags")
    if not parsed:
        raise URIParseError("no name given")
    if contains_forbidden_characters(parsed):
        raise URIParseError("forbidden characters in name")
    if path and contains_forbidden_characters(path):
        raise URIParseError("path contains forbidden characters")
    if query and contains_forbidden_characters(query):
        raise URIParseError("query contains forbidden characters")
    return parsed, is_channel, n, rank, claim_id, path, query
