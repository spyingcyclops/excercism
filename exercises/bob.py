def response(hey_bob):

    resps = {
        0: "Fine, be that way.",
        1: "Sure.",
        2: "Calm down, I know what I'm doing!",
        3: "Whoa, chill out!",
        4: "Whatever.",
    }

    is_question = False
    if hey_bob[-1] == "?":
        is_question = True

    punc = """! ()-[]{};:'"\,<>.?/@#$%^&*_~"""
    for i in hey_bob:
        if i in punc:
            hey_bob = hey_bob.replace(i, "")

    if hey_bob == "":
        return resps[0]
    if is_question and not all(map(str.isupper, hey_bob)):
        return resps[1]
    if is_question and all(map(str.isupper, hey_bob)):
        return resps[2]
    if not is_question and all(map(str.isupper, hey_bob)):
        return resps[3]
    else:
        return resps[4]


print(response("1, 2, 3 GO!"))
