text = input()
digits = []
letters = []
other_chars = []

for ch in text:
    if ch.isdigit():
        digits.append(ch)
    elif ch.isalpha():
        letters.append(ch)
    else:
        other_chars.append(ch)

print(f"{''.join(digits)}")
print(f"{''.join(letters)}")
print(f"{''.join(other_chars)}")
