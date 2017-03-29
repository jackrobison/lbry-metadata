import string
import re

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


def get_schema_regex():
    def _named(name, regex):
        return "(?P<" + name + ">" + regex + ")"

    def _group(regex):
        return "(?:" + regex + ")"

    n_char = re.escape(":")
    claim_id_char = re.escape("#")
    rank_char = re.escape("$")
    channel_char = re.escape("@")
    path_char = re.escape("/")
    query_char = re.escape("?")

    claim_id_len = 40

    name = "[a-zA-Z0-9]+"  # expand later

    protocol = _named("protocol", re.escape("lbry://"))

    content_name = _named("content_name", name)
    channel_name = _named("channel_name", channel_char + name)
    content_or_channel_name = _named("content_or_channel_name", content_name + "|" + channel_name)

    claim_id_piece = _named("claim_id", "[0-9a-f]{1," + str(claim_id_len) + "}")
    claim_id = _group(claim_id_char + claim_id_piece)

    n_piece = _named("n", "\-?[1-9][0-9]*")
    n = _group(n_char + n_piece)

    rank_piece = _named("rank", "\-?[1-9][0-9]*")
    rank = _group(rank_char + rank_piece)

    modifier = _named("modifier", claim_id + "|" + n + "|" + rank)

    path_item = _group(name)
    path_item_cont = _group(path_char + name)
    path_piece = _named("path", path_item + path_item_cont + '*')
    path = _group(path_char + path_piece)

    query_piece = _named("query", "[a-zA-Z0-9=&]+")
    query = _group(query_char + query_piece)

    uri = _named("uri", (
        '^' + protocol + '?' + content_or_channel_name + modifier + '?' + path + '?' + query + '?' + '$'
    ))

    return uri


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

    match = re.match(get_schema_regex(), uri_string)

    if match is None:
        raise URIParseError('Invalid URI')

    # return match.groupdict()
    return tuple([
        match.group("content_or_channel_name"),
        True if match.group("channel_name") else False,
        int(match.group("n")) if match.group("n") is not None else None,
        int(match.group("rank")) if match.group("rank") is not None else None,
        match.group("claim_id"),
        match.group("path"),
        match.group("query"),
    ])
