def encode(plain):
    """
    encode('javad')
    >>> [106, 97, 118, 97, 100]
    """
    return [ord(elm) for elm in plain]

def decode(encode):
    """
    decode([106, 97, 118, 97, 100])
    >>> javad
    """
    return "".join(chr(elm) for elm in encode)
