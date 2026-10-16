def response(hey_bob):
    if hey_bob == None or (hey_bob != None and hey_bob.isspace() or hey_bob == ""):
        return "Fine. Be that way!"
    else:
        hey_bob = hey_bob.strip()
        if hey_bob.isupper():
            if hey_bob.endswith("?"):
                return "Calm down, I know what I'm doing!"
            else:
                return "Whoa, chill out!"
        elif hey_bob.endswith("?"):
            return "Sure."
        else:
            return "Whatever."