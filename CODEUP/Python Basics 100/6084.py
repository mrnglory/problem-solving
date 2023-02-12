h, b, c, s = map(int, input().split())

memory = format((h * b * c * s) / 8 / 1024 / 1024, ".1f")
print(f"{memory} MB")
