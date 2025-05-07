import zlib

mode = input()

match mode:
    case "pack":
        text = input()
        compressed = zlib.compress(text.encode(), level=9)
        print(len(compressed))
        print(*compressed)
    case "unpack":
        length = int(input())
        compressed = bytes(map(int, input().split()))
        decompressed = zlib.decompress(compressed)
        print(decompressed.decode())
