def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""

    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Masks for checking the two most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # Iterate over each integer (representing a byte) in the data
    for num in data:
        # Only look at the last 8 bits of the integer
        num = num & 0xFF

        # If we're expecting a new UTF-8 character, determine its length
        if n_bytes == 0:
            # Check the leading bits to determine the number of bytes
            if num & mask1 == 0:
                continue  # 1-byte character
            elif num & (mask1 | mask2) == mask1:
                return False  # Invalid byte pattern
            elif num & (mask1 | mask2 | (1 << 5)) == (mask1 | mask2):
                n_bytes = 1  # 2-byte character
            elif num & (mask1 | mask2 | (1 << 5) | (1 << 4)) == \
                       (mask1 | mask2 | (1 << 5)):
                n_bytes = 2  # 3-byte character
            elif num & (mask1 | mask2 | (1 << 5) | (1 << 4) | (1 << 3)) == \
                       (mask1 | mask2 | (1 << 5) | (1 << 4)):
                n_bytes = 3  # 4-byte character
            else:
                return False  # Invalid byte pattern
        else:
            # For continuation bytes, check that they start with '10'
            if not (num & mask1 and not (num & mask2)):
                return False
            n_bytes -= 1

    # If there are remaining bytes expected, it's an invalid encoding
    return n_bytes == 0
