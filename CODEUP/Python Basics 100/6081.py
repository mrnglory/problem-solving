multiplicand = int(input(), 16)

for multiplier in range(1, int("F", 16) + 1):
    print("%X"%multiplicand, "*%X"%multiplier, "=%X"%(multiplicand * multiplier), sep="")
