def encrypt(text, n):
    if text and n > 0:
        for _ in range(n):
            text = "".join(list(text)[1::2] + list(text)[0::2])
    return text


def decrypt(encrypted_text, n):
    text = encrypted_text
    if encrypted_text and n > 0:
        for _ in range(n):
            second_chars = text[0:(len(text) // 2)]
            other_chars = text[(len(text) // 2):]
            print(second_chars, other_chars)
            if len(text) % 2 == 0:
                text = "".join([a + b for a, b in zip(other_chars, second_chars)])
            else:
                text = "".join([a + b for a, b in zip(other_chars, second_chars)]) + other_chars[-1]
    return text
