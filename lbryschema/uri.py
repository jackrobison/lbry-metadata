import re
from collections import namedtuple
from lbryschema.error import URIParseError


def render_uri(uri_named_tuple):
    uri_str = "lbry://%s" % uri_named_tuple.name
    if uri_named_tuple.claim_sequence is not None:
        uri_str += ":%i" % uri_named_tuple.claim_sequence
    elif uri_named_tuple.bid_position is not None:
        uri_str += "$%i" % uri_named_tuple.bid_position
    elif uri_named_tuple.claim_id is not None:
        uri_str += "#%s" % uri_named_tuple.claim_id
    if uri_named_tuple.path is not None:
        uri_str += "/%s" % uri_named_tuple.path
    if uri_named_tuple.query is not None:
        uri_str += "?%s" % uri_named_tuple.query
    return uri_str


LBRYURIType = namedtuple('URI', ['name', 'is_channel', 'claim_sequence', 'bid_position', 'claim_id',
                             'path', 'query'])


class LBRYURI(LBRYURIType):
    __slots__ = ()

    def __repr__(self):
        return render_uri(self)

    def __str__(self):
        return render_uri(self)

    def __eq__(self, other):
        if isinstance(other, str):
            return tuple(self) == tuple(parse_lbry_uri(other))
        return tuple(self) == tuple(other)


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
    positive_number = "[1-9][0-9]*"
    number = '\-?' + positive_number

    protocol = _named("protocol", re.escape("lbry://"))

    content_name = _named("content_name", name)
    channel_name = _named("channel_name", channel_char + name)
    content_or_channel_name = _named("content_or_channel_name", content_name + "|" + channel_name)

    claim_id_piece = _named("claim_id", "[0-9a-f]{1," + str(claim_id_len) + "}")
    claim_id = _group(claim_id_char + claim_id_piece)

    bid_position_piece = _named("bid_position", number)
    bid_position = _group(n_char + bid_position_piece)

    claim_sequence_piece = _named("claim_sequence", number)
    claim_sequence = _group(rank_char + claim_sequence_piece)

    modifier = _named("modifier", claim_id + "|" + bid_position + "|" + claim_sequence)

    path_item = _group(name)
    path_item_cont = _group(path_char + name)
    path_piece = _named("path", path_item + path_item_cont + '*')
    path = _group(path_char + path_piece)

    query_piece = _named("query", "[a-zA-Z0-9=&]+")
    query = _group(query_char + query_piece)

    uri = _named("uri", (
        '^' +
        protocol + '?' +
        content_or_channel_name +
        modifier + '?' +
        path + '?' +
        query + '?' +
        '$'
    ))

    return uri


def parse_lbry_uri(uri_string):
    """
    Parser for lbry uris, only one filter (:#) may be used at a time

    :param uri_string: format - lbry://name:n$rank#id/path?query
                       optional filters:
                       claim_sequence (int): preceded by ":", indicates the nth claim to the name
                       bid_position (int): preceded by "$", indicates the bid queue position of the
                                   claim for the name
                       claim_id (str): preceded by "#", indicates the claim id for the claim
                       path (str): preceded by "/", indicates claim within a channel
                       query (str): preceded by "?", query to be passed to the requested claim
    :return: URI
    """

    match = re.match(get_schema_regex(), uri_string)

    if match is None:
        raise URIParseError('Invalid URI')

    uri_tuple = (
        match.group("content_or_channel_name"),
        True if match.group("channel_name") else False,
        int(match.group("bid_position")) if match.group("bid_position") is not None else None,
        int(match.group("claim_sequence")) if match.group("claim_sequence") is not None else None,
        match.group("claim_id"),
        match.group("path"),
        match.group("query")
    )
    return LBRYURI(*uri_tuple)
