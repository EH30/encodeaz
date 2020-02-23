import encodeaz

access = encodeaz.azencode()
encoded = access.encode("Hello World!")
print("Encodeed: " + encoded)
print("Decoded: " + access.decode(encoded))
