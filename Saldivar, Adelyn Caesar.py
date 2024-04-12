def caesar_cipher(text_list, shift_list):
    encrypted_texts = []
    for text, shift in zip(text_list, shift_list):
        result = ''
        for char in text:
            if char.isalpha():
                ascii_code = ord(char)
                if char.isupper():
                    shifted_code = (ascii_code - 65 + shift) % 26 + 65
                elif char.islower():
                    shifted_code = (ascii_code - 97 + shift) % 26 + 97
                result += chr(shifted_code)
            else:
                result += char
        encrypted_texts.append(result)
    return encrypted_texts

plaintext = ["Adelyn Saldivar", "BSIT", "IT36A", "Aim to Excel"]
shift = [3, 3, 3, 3]
encrypted_texts = caesar_cipher(plaintext, shift)
print("Encrypted:", encrypted_texts)

# Now to decrypt, we need to apply the reverse of the shifts
decrypted_texts = caesar_cipher(encrypted_texts, [-s for s in shift])
print("Decrypted:", decrypted_texts)
