#!/usr/bin/python3

import dis

with open("hidden_4.pyc", "r") as file:
    code = file.read()
    instructions = dis.get_instructions(code)
    names = set()
    for instruction in instructions:
        if instruction.opname == "STORE_NAME"