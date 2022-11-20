def is_palindrome_iterative(word):
    if word == "":
        return False

    char_set = list(word)
    palindrome = "".join(reversed(char_set))

    if word == palindrome:
        return True

    return False
