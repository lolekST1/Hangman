def check_email(string):
    if " " not in string and "@" in string and "@." not in string:
        if string.find("@") < string.rfind("."):
            return True
    return False
