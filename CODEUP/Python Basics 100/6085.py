w, h, b = map(int, input().split())

memory = format(w * h * b / 8 / 1024 / 1024, ".2f")
print(f"{memory} MB")
