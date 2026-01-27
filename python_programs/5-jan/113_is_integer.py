def is_integer(s):
    if not s:
        return False
    if s[0] == "+" or s[0] == "-":
        return s[1:].isdigit()
    return s.isdigit()

print(is_integer("4536"))
print(is_integer("-4756"))
print(is_integer("473r"))
print(is_integer(""))