import zlib
import struct
import base64


def gzip_compress_exact_match(data):
    compressor = zlib.compressobj(
        6,
        zlib.DEFLATED,
        -zlib.MAX_WBITS,
        8,
        zlib.Z_DEFAULT_STRATEGY
    )
    compressed = compressor.compress(data)
    compressed += compressor.flush(zlib.Z_FINISH)

    header = b'\x1f\x8b'
    header += b'\x08'
    header += b'\x00'
    header += b'\x00\x00\x00\x00'
    header += b'\x00'
    header += b'\x00'

    crc32 = zlib.crc32(data) & 0xFFFFFFFF
    isize = len(data) & 0xFFFFFFFF
    trailer = struct.pack('<I', crc32)
    trailer += struct.pack('<I', isize)
    gzip_data = header + compressed + trailer
    return base64.b64encode(gzip_data).decode('ascii')


if __name__ == '__main__':
    res = gzip_compress_exact_match("abc".encode())
    print(res)