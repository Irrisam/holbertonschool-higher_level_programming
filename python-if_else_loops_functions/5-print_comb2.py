#!/usr/bin/python3
coma = "0"
for i in range(0, 99):
    if i > 9:
        coma = ", "
    print(f"{coma}{i}", end="")
    if i <= 9:
        coma = ", 0"
i += 1
print("\n")