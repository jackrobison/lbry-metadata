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