def get_sum_pairs(n):
    for i in range(1, n // 2 + 1):
        yield (n - i, i)

with open("enc", "r", encoding="utf-8") as f:
    enc = f.read()

possible_char_pairs = []
for i in range(0, len(enc)):
    possible_char_pairs.append([])
    sum_ = ord(enc[i])
    sum_pairs = list(filter(lambda p: p[0] >> 8 > 0 and p[0] & 0xFF00 == p[0], get_sum_pairs(sum_)))

    for p in sum_pairs:
        i1 = p[0] >> 8
        c1 = chr(i1)
        i2 = p[1]
        c2 = chr(i2)

        if (c1.isprintable() and c1.isascii()) and (c2.isprintable() and c2.isascii()):
            possible_char_pairs[i].append(c1 + c2)

print("".join(x[0] for x in possible_char_pairs))