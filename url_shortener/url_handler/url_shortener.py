import hashlib, base58

def hash(long_url):
    """
    Url shortener utility function.

    Use `sha256` and `base58` to encode long_url.
    """
    sha256 = hashlib.sha256()
    sha256.update(str.encode(long_url))
    sha256_hex_str = int(sha256.hexdigest(), 16)
    sha256_lsb_64num = int(bin(sha256_hex_str)[-64:], 2)

    short_url_byte_num = str(sha256_lsb_64num).encode()
    short_url = base58.b58encode(short_url_byte_num).decode()[:8]

    return short_url