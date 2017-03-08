import os
from Crypto.PublicKey import RSA


def pack_sig(sig_long):
    while sig_long:
        yield chr(sig_long & 0xFF)
        sig_long >>= 8


def unpack_sig(sig_bytes):
    cnt = 0
    total = 0
    while sig_bytes:
        total += sig_bytes.pop() * (256 ** cnt)
        cnt += 1
    return (total, )


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


__b58chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
assert len(__b58chars) == 58

__b43chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ$*+-./:'
assert len(__b43chars) == 43


def base_decode(v, length, base):
    """ decode v into a string of len bytes."""
    if base == 58:
        chars = __b58chars
    elif base == 43:
        chars = __b43chars
    long_value = 0L
    for (i, c) in enumerate(v[::-1]):
        long_value += chars.find(c) * (base**i)
    result = ''
    while long_value >= 256:
        div, mod = divmod(long_value, 256)
        result = chr(mod) + result
        long_value = div
    result = chr(long_value) + result
    nPad = 0
    for c in v:
        if c == chars[0]: nPad += 1
        else: break
    result = chr(0)*nPad + result
    if length is not None and len(result) != length:
        return None
    return result