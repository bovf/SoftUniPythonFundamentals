message = input()
message_ciphered = ""

for char in message:
    new_char = chr(ord(char) + 3)
    message_ciphered += new_char

print(message_ciphered)
