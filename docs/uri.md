# URI

## Regex

If you are a robot and prefer regexes to English, here's the full regex for lbry:// URIs:

```
(?P<uri>
  ^
  (?P<protocol>lbry\:\/\/)?
  (?P<content_or_channel_name>
    (?P<content_name>[a-zA-Z0-9\-]+)
    |
    (?P<channel_name>\@[a-zA-Z0-9\-]{4,})
  )
  (?P<modifier>
    (?:\#(?P<claim_id>[0-9a-f]{1,40}))
    |
    (?:\$(?P<bid_position>\-?[1-9][0-9]*))
    |
    (?:\:(?P<claim_sequence>\-?[1-9][0-9]*))
  )?
  (?:\/(?P<path>[a-zA-Z0-9\-]+))?
  $
)

```

## Protocol

The LBRY protocol is called `lbry`. URIs using the protocol must start with `lbry://`.

## Reserved characters

- CHANNEL_CHAR = '@'
- CLAIM_ID_CHAR = '#'
- CLAIM_SEQUENCE_CHAR = ':'
- BID_POSITION_CHAR = '$'
- PATH_CHAR = '/'
- QUERY_CHAR = '?'

## Names

Names may contain English letters (upper and lower case), numbers, and hyphens.

### Content Name

`content_name` is the name of piece of content. 

### Channel Name

## Modifiers

Only one modifier is allowed at a time.

### Claim ID

### Claim Sequence

### Bid Position

## Path

## Query Params

_not implemented yet_