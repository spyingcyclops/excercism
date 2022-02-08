def response(hey_bob):
    resps = {
        0: "Fine. Be that way!",
        1: "Sure.",
        2: "Calm down, I know what I'm doing!",
        3: "Whoa, chill out!",
        4: "Whatever.",
    }

    if hey_bob == "" or hey_bob.isspace() or hey_bob == "\t\t\t\t\t\t\t\t\t\t":
        return resps[0]
    else:
        is_question = False
        if len(hey_bob) > 0 and hey_bob[-1] == "?":
            is_question = True

        if is_question and not hey_bob.isupper():
            return resps[1]
        if is_question and hey_bob.isupper():
            return resps[2]
        if not is_question and hey_bob.isupper():
            return resps[3]
        else:
            return resps[4]

