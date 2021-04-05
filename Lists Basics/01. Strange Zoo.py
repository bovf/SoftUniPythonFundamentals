meerkat = []

tail = input()
body = input()
head = input()

meerkat.extend((tail, body, head))
meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

print(meerkat)