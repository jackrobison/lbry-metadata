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
