def add_prefix_un(word):
    return "un" + word


def make_word_groups(words):
    prefix = words.pop(0)
    longwords = [prefix]
    for i in words:
        longwords.append(prefix + i)
        x = " :: ".join(longwords)
    return prefix + " :: " + x


# for i in words:
#     (words[0] + " :: ").join(words)
#     return(words)


def remove_suffix_ness(word):
    if word.endswith("iness"):
        return word.replace("iness", "y")

    elif word.endswith("ness"):
        return word.replace("ness", "")

    else:
        return "Suffix was not found in the word."


def adjective_to_verb(sentence, index):
    sentence = sentence.replace(".", "")
    x = sentence.split()
    verb = x[index] + "en"
    return verb


# 1
print("\n1. Add a prefix to a word")
add_prefix_un("happy")

# 2
print("\n2. Add prefixes to word groups")
make_word_groups(["en", "close", "joy", "lighten"])
make_word_groups(["pre", "serve", "dispose", "position"])
make_word_groups(["auto", "didactic", "graph", "mate"])
make_word_groups(["inter", "twine", "connected", "dependent"])
make_word_groups(
    [
        "auto",
        "didactic",
        "graph",
        "mate",
        "chrome",
        "centric",
        "complete",
        "echolalia",
        "encoder",
        "biography",
    ]
)

# 3
print("\n3. Remove a suffix from a word")
remove_suffix_ness("heaviness")
remove_suffix_ness("sadness")
remove_suffix_ness("softness")
remove_suffix_ness("crabbiness")
remove_suffix_ness("lightness")
remove_suffix_ness("artiness")
remove_suffix_ness("edginess")


# 4
print("\n4. Extract and transform a word")
adjective_to_verb("I need to make that bright.", -1)
adjective_to_verb("Charles made weak crying noises.", 2)
