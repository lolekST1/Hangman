def what_to_do(instructions):
    sim = "Simon says"
    if instructions.count(sim) == 1:
        if instructions.find(sim) == 0:
            return str("I " + instructions[11:])
        elif instructions.rfind(sim) == len(instructions) - 10:
            return str("I " + instructions[:-10])
    return "I won't do it!"
