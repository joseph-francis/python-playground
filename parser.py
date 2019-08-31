class Sentence(object):
    def __init__(self, subject, verb, obj):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]


def peek(word_list):
    if word_list:
        print(word_list[0][0])
        return word_list[0][0]
    else:
        return None


def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    while peek(word_list) == word_type:
        print("match called")
        match(word_list, word_type)


def parse_verb(word_list):
    skip(word_list, "stop")

    if peek(word_list) == "verb":
        return match(word_list, "verb")
    else:
        return ValueError("There was an error")


def parse_objects(word_list):
    skip(word_list, "stop")
    next_word = peek(word_list)

    if next_word == "noun":
        return match(word_list, "noun")
    elif next_word == "direction":
        return match(word_list, "direction")
    else:
        raise ValueError("There was an another problem.")


def parse_subject(word_list):
    skip(word_list, "stop")
    next_word = peek(word_list)

    if next_word == "noun":
        return match(word_list, "noun")
    elif next_word == "verb":
        return match("noun", "player")
    else:
        raise ValueError("Then again, another problem.")


def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_objects(word_list)
    print(f"OBJECT: {verb}")
    return Sentence(subj, verb, obj)


x = parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
print(x.verb)
