s = input()
r = [x for x in s if x not in ",.!?"]
r = "".join(r)
print(r.lower())
